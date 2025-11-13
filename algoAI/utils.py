
import os
import joblib
from django.conf import settings
from .ml_configs import ML_CONFIGS

def load_ml_model(model_name):
    """Load a machine learning model by name"""
    if model_name not in ML_CONFIGS:
        raise ValueError(f"Model {model_name} not found in configurations")
    
    config = ML_CONFIGS[model_name]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')
    model_path = os.path.join(models_dir, config['model_file'])
    
    return joblib.load(model_path)

def get_model_config(model_name):
    """Get configuration for a specific model"""
    return ML_CONFIGS.get(model_name)

def prepare_input_features(model_name, post_data):
    """Prepare input features based on model configuration"""
    config = get_model_config(model_name)
    features = []
    input_dict = {}
    
    for field in config['input_fields']:
        field_name = field['name']
        value = float(post_data.get(field_name, field['default']))
        features.append(value)
        input_dict[field_name] = value
    
    return features, input_dict

def interpret_prediction(model_name, prediction_value):
    """Interpret prediction result based on model configuration"""
    config = get_model_config(model_name)
    prediction_class = int(prediction_value)
    
    if prediction_class in config['output_classes']:
        return config['output_classes'][prediction_class]
    
    return None