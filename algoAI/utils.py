import os
import joblib
import numpy as np

def get_model_config(model_name):
    from .ml_configs import ML_CONFIGS
    return ML_CONFIGS.get(model_name)

def load_ml_model(model_name):
    from .ml_configs import ML_CONFIGS
    
    if model_name not in ML_CONFIGS:
        raise ValueError(f"Model {model_name} not found")
    
    config = ML_CONFIGS[model_name]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')

    # Load model
    model_path = os.path.join(models_dir, config['model_file'])
    loaded_model = joblib.load(model_path)
    # Handle case where model file contains a dict with 'model' key
    if isinstance(loaded_model, dict) and 'model' in loaded_model:
        model = loaded_model['model']
    else:
        model = loaded_model

    # Load scaler if exists
    scaler = None
    if config.get('scaler_file'):
        scaler_path = os.path.join(models_dir, config['scaler_file'])
        loaded_scaler = joblib.load(scaler_path)
        # Handle case where scaler file contains a dict with 'scaler' key
        if isinstance(loaded_scaler, dict) and 'scaler' in loaded_scaler:
            scaler = loaded_scaler['scaler']
        else:
            scaler = loaded_scaler
    
    return model, scaler

def prepare_input_features(model_name, post_data):
    """
    Standard feature preparation for classification models
    Only converts numeric fields to float
    """
    config = get_model_config(model_name)
    features = []
    input_dict = {}
    
    for field in config['input_fields']:
        field_name = field['name']
        field_type = field.get('type', 'number')
        
        # Get the value from POST data or use default
        value = post_data.get(field_name, field['default'])
        
        # Only convert to float if it's a numeric field
        if field_type in ['number', 'radio', 'select']:
            # For select/radio, check if the value is already numeric
            try:
                value = float(value)
            except (ValueError, TypeError):
                # If conversion fails, it might be a string option
                # Keep it as is for now (shouldn't happen for classification models)
                pass
        
        features.append(value)
        input_dict[field_name] = value
    
    return features, input_dict

def make_prediction(model_name, features):
    model, scaler = load_ml_model(model_name)
    features_array = np.array([features])
    
    if scaler is not None:
        features_scaled = scaler.transform(features_array)
    else:
        features_scaled = features_array
    
    prediction = model.predict(features_scaled)
    return int(prediction[0])

def interpret_prediction(model_name, prediction_value):
    config = get_model_config(model_name)
    prediction_class = int(prediction_value)
    
    if prediction_class in config['output_classes']:
        return config['output_classes'][prediction_class]
    
    return None

def get_model_info(model_name):
    config = get_model_config(model_name)
    if not config:
        return None
    
    return {
        'name': config['name'],
        'display_name': config['display_name'],
        'description': config['description'],
        'uses_scaler': config.get('scaler_file') is not None,
        'scaler_file': config.get('scaler_file'),
        'model_file': config['model_file'],
        'num_features': len(config['input_fields']),
        'num_classes': len(config['output_classes'])
    }

def prepare_regression_features(model_name, post_data):
    """
    Special handling for regression models with OneHotEncoded features
    """
    config = get_model_config(model_name)
    
    # Check which regression model this is
    if model_name in ['Random_Forest_regression',
                      'SVM_regression', 
                      'regression_linaire', 
                      'Decision_Tree_regression', 
                      'XGB_regression',
                      'SVM_regression'
                      ]:
        return prepare_car_price_features(post_data)
    else:
        # Use standard preparation for other models
        return prepare_input_features(model_name, post_data)

def prepare_car_price_features(post_data):
    """
    Prepare features for car price prediction models
    Handles OneHotEncoding for Make, Model, and Fuel_Type
    
    Expected order:
    ['Make_Audi', 'Make_BMW', 'Make_Ford', 'Make_Honda', 'Make_Toyota',
     'Model_Model A', 'Model_Model B', 'Model_Model C', 'Model_Model D', 'Model_Model E',
     'Fuel Type_Diesel', 'Fuel Type_Electric', 'Fuel Type_Petrol',
     'Year', 'Engine Size', 'Mileage', 'Transmission']
    """
    
    # Get values from form
    make = post_data.get('Make', 'Honda')
    model = post_data.get('Model', 'Model B')
    fuel_type = post_data.get('Fuel_Type', 'Petrol')
    transmission = int(post_data.get('Transmission', 0))
    year = float(post_data.get('Year', 2015))
    engine_size = float(post_data.get('Engine_Size', 2.5))
    mileage = float(post_data.get('Mileage', 50000))
    
    # Initialize features array (17 features total)
    features = []
    
    # One-hot encode Make (5 features)
    make_options = ['Audi', 'BMW', 'Ford', 'Honda', 'Toyota']
    for option in make_options:
        features.append(1 if make == option else 0)
    
    # One-hot encode Model (5 features)
    model_options = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
    for option in model_options:
        features.append(1 if model == option else 0)
    
    # One-hot encode Fuel Type (3 features)
    fuel_options = ['Diesel', 'Electric', 'Petrol']
    for option in fuel_options:
        features.append(1 if fuel_type == option else 0)
    
    # Add numerical features (4 features)
    features.extend([year, engine_size, mileage, transmission])
    
    # Create input dictionary for display
    input_dict = {
        'Make': make,
        'Model': model,
        'Fuel Type': fuel_type,
        'Transmission': 'Automatic' if transmission == 0 else 'Manual',
        'Year': int(year),
        'Engine Size': engine_size,
        'Mileage': int(mileage)
    }
    
    return features, input_dict

def make_regression_prediction(model_name, features):
    """
    Make prediction for regression models (returns continuous value)
    """
    model, scaler = load_ml_model(model_name)
    features_array = np.array([features])
    
    # Apply scaling if scaler exists
    if scaler is not None:
        # Only Random Forest and SVM regression use scalers
        if model_name in ['Random_Forest_regression', 'SVM_regression']:
            # Feature structure (17 total features):
            # [0-4]: Make (one-hot encoded, 5 features)
            # [5-9]: Model (one-hot encoded, 5 features)
            # [10-12]: Fuel_Type (one-hot encoded, 3 features)
            # [13]: Year - NEEDS SCALING
            # [14]: Engine_Size - NEEDS SCALING
            # [15]: Mileage - NEEDS SCALING
            # [16]: Transmission - NO SCALING (categorical 0/1)
            
            # Split features
            one_hot_features = features_array[:, :13]  # Indices 0-12: one-hot encoded
            year = features_array[:, 13:14]             # Index 13: Year
            engine_size = features_array[:, 14:15]      # Index 14: Engine_Size
            mileage = features_array[:, 15:16]          # Index 15: Mileage
            transmission = features_array[:, 16:17]     # Index 16: Transmission
            
            # Combine only the 3 features that need scaling
            features_to_scale = np.concatenate([year, engine_size, mileage], axis=1)
            
            # Scale these 3 features
            scaled_features = scaler.transform(features_to_scale)
            
            # Reconstruct full feature array in correct order:
            # [one-hot (13)] + [scaled Year, Engine, Mileage (3)] + [Transmission (1)]
            features_array = np.concatenate([
                one_hot_features,   # 0-12
                scaled_features,    # 13-15 (scaled)
                transmission        # 16 (not scaled)
            ], axis=1)
        else:
            # Standard scaling for other regression models
            features_array = scaler.transform(features_array)
    
    # XGBoost and other models without scalers use features as-is
    # Make prediction
    prediction = model.predict(features_array)
    predicted_value = float(prediction[0])
    
    return predicted_value

def interpret_regression_prediction(model_name, prediction_value):
    """
    Interpret regression prediction (continuous value)
    """
    config = get_model_config(model_name)
    
    # Format price nicely for car price models
    return {
        'label': f'${prediction_value:,.2f}',
        'value': prediction_value,
        'image': config['output_classes'][0]['image'],
        'badge_class': config['output_classes'][0]['badge_class'],
        'description': f'Estimated car price: ${prediction_value:,.2f}'
    }

def validate_model_files(model_name):
    config = get_model_config(model_name)
    if not config:
        return False, f"Model config not found: {model_name}"
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')
    
    model_path = os.path.join(models_dir, config['model_file'])
    if not os.path.exists(model_path):
        return False, f"Model file not found: {config['model_file']}"
    
    if config.get('scaler_file'):
        scaler_path = os.path.join(models_dir, config['scaler_file'])
        if not os.path.exists(scaler_path):
            return False, f"Scaler file not found: {config['scaler_file']}"
    
    return True, "All files valid"