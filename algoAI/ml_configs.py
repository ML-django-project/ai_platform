
ML_CONFIGS = {
    'logistic_regression': {
        'name': 'logistic_regression',
        'display_name': 'Régression Logistique',
        'description': "Algorithme d'apprentissage supervisé de classification",
        'model_file': 'logistic_regression_sklearn.pkl',
        'scaler_file' : None,
        'image_path': 'images/regression_logistique.jpg',
        'detail_pdf': 'pdfs/chapitre5.pdf',
        'demo_pdf': 'pdfs/course_demonstration.pdf',
        'input_fields': [
            {
                'name': 'hauteur',
                'label': 'Hauteur (m)',
                'type': 'range',
                'min': 2,
                'max': 5.5,
                'step': 0.1,
                'default': 3
            },
            {
                'name': 'n_roues',
                'label': 'Nombre de roues',
                'type': 'range',
                'min': 4,
                'max': 18,
                'step': 2,
                'default': 4
            }
        ],
        'output_classes': {
            0: {
                'label': 'Camion',
                'image': 'images/camion.jpg',
                'badge_class': 'bg-primary'
            },
            1: {
                'label': 'Touristique',
                'image': 'images/touristique.jpg',
                'badge_class': 'bg-success'
            }
        }
    },
#************************************************************************************************************
    'decision_tree': {
        'name': 'decision_tree',
        'display_name': 'Decision Tree',
        'description': "Algorithme d'apprentissage supervisé de classification",
        'model_file': 'decision_tree.pkl',
        'scaler_file' : None,
        'image_path': 'images/regression_logistique.jpg',
        'detail_pdf': 'pdfs/chapitre5.pdf',
        'demo_pdf': 'pdfs/course_demonstration.pdf',
        'input_fields': [
            {
                'name': 'sepal_length',
                'label': 'sepal length (cm)',
                'type': 'range',
                'min': 2,
                'max': 5.5,
                'step': 0.1,
                'default': 3
            },
            {
                'name': 'sepal_width',
                'label': 'sepal width (cm)',
                'type': 'range',
                'min': 4,
                'max': 18,
                'step': 2,
                'default': 4
            }
        ],
        'output_classes': {
            0: {
                'label': 'setosa',
                'image': 'images/camion.jpg',
                'badge_class': 'bg-primary'
            },
            1: {
                'label': 'versicolor',
                'image': 'images/touristique.jpg',
                'badge_class': 'bg-success'
            },
            2: {
                'label': 'versicolor',
                'image': 'images/touristique.jpg',
                'badge_class': 'bg-success'
            }
        }
    },
#**********************************************************************************************
        #edible=e, poisonous=p
    'mushroom_classification': {
        'name': 'mushroom_classification',
        'display_name': 'Classification des Champignons',
        'description': "Algorithme de classification pour identifier les champignons comestibles ou vénéneux basé sur l'ensemble de données UCI Mushroom",
        'model_file': 'mushroom_classifier.pkl',
        'scaler_file' : None,
        'image_path': 'images/mushrooms/mushroom.jpg',
        'detail_pdf': 'pdfs/Mushroom_Classification.pdf',
        'demo_pdf': 'pdfs/Mushroom_Classification.pdf',
        'input_fields': [
            {
                'name': 'cap_shape',
                'label': 'Forme du chapeau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Cloche (bell=b)'},
                    {'value': 1, 'label': 'Conique (conical=c)'},
                    {'value': 2, 'label': 'Convexe (convex=x)'},
                    {'value': 3, 'label': 'Plat (flat=f)'},
                    {'value': 4, 'label': 'Bossu (knobbed=k)'},
                    {'value': 5, 'label': 'Enfoncé (sunken=s)'}
                ],
                'default': 2
            },
            {
                'name': 'cap_surface',
                'label': 'Surface du chapeau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Fibreux (fibrous=f)'},
                    {'value': 1, 'label': 'Rainuré (grooves=g)'},
                    {'value': 2, 'label': 'Écaillé (scaly=y)'},
                    {'value': 3, 'label': 'Lisse (smooth=s)'}
                ],
                'default': 0
            },
            {
                'name': 'cap_color',
                'label': 'Couleur du chapeau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Marron (brown=n)'},
                    {'value': 1, 'label': 'Beige (buff=b)'},
                    {'value': 2, 'label': 'Cannelle (cinnamon=c)'},
                    {'value': 3, 'label': 'Gris (gray=g)'},
                    {'value': 4, 'label': 'Vert (green=r)'},
                    {'value': 5, 'label': 'Rose (pink=p)'},
                    {'value': 6, 'label': 'Violet (purple=u)'},
                    {'value': 7, 'label': 'Rouge (red=e)'},
                    {'value': 8, 'label': 'Blanc (white=w)'},
                    {'value': 9, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 0
            },
            {
                'name': 'bruises',
                'label': 'Meurtrissures',
                'type': 'radio',
                'options': [
                    {'value': 0, 'label': 'Présence de meurtrissures (bruises=t)'},
                    {'value': 1, 'label': 'Pas de meurtrissures (no=f)'}
                ],
                'default': 1
            },
            {
                'name': 'odor',
                'label': 'Odeur',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Amande (almond=a)'},
                    {'value': 1, 'label': 'Anis (anise=l)'},
                    {'value': 2, 'label': 'Créosote (creosote=c)'},
                    {'value': 3, 'label': 'Poisson (fishy=y)'},
                    {'value': 4, 'label': 'Fétide (foul=f)'},
                    {'value': 5, 'label': 'Moisi (musty=m)'},
                    {'value': 6, 'label': 'Aucune odeur (none=n)'},
                    {'value': 7, 'label': 'Piquant (pungent=p)'},
                    {'value': 8, 'label': 'Épicé (spicy=s)'}
                ],
                'default': 6
            },
            {
                'name': 'gill_attachment',
                'label': 'Attache des lamelles',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Attaché (attached=a)'},
                    {'value': 1, 'label': 'Descendant (descending=d)'},
                    {'value': 2, 'label': 'Libre (free=f)'},
                    {'value': 3, 'label': 'Entaillé (notched=n)'}
                ],
                'default': 2
            },
            {
                'name': 'gill_spacing',
                'label': 'Espacement des lamelles',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Serré (close=c)'},
                    {'value': 1, 'label': 'En grappe (crowded=w)'},
                    {'value': 2, 'label': 'Distant (distant=d)'}
                ],
                'default': 1
            },
            {
                'name': 'gill_size',
                'label': 'Taille des lamelles',
                'type': 'radio',
                'options': [
                    {'value': 0, 'label': 'Larges (broad=b)'},
                    {'value': 1, 'label': 'Étroites (narrow=n)'}
                ],
                'default': 0
            },
            {
                'name': 'gill_color',
                'label': 'Couleur des lamelles',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Noir (black=k)'},
                    {'value': 1, 'label': 'Marron (brown=n)'},
                    {'value': 2, 'label': 'Beige (buff=b)'},
                    {'value': 3, 'label': 'Chocolat (chocolate=h)'},
                    {'value': 4, 'label': 'Gris (gray=g)'},
                    {'value': 5, 'label': 'Vert (green=r)'},
                    {'value': 6, 'label': 'Orange (orange=o)'},
                    {'value': 7, 'label': 'Rose (pink=p)'},
                    {'value': 8, 'label': 'Violet (purple=u)'},
                    {'value': 9, 'label': 'Rouge (red=e)'},
                    {'value': 10, 'label': 'Blanc (white=w)'},
                    {'value': 11, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 10
            },
            {
                'name': 'stalk_shape',
                'label': 'Forme du pied',
                'type': 'radio',
                'options': [
                    {'value': 0, 'label': 'Évasé (enlarging=e)'},
                    {'value': 1, 'label': 'Effilé (tapering=t)'}
                ],
                'default': 0
            },
            {
                'name': 'stalk_root',
                'label': 'Racine du pied',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Bulbeux (bulbous=b)'},
                    {'value': 1, 'label': 'En massue (club=c)'},
                    {'value': 2, 'label': 'En coupe (cup=u)'},
                    {'value': 3, 'label': 'Égal (equal=e)'},
                    {'value': 4, 'label': 'Rhizomorphe (rhizomorphs=z)'},
                    {'value': 5, 'label': 'Racinaire (rooted=r)'},
                    {'value': 6, 'label': 'Manquant (missing=?)'}
                ],
                'default': 6
            },
            {
                'name': 'stalk_surface_above_ring',
                'label': 'Surface du pied au-dessus de l anneau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Fibreux (fibrous=f)'},
                    {'value': 1, 'label': 'Écaillé (scaly=y)'},
                    {'value': 2, 'label': 'Soyeux (silky=k)'},
                    {'value': 3, 'label': 'Lisse (smooth=s)'}
                ],
                'default': 0
            },
            {
                'name': 'stalk_surface_below_ring',
                'label': 'Surface du pied en-dessous de l anneau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Fibreux (fibrous=f)'},
                    {'value': 1, 'label': 'Écaillé (scaly=y)'},
                    {'value': 2, 'label': 'Soyeux (silky=k)'},
                    {'value': 3, 'label': 'Lisse (smooth=s)'}
                ],
                'default': 0
            },
            {
                'name': 'stalk_color_above_ring',
                'label': 'Couleur du pied au-dessus de l anneau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Marron (brown=n)'},
                    {'value': 1, 'label': 'Beige (buff=b)'},
                    {'value': 2, 'label': 'Cannelle (cinnamon=c)'},
                    {'value': 3, 'label': 'Gris (gray=g)'},
                    {'value': 4, 'label': 'Orange (orange=o)'},
                    {'value': 5, 'label': 'Rose (pink=p)'},
                    {'value': 6, 'label': 'Rouge (red=e)'},
                    {'value': 7, 'label': 'Blanc (white=w)'},
                    {'value': 8, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 7
            },
            {
                'name': 'stalk_color_below_ring',
                'label': 'Couleur du pied en-dessous de l anneau',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Marron (brown=n)'},
                    {'value': 1, 'label': 'Beige (buff=b)'},
                    {'value': 2, 'label': 'Cannelle (cinnamon=c)'},
                    {'value': 3, 'label': 'Gris (gray=g)'},
                    {'value': 4, 'label': 'Orange (orange=o)'},
                    {'value': 5, 'label': 'Rose (pink=p)'},
                    {'value': 6, 'label': 'Rouge (red=e)'},
                    {'value': 7, 'label': 'Blanc (white=w)'},
                    {'value': 8, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 7
            },
            {
                'name': 'veil_type',
                'label': 'Type de voile',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Partiel (partial=p)'},
                    {'value': 1, 'label': 'Universel (universal=u)'}
                ],
                'default': 0
            },
            {
                'name': 'veil_color',
                'label': 'Couleur du voile',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Marron (brown=n)'},
                    {'value': 1, 'label': 'Orange (orange=o)'},
                    {'value': 2, 'label': 'Blanc (white=w)'},
                    {'value': 3, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 2
            },
            {
                'name': 'ring_number',
                'label': "Nombre d'anneaux",
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Aucun (none=n)'},
                    {'value': 1, 'label': 'Un (one=o)'},
                    {'value': 2, 'label': 'Deux (two=t)'}
                ],
                'default': 1
            },
            {
                'name': 'ring_type',
                'label': "Type d'anneau",
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Arachnéen (cobwebby=c)'},
                    {'value': 1, 'label': 'Évanescent (evanescent=e)'},
                    {'value': 2, 'label': 'Évasé (flaring=f)'},
                    {'value': 3, 'label': 'Large (large=l)'},
                    {'value': 4, 'label': 'Aucun (none=n)'},
                    {'value': 5, 'label': 'Pendant (pendant=p)'},
                    {'value': 6, 'label': 'Gainé (sheathing=s)'},
                    {'value': 7, 'label': 'Zoné (zone=z)'}
                ],
                'default': 1
            },
            {
                'name': 'spore_print_color',
                'label': 'Couleur des spores',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Noir (black=k)'},
                    {'value': 1, 'label': 'Marron (brown=n)'},
                    {'value': 2, 'label': 'Beige (buff=b)'},
                    {'value': 3, 'label': 'Chocolat (chocolate=h)'},
                    {'value': 4, 'label': 'Vert (green=r)'},
                    {'value': 5, 'label': 'Orange (orange=o)'},
                    {'value': 6, 'label': 'Violet (purple=u)'},
                    {'value': 7, 'label': 'Blanc (white=w)'},
                    {'value': 8, 'label': 'Jaune (yellow=y)'}
                ],
                'default': 1
            },
            {
                'name': 'population',
                'label': 'Population',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Abondante (abundant=a)'},
                    {'value': 1, 'label': 'En grappe (clustered=c)'},
                    {'value': 2, 'label': 'Nombreuse (numerous=n)'},
                    {'value': 3, 'label': 'Éparpillée (scattered=s)'},
                    {'value': 4, 'label': 'Plusieurs (several=v)'},
                    {'value': 5, 'label': 'Solitaire (solitary=y)'}
                ],
                'default': 4
            },
            {
                'name': 'habitat',
                'label': 'Habitat',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Herbes (grasses=g)'},
                    {'value': 1, 'label': 'Feuilles (leaves=l)'},
                    {'value': 2, 'label': 'Prairies (meadows=m)'},
                    {'value': 3, 'label': 'Sentiers (paths=p)'},
                    {'value': 4, 'label': 'Urbain (urban=u)'},
                    {'value': 5, 'label': 'Déchets (waste=w)'},
                    {'value': 6, 'label': 'Bois (woods=d)'}
                ],
                'default': 6
            }
        ],
        'output_classes': {
            0: {
                'label': 'COMESTIBLE (edible=e)',
                'image': 'images/mushrooms/edible_mushroom.jpg',
                'badge_class': 'bg-success',
                'description': 'Ce champignon est comestible - Bon appétit!'
            },
            1: {
                'label': 'VÉNÉNEUX (poisonous=p)',
                'image': 'images/mushrooms/poisonous_mushroom.jpg', 
                'badge_class': 'bg-danger',
                'description': 'ATTENTION: Ce champignon est vénéneux! Ne pas consommer.'
            }
        }
    },
#******************************************************************************
    'heart_disease': {
        'name': 'heart_disease',
        'display_name': 'Heart Disease Risk Prediction',
        'description': "Machine learning model to predict heart disease risk based on health parameters and lifestyle factors",
        'model_file': 'LogisticRegression.pkl',
        'scaler_file' : 'ScalerLogisticRegression.pkl',
        'image_path': 'images/heart_disease.jpg',
        'detail_pdf': 'pdfs/heart_disease_guide.pdf',
        'demo_pdf': 'pdfs/heart_disease_demo.pdf',
        'input_fields': [
            {
                'name': 'Age',
                'label': 'Age (years)',
                'type': 'number',
                'min': 18,
                'max': 100,
                'step': 1,
                'default': 45
            },
            {
                'name': 'Gender',
                'label': 'Gender',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'Female'},
                    {'value': 1, 'label': 'Male'}
                ],
                'default': 0
            },
            {
                'name': 'Weight',
                'label': 'Weight (kg)',
                'type': 'number',
                'min': 30,
                'max': 200,
                'step': 1,
                'default': 70
            },
            {
                'name': 'Height',
                'label': 'Height (cm)',
                'type': 'number',
                'min': 100,
                'max': 220,
                'step': 1,
                'default': 170
            },
            {
                'name': 'BMI',
                'label': 'BMI (Body Mass Index)',
                'type': 'number',
                'min': 15,
                'max': 50,
                'step': 0.1,
                'default': 24.2
            },
            {
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
            {
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
            {
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
            {
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
            {
                'name': 'Hypertension',
                'label': 'Hypertension',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'No'},
                    {'value': 1, 'label': 'Yes'}
                ],
                'default': 0
            },
            {
                'name': 'Diabetes',
                'label': 'Diabetes',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'No'},
                    {'value': 1, 'label': 'Yes'}
                ],
                'default': 0
            },
            {
                'name': 'Hyperlipidemia',
                'label': 'Hyperlipidemia (High Cholesterol)',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'No'},
                    {'value': 1, 'label': 'Yes'}
                ],
                'default': 0
            },
            {
                'name': 'Family_History',
                'label': 'Family History of Heart Disease',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'No'},
                    {'value': 1, 'label': 'Yes'}
                ],
                'default': 0
            },
            {
                'name': 'Previous_Heart_Attack',
                'label': 'Previous Heart Attack',
                'type': 'select',
                'options': [
                    {'value': 0, 'label': 'No'},
                    {'value': 1, 'label': 'Yes'}
                ],
                'default': 0
            },
            {
                'name': 'Systolic_BP',
                'label': 'Systolic Blood Pressure (mmHg)',
                'type': 'number',
                'min': 80,
                'max': 200,
                'step': 1,
                'default': 120
            },
            {
                'name': 'Diastolic_BP',
                'label': 'Diastolic Blood Pressure (mmHg)',
                'type': 'number',
                'min': 50,
                'max': 130,
                'step': 1,
                'default': 80
            },
            {
                'name': 'Heart_Rate',
                'label': 'Heart Rate (bpm)',
                'type': 'number',
                'min': 40,
                'max': 150,
                'step': 1,
                'default': 72
            },
            {
                'name': 'Blood_Sugar_Fasting',
                'label': 'Fasting Blood Sugar (mg/dL)',
                'type': 'number',
                'min': 60,
                'max': 300,
                'step': 1,
                'default': 95
            },
            {
                'name': 'Cholesterol_Total',
                'label': 'Total Cholesterol (mg/dL)',
                'type': 'number',
                'min': 100,
                'max': 400,
                'step': 1,
                'default': 200
            }
        ],
        'output_classes': {
            0: {
                'label': '🟢 LOW RISK',
                'image': 'images/low_risk_heart.jpg',
                'badge_class': 'bg-success',
                'description': 'Low risk of heart disease. Maintain healthy lifestyle!'
            },
            1: {
                'label': '🟡 MODERATE RISK',
                'image': 'images/moderate_risk_heart.jpg',
                'badge_class': 'bg-warning',
                'description': 'Moderate risk of heart disease. Consider lifestyle improvements.'
            },
            2: {
                'label': '🔴 HIGH RISK',
                'image': 'images/high_risk_heart.jpg',
                'badge_class': 'bg-danger',
                'description': 'High risk of heart disease. Please consult a healthcare professional.'
            }
        }
    }
}