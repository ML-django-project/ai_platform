
import os
import joblib
import numpy as np

def get_model_config(model_name):
    """Get configuration for a specific model"""
    from .ml_configs import ML_CONFIGS
    return ML_CONFIGS.get(model_name)

def load_ml_model(model_name):
    """Load the ML model and scaler from disk"""
    from .ml_configs import ML_CONFIGS
    
    if model_name not in ML_CONFIGS:
        raise ValueError(f"Model {model_name} not found")
    
    config = ML_CONFIGS[model_name]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')

    # Load model
    model_path = os.path.join(models_dir, config['model_file'])
    model = joblib.load(model_path)

    # Load scaler if exists
    scaler = None
    if config.get('scaler_file'):
        scaler_path = os.path.join(models_dir, config['scaler_file'])
        scaler = joblib.load(scaler_path)
    
    return model, scaler

def prepare_input_features(model_name, post_data):
    """Prepare input features from POST data"""
    config = get_model_config(model_name)
    features = []
    input_dict = {}
    
    for field in config['input_fields']:
        field_name = field['name']
        value = float(post_data.get(field_name, field['default']))
        features.append(value)
        input_dict[field_name] = value
    
    return features, input_dict

def make_prediction(model_name, features):
    """Make prediction using the model"""
    model, scaler = load_ml_model(model_name)
    features_array = np.array([features])
    
    if scaler is not None:
        features_scaled = scaler.transform(features_array)
    else:
        features_scaled = features_array
    
    prediction = model.predict(features_scaled)
    return int(prediction[0])

def interpret_prediction(model_name, prediction_value):
    """Get the output class info for a prediction"""
    config = get_model_config(model_name)
    prediction_class = int(prediction_value)
    
    if prediction_class in config['output_classes']:
        return config['output_classes'][prediction_class]
    
    return None

def get_model_info(model_name):
    """Get model metadata"""
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

def validate_model_files(model_name):
    """Check if model files exist"""
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