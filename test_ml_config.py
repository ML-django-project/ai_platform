# test_ml_config.py
# Run this file to test if your ml_configs.py is working correctly
# Place this file in your project root (same level as manage.py)
# Run: python test_ml_config.py

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_platform.settings')
django.setup()

from algoAI.ml_configs import ML_CONFIGS, FIELDS, OUTPUT_CLASSES

print("=" * 80)
print("🧪 TESTING ML_CONFIGS.PY")
print("=" * 80)

# Test 1: Check if ML_CONFIGS exists
print("\n✅ TEST 1: ML_CONFIGS Dictionary")
print(f"   Found {len(ML_CONFIGS)} models")
print(f"   Model names: {list(ML_CONFIGS.keys())}")

# Test 2: Check if Random_Forest_classification exists
print("\n✅ TEST 2: Random_Forest_classification Exists")
if 'Random_Forest_classification' in ML_CONFIGS:
    print("   ✅ Found!")
    rf_config = ML_CONFIGS['Random_Forest_classification']
    print(f"   Display Name: {rf_config['display_name']}")
    print(f"   Description: {rf_config['description']}")
    print(f"   Model File: {rf_config['model_file']}")
    print(f"   Image Path: {rf_config['image_path']}")
    print(f"   Scaler File: {rf_config['scaler_file']}")
    print(f"   Number of Fields: {len(rf_config['input_fields'])}")
    print(f"   Number of Output Classes: {len(rf_config['output_classes'])}")
else:
    print("   ❌ NOT FOUND!")
    print("   This is the problem! The model name doesn't exist in ML_CONFIGS")

# Test 3: Check all models
print("\n✅ TEST 3: All Models Summary")
for model_name, config in ML_CONFIGS.items():
    print(f"\n   📊 {model_name}")
    print(f"      Display: {config['display_name']}")
    print(f"      Fields: {len(config['input_fields'])}")
    print(f"      Classes: {len(config['output_classes'])}")
    print(f"      Has Scaler: {config['scaler_file'] is not None}")

# Test 4: Check FIELDS dictionary
print(f"\n✅ TEST 4: FIELDS Dictionary")
print(f"   Total fields defined: {len(FIELDS)}")
print(f"   Field names: {list(FIELDS.keys())[:10]}... (showing first 10)")

# Test 5: Check OUTPUT_CLASSES dictionary
print(f"\n✅ TEST 5: OUTPUT_CLASSES Dictionary")
print(f"   Total output types: {len(OUTPUT_CLASSES)}")
print(f"   Output types: {list(OUTPUT_CLASSES.keys())}")

# Test 6: Test get_model_config function
print(f"\n✅ TEST 6: Testing get_model_config Function")
from algoAI.utils import get_model_config

test_names = ['Random_Forest_classification', 'mushroom_classification', 'logistic_regression']
for test_name in test_names:
    config = get_model_config(test_name)
    if config:
        print(f"   ✅ {test_name}: FOUND")
    else:
        print(f"   ❌ {test_name}: NOT FOUND")

# Test 7: Check file structure
print(f"\n✅ TEST 7: File Structure")
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, 'models_ai')
static_dir = os.path.join(base_dir, 'algoAI', 'static')

print(f"   Base Directory: {base_dir}")
print(f"   Models Directory: {models_dir}")
print(f"   Models Dir Exists: {os.path.exists(models_dir)}")

if os.path.exists(models_dir):
    pkl_files = [f for f in os.listdir(models_dir) if f.endswith('.pkl')]
    print(f"   PKL files found: {pkl_files}")
    
    # Check if Random Forest files exist
    rf_model = 'RF_classification.pkl'
    rf_scaler = 'Scaler_RF_Regression.pkl'
    print(f"   {rf_model} exists: {rf_model in pkl_files}")
    print(f"   {rf_scaler} exists: {rf_scaler in pkl_files}")

print("\n" + "=" * 80)
print("🎯 DIAGNOSIS")
print("=" * 80)

# Diagnosis
if 'Random_Forest_classification' not in ML_CONFIGS:
    print("\n❌ PROBLEM FOUND: 'Random_Forest_classification' is NOT in ML_CONFIGS")
    print("   SOLUTION: Make sure your ml_configs.py has this model defined")
    print("   Check for typos in the model name!")
else:
    rf_config = ML_CONFIGS['Random_Forest_classification']
    
    # Check model file
    model_path = os.path.join(models_dir, rf_config['model_file'])
    if not os.path.exists(model_path):
        print(f"\n⚠️  WARNING: Model file not found: {rf_config['model_file']}")
        print(f"   Expected at: {model_path}")
        print("   SOLUTION: Make sure the .pkl file exists in models_ai/ folder")
    
    # Check scaler file
    if rf_config['scaler_file']:
        scaler_path = os.path.join(models_dir, rf_config['scaler_file'])
        if not os.path.exists(scaler_path):
            print(f"\n⚠️  WARNING: Scaler file not found: {rf_config['scaler_file']}")
            print(f"   Expected at: {scaler_path}")
            print("   SOLUTION: Make sure the scaler .pkl file exists or set scaler_file=None")
    
    # Check if all looks good
    if (os.path.exists(model_path) and 
        (not rf_config['scaler_file'] or os.path.exists(scaler_path))):
        print("\n✅ EVERYTHING LOOKS GOOD!")
        print("   The model should work correctly.")
        print("\n   If you're still getting redirected, try:")
        print("   1. Restart your Django server")
        print("   2. Clear your browser cache")
        print("   3. Check Django console for errors")

print("\n" + "=" * 80)