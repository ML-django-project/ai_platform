from django.shortcuts import render
import os
import joblib

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def regLog_details(request):
    return render(request, 'regLog_details.html')

def regLog_atelier(request):
    return render(request, 'regLog_atelier.html')

def regLog_tester(request):
    return render(request, 'vehicles_form.html')

def load_models(name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir,'models_ai' )
    model_path = os.path.join(models_dir, name)
    ml_model = joblib.load(model_path)
    return ml_model

def regLog_prediction(request):
    # Tâche 1: Recevoir le Colis
    if request.method == 'POST':

        # Tâche 2: Déballer le Colis
        hauteur = float(request.POST.get('hauteur'))
        nbr_roues = float(request.POST.get('Nombre_de_roues'))

        # Tâche 3: Réveiller l'Expert
        model = load_models('logistic_regression_sklearn.pkl')

        # Tâche 4: Poser la Question à l'Expert
        prediction = model.predict([[hauteur, nbr_roues]])
        predicted_class = prediction[0]

        # Tâche 5: Traduire la Réponse
        type_vehicules = {0: 'Camion', 1: 'Touristique'}
        img_url = {
            'Camion': 'images/camion.jpg',
            'Touristique': 'images/touristique.jpg'
        }

        pred_vehicule = type_vehicules[predicted_class]
        pred_img = img_url[pred_vehicule]

        # Tâche 6: Préparer le Plateau-Repas (context)
        context = {
            'type_vehicule': pred_vehicule,
            'img_vehicule': pred_img,
            'initial_data': {
                'hauteur': hauteur,
                'nbr_roues': nbr_roues
            }
        }
        return render(request, 'reglog_results.html', context)

    return render(request, 'vehicles_form.html')
