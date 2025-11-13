
ML_CONFIGS = {
    'logistic_regression': {
        'name': 'logistic_regression',
        'display_name': 'Régression Logistique',
        'description': "Algorithme d'apprentissage supervisé de classification",
        'model_file': 'logistic_regression_sklearn.pkl',
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
    }
}