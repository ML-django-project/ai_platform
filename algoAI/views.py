from django.shortcuts import render
from .models import predHistory
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import os
import joblib

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def regLog_details(request):
    return render(request, 'reglog/regLog_details.html')

def regLog_atelier(request):
    return render(request, 'reglog/regLog_atelier.html')

def regLog_tester(request):
    return render(request, 'reglog/vehicles_form.html')

def load_models(name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir,'models_ai' )
    model_path = os.path.join(models_dir, name)
    ml_model = joblib.load(model_path)
    return ml_model

@login_required
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

        # save prediction to database
        predHistory.objects.create(
            hauteur = hauteur,
            n_roues = nbr_roues,
            pred_result = predicted_class,
            user = request.user
        )

        # Tâche 6: Préparer le Plateau-Repas (context)
        context = {
            'type_vehicule': pred_vehicule,
            'img_vehicule': pred_img,
            'initial_data': {
                'hauteur': hauteur,
                'nbr_roues': nbr_roues
            }
        }
        return render(request, 'reglog/reglog_results.html', context)

    return render(request, 'reglog/vehicles_form.html')

@login_required
def preds_list(request):
    preds = predHistory.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'preds': preds,
    }
    return render(request, 'reglog/preds_list.html', context)

@login_required
def download_predictions_pdf(request):
    # Get user's predictions
    preds = predHistory.objects.filter(user=request.user).order_by('-created_at')
    
    # Create the HttpResponse object with PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="predictions_{request.user.username}.pdf"'
    
    # Create the PDF object
    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    # Add title
    title = Paragraph(f"Historique des Prédictions - {request.user.username}", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
    # Add metadata
    metadata = Paragraph(
        f"<b>Date de génération:</b> {timezone.now().strftime('%d/%m/%Y %H:%M')}<br/>"
        f"<b>Nombre total de prédictions:</b> {preds.count()}",
        styles['Normal']
    )
    elements.append(metadata)
    elements.append(Spacer(1, 0.3*inch))
    
    # Create table data
    data = [['ID', 'Hauteur (m)', 'Nombre de Roues', 'Type de Véhicule', 'Date de Création']]
    
    type_vehicules = {0: 'Camion', 1: 'Touristique'}
    
    for pred in preds:
        data.append([
            str(pred.id),
            str(pred.hauteur),
            str(int(pred.n_roues)),
            type_vehicules[pred.pred_result],
            pred.created_at.strftime('%d/%m/%Y %H:%M')
        ])
    
    # Create table
    table = Table(data, colWidths=[0.8*inch, 1.2*inch, 1.5*inch, 1.5*inch, 1.8*inch])
    
    # Add style to table
    table.setStyle(TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#343a40')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Body styling
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elements.append(table)
    
    # Add footer
    elements.append(Spacer(1, 0.5*inch))
    footer = Paragraph(
        "© 2025-2026 AI Platform. Pr. Mohammed AMEKSA - All rights reserved.",
        styles['Normal']
    )
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    return response