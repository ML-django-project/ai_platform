FIELDS = {
    ############ car price ##############################################################################################

    'Make': {
        'name': 'Make',
        'label': 'Car Make',
        'type': 'select',
        'options': [
            {'value': 'Audi', 'label': 'Audi'},
            {'value': 'BMW', 'label': 'BMW'},
            {'value': 'Ford', 'label': 'Ford'},
            {'value': 'Honda', 'label': 'Honda'},
            {'value': 'Toyota', 'label': 'Toyota'}
        ],
        'default': 'Honda'
    },
    
    # Car Model (will be one-hot encoded)
    'Model': {
        'name': 'Model',
        'label': 'Car Model',
        'type': 'select',
        'options': [
            {'value': 'Model A', 'label': 'Model A'},
            {'value': 'Model B', 'label': 'Model B'},
            {'value': 'Model C', 'label': 'Model C'},
            {'value': 'Model D', 'label': 'Model D'},
            {'value': 'Model E', 'label': 'Model E'}
        ],
        'default': 'Model B'
    },
    
    # Fuel Type (will be one-hot encoded)
    'Fuel_Type': {
        'name': 'Fuel_Type',
        'label': 'Fuel Type',
        'type': 'select',
        'options': [
            {'value': 'Diesel', 'label': 'Diesel'},
            {'value': 'Electric', 'label': 'Electric'},
            {'value': 'Petrol', 'label': 'Petrol'}
        ],
        'default': 'Petrol'
    },
    
    # Transmission (will be label encoded)
    'Transmission': {
        'name': 'Transmission',
        'label': 'Transmission',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'Automatic'},
            {'value': 1, 'label': 'Manual'}
        ],
        'default': 0
    },
    
    # Year
    'Year': {
        'name': 'Year',
        'label': 'Year',
        'type': 'number',
        'min': 2000,
        'max': 2025,
        'step': 1,
        'default': 2015
    },
    
    # Engine Size
    'Engine_Size': {
        'name': 'Engine_Size',
        'label': 'Engine Size (L)',
        'type': 'number',
        'min': 1.0,
        'max': 4.5,
        'step': 0.1,
        'default': 2.5
    },
    
    # Mileage
    'Mileage': {
        'name': 'Mileage',
        'label': 'Mileage (km)',
        'type': 'number',
        'min': 0,
        'max': 200000,
        'step': 1000,
        'default': 50000
    },
    ##################### Heart Disease Health fields #########################################################################
    'Age': {
        'name': 'Age',
        'label': 'Age (years)',
        'type': 'number',
        'min': 18,
        'max': 100,
        'step': 1,
        'default': 45
    },
    'Gender': {
        'name': 'Gender',
        'label': 'Gender',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'Female'},
            {'value': 1, 'label': 'Male'}
        ],
        'default': 0
    },
    'Weight': {
        'name': 'Weight',
        'label': 'Weight (kg)',
        'type': 'number',
        'min': 30,
        'max': 200,
        'step': 1,
        'default': 70
    },
    'Height': {
        'name': 'Height',
        'label': 'Height (cm)',
        'type': 'number',
        'min': 100,
        'max': 220,
        'step': 1,
        'default': 170
    },
    'BMI': {
        'name': 'BMI',
        'label': 'BMI (Body Mass Index)',
        'type': 'number',
        'min': 15,
        'max': 50,
        'step': 0.1,
        'default': 24.2
    },
    'Smoking': {
        'name': 'Smoking',
        'label': 'Smoking Status',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'Current Smoker'},
            {'value': 1, 'label': 'Former Smoker'},
            {'value': 2, 'label': 'Never Smoked'}
        ],
        'default': 2
    },
    'Alcohol_Intake': {
        'name': 'Alcohol_Intake',
        'label': 'Alcohol Intake',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'High'},
            {'value': 1, 'label': 'Low'},
            {'value': 2, 'label': 'Moderate'}
        ],
        'default': 1
    },
    'Physical_Activity': {
        'name': 'Physical_Activity',
        'label': 'Physical Activity Level',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'Active'},
            {'value': 1, 'label': 'Moderate'},
            {'value': 2, 'label': 'Sedentary'}
        ],
        'default': 1
    },
    'Diet': {
        'name': 'Diet',
        'label': 'Diet Quality',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'Average'},
            {'value': 1, 'label': 'Healthy'},
            {'value': 2, 'label': 'Unhealthy'}
        ],
        'default': 1
    },
    'Stress_Level': {
        'name': 'Stress_Level',
        'label': 'Stress Level',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'High'},
            {'value': 1, 'label': 'Low'},
            {'value': 2, 'label': 'Medium'}
        ],
        'default': 1
    },
    'Hypertension': {
        'name': 'Hypertension',
        'label': 'Hypertension',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'No'},
            {'value': 1, 'label': 'Yes'}
        ],
        'default': 0
    },
    'Diabetes': {
        'name': 'Diabetes',
        'label': 'Diabetes',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'No'},
            {'value': 1, 'label': 'Yes'}
        ],
        'default': 0
    },
    'Hyperlipidemia': {
        'name': 'Hyperlipidemia',
        'label': 'Hyperlipidemia (High Cholesterol)',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'No'},
            {'value': 1, 'label': 'Yes'}
        ],
        'default': 0
    },
    'Family_History': {
        'name': 'Family_History',
        'label': 'Family History of Heart Disease',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'No'},
            {'value': 1, 'label': 'Yes'}
        ],
        'default': 0
    },
    'Previous_Heart_Attack': {
        'name': 'Previous_Heart_Attack',
        'label': 'Previous Heart Attack',
        'type': 'select',
        'options': [
            {'value': 0, 'label': 'No'},
            {'value': 1, 'label': 'Yes'}
        ],
        'default': 0
    },
    'Systolic_BP': {
        'name': 'Systolic_BP',
        'label': 'Systolic Blood Pressure (mmHg)',
        'type': 'number',
        'min': 80,
        'max': 200,
        'step': 1,
        'default': 120
    },
    'Diastolic_BP': {
        'name': 'Diastolic_BP',
        'label': 'Diastolic Blood Pressure (mmHg)',
        'type': 'number',
        'min': 50,
        'max': 130,
        'step': 1,
        'default': 80
    },
    'Heart_Rate': {
        'name': 'Heart_Rate',
        'label': 'Heart Rate (bpm)',
        'type': 'number',
        'min': 40,
        'max': 150,
        'step': 1,
        'default': 72
    },
    'Blood_Sugar_Fasting': {
        'name': 'Blood_Sugar_Fasting',
        'label': 'Fasting Blood Sugar (mg/dL)',
        'type': 'number',
        'min': 60,
        'max': 300,
        'step': 1,
        'default': 95
    },
    'Cholesterol_Total': {
        'name': 'Cholesterol_Total',
        'label': 'Total Cholesterol (mg/dL)',
        'type': 'number',
        'min': 100,
        'max': 400,
        'step': 1,
        'default': 200
    }
}
############################################################################################################################
#######################################################################################################
#######################################################################################
OUTPUT_CLASSES = {
    'car_price': {
        0: {
        'label': 'Price Prediction',
        'image': 'images/car_price/car.jpg',
        'badge_class': 'bg-info',
        'description': 'Estimated car price based on features'
    }
    },
    'heart_risk': {
        0: {
            'label': 'LOW RISK',
            'image': 'images/logistic_regression/low_risk.jpeg',
            'badge_class': 'bg-success',
            'description': 'Low risk of heart disease. Maintain healthy lifestyle!'
        },
        1: {
            'label': 'MODERATE RISK',
            'image': 'images/logistic_regression/moderate_risk.jpeg',
            'badge_class': 'bg-warning',
            'description': 'Moderate risk of heart disease. Consider lifestyle improvements.'
        },
        2: {
            'label': 'HIGH RISK',
            'image': 'images/logistic_regression/high_risk.jpeg',
            'badge_class': 'bg-danger',
            'description': 'High risk of heart disease. Please consult a healthcare professional.'
        }
    }
}

#######################################################################################################
###################################################################################################
###########################################################################################



def create_model(name, display_name, description, model_file, image_path, 
                 field_keys, output_class_key, scaler_file=None, 
                 detail_pdf=None, demo_pdf=None, algorithm=None, task_type=None):
    return {
        'name': name,
        'display_name': display_name,
        'description': description,
        'model_file': model_file,
        'scaler_file': scaler_file,
        'image_path': image_path,
        'detail_pdf': detail_pdf,
        'demo_pdf': demo_pdf,
        'input_fields': [FIELDS[key] for key in field_keys],
        'output_classes': OUTPUT_CLASSES[output_class_key],
        'algorithm': algorithm, 
        'task_type': task_type
    }

ML_CONFIGS = {
    'regression_linaire': create_model(
        name='regression_linaire',
        display_name='Car Price Prediction - regression_linaire',
        description="Predict car prices using Random Forest algorithm",
        model_file='Linear_Regression.pkl',
        image_path='images/regression_linaire.png',
        field_keys=['Make', 'Model', 'Fuel_Type', 'Transmission', 'Year', 'Engine_Size', 'Mileage'],
        output_class_key='car_price',
        scaler_file=None,
        detail_pdf='pdfs/random_forest_regression_guide.pdf',
        demo_pdf='pdfs/random_forest_regression_demo.pdf',
    ),
    #SVM regression
    'SVM_regression': create_model(
        name='SVM_regression',
        display_name='Car Price Prediction - SVM Regression',
        description="Predict car prices using Random Forest algorithm",
        model_file='RF_Regression.pkl',
        image_path='images/SVM.png',
        field_keys=['Make', 'Model', 'Fuel_Type', 'Transmission', 'Year', 'Engine_Size', 'Mileage'],
        output_class_key='car_price',
        scaler_file='Scaler_RF_Regression.pkl',
        detail_pdf='pdfs/Supervised_learning_classification_guide.pdf',
        demo_pdf='pdfs/random_forest_regression_demo.pdf',
    ),
    # SVM clasification
    'SVM_classification': create_model(
        name='SVM_classification',
        display_name='Heart Disease Risk Prediction - SVM classification',
        description="Machine learning model to predict heart disease risk",
        model_file='svm_clas_reduced_features.pkl',
        image_path='images/SVM.png',
        field_keys=[
            'Age', 'Gender', 'Stress_Level',
            'Hypertension', 'Diabetes', 'Hyperlipidemia', 'Family_History',
            'Previous_Heart_Attack', 'Diastolic_BP', 'Cholesterol_Total'
        ],
        output_class_key='heart_risk',
        scaler_file= 'scaler_svm_reduced_features.pkl',
        detail_pdf= 'pdfs/Supervised_learning_classification_guide.pdf',
        demo_pdf=  'pdfs/svm_classification_demo.pdf',
    ),
     #XGB regression
    'XGB_regression': create_model(
        name='XGB_regression',
        display_name='Car Price Prediction - XGB Regression',
        description="Predict car prices using eXtreme Gradient Boosting Regression.",
        model_file='RF_Regression.pkl',
        image_path='images/XGB_image.png',
        field_keys=['Make', 'Model', 'Fuel_Type', 'Transmission', 'Year', 'Engine_Size', 'Mileage'],
        output_class_key='car_price',
        scaler_file='Scaler_RF_Regression.pkl',
        detail_pdf='pdfs/Supervised_learning_classification_guide.pdf',
        demo_pdf='pdfs/random_forest_regression_demo.pdf',
    ),
    # XGB clasification
    'XGB_classification': create_model(
        name='XGB_classification',
        display_name='Heart Disease Risk Prediction - XGB classification',
        description="Predict heart disease risk using eXtreme Gradient Boosting Regression ",
        model_file='xgboost_with_scaler.pkl',
        image_path='images/XGB_image.png',
        field_keys=[
            'Hypertension', 'Cholesterol_Total', 'Diabetes', 'Age', 'Previous_Heart_Attack', 'Systolic_BP', 'Heart_Rate', 'Diastolic_BP'
        ],
        output_class_key='heart_risk',
        scaler_file= 'xgboost_with_scaler.pkl',
        detail_pdf= 'pdfs/Xgboost_cours.pdf',
        demo_pdf=  'pdfs/xgboost_demo_cla.pdf',
    ),
    
    
    # Car Price - Random Forest Regression

    'Random_Forest_regression': create_model(
        name='Random_Forest_regression',
        display_name='Car Price Prediction - Random Forest Regression',
        description="Predict car prices using Random Forest algorithm",
        model_file='RF_Regression.pkl',
        image_path='images/random_forest.png',
        field_keys=['Make', 'Model', 'Fuel_Type', 'Transmission', 'Year', 'Engine_Size', 'Mileage'],
        output_class_key='car_price',
        scaler_file='Scaler_RF_Regression.pkl',
        detail_pdf='pdfs/random_forest_regression_guide.pdf',
        demo_pdf='pdfs/random_forest_regression_demo.pdf',
    ),
    
    # Random Forest - classification
    'Random_Forest_classification': create_model(
        name='Random_Forest_classification',
        display_name='Heart Disease Risk Prediction - Random Forest Classification',
        description="Machine learning model to predict heart disease risk",
        model_file='RF_classification.pkl',
        image_path='images/random_forest.png',
        field_keys=[
            'Cholesterol_Total', 'Age', 'Hypertension', 'Diabetes', 'Previous_Heart_Attack', 'BMI', 'Diastolic_BP', 'Heart_Rate', 'Weight'
        ],
        output_class_key='heart_risk',
        scaler_file=None,
        detail_pdf= 'pdfs/logistic_regresssion_guide.pdf',
        demo_pdf=  'pdfs/logistic_regresssion_demo.pdf',
    ),
    # Heart Disease - Logistic Regression
    'logistic_regression': create_model(
        name='logistic_regression',
        display_name='Heart Disease Risk Prediction - Logistic Regression',
        description="Machine learning model to predict heart disease risk",
        model_file='LogisticRegression.pkl',
        image_path='images/logistic_regression/logistic_regresion_image.jpeg',
        field_keys=[
            'Age', 'Gender', 'Weight', 'Height', 'BMI', 'Smoking',
            'Alcohol_Intake', 'Physical_Activity', 'Diet', 'Stress_Level',
            'Hypertension', 'Diabetes', 'Hyperlipidemia', 'Family_History',
            'Previous_Heart_Attack', 'Systolic_BP', 'Diastolic_BP',
            'Heart_Rate', 'Blood_Sugar_Fasting', 'Cholesterol_Total'
        ],
        output_class_key='heart_risk',
        scaler_file='ScalerLogisticRegression.pkl',
        detail_pdf= 'pdfs/logistic_regresssion_guide.pdf',
        demo_pdf=  'pdfs/logistic_regresssion_demo.pdf',
    ),
    # Decision Tree regression
    'Decision_Tree_regression': create_model(
        name='Decision_Tree_regression',
        display_name='Heart Disease Risk Prediction - Decision Tree regression',
        description="Machine learning model to predict heart disease risk",
        model_file='Decision_Tree_Regression.pkl',
        image_path='images/dession_tree_images.png',
        field_keys=['Make', 'Model', 'Fuel_Type', 'Transmission', 'Year', 'Engine_Size', 'Mileage'],
        output_class_key='heart_risk',
        scaler_file=None,
        detail_pdf= 'pdfs/logistic_regresssion_guide.pdf',
        demo_pdf=  'pdfs/logistic_regresssion_demo.pdf',
    ),
    # Decision Tree clasification
    'Decision_Tree_clasification': create_model(
        name='Decision_Tree_clasification',
        display_name='Heart Disease Risk Prediction - Decision Tree clasification',
        description="Machine learning model to predict heart disease risk",
        model_file='Decision_Tree_classification.pkl',
        image_path='images/dession_tree_images.png',
        field_keys=[
            'Cholesterol_Total', 'Hypertension', 'Diabetes', 'Age',
            'Previous_Heart_Attack'
        ],
        output_class_key='heart_risk',
        scaler_file='Scaler_Decision_Tree_classification.pkl',
        detail_pdf= 'pdfs/logistic_regresssion_guide.pdf',
        demo_pdf=  'pdfs/logistic_regresssion_demo.pdf',
    ),
}


####################################################################################################
############################################################################################################
##################################################################################################
