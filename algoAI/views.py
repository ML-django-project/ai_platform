from django.shortcuts import render, redirect, get_object_or_404
from .models import Prediction, MLModel
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from .ml_configs import ML_CONFIGS
from .utils import (
    get_model_config, 
    prepare_input_features, 
    make_prediction,
    interpret_prediction,
    validate_model_files,
    get_model_info
)
import os
import joblib

# Create your views here.
def index(request):
    models = ML_CONFIGS
    return render(request, 'index.html', {'ml_models': models})

def about(request):
    return render(request, 'about.html')

def model_details(request, model_name):
    config = get_model_config(model_name)
    if not config:
        return redirect('index')
    return render(request, 'ml/model_details.html', {'config': config})

def model_atelier(request, model_name):
    config = get_model_config(model_name)
    if not config:
        return redirect('index')
    return render(request, 'ml/model_atelier.html', {'config': config})

def model_tester(request, model_name):
    #model input form
    config = get_model_config(model_name)
    if not config:
        return redirect('index')
    return render(request, 'ml/model_form.html', {'config': config})

def model_overview(request, model_name):
    config = get_model_config(model_name)
    if not config:
        print(f"DEBUG model_overview: config { model_name } not found")
        print(f"DEBUG model_overview: redirect to index")
        return redirect('index')
    
    print(f"config found for {model_name}")

    context = {
        'config': config,
        'model_name': model_name
    }
    
    return render(request, 'ml/model_overview.html', context)


def model_form(request, model_name):
    config = get_model_config(model_name)
    if not config:
        return redirect('index')
    return render(request, 'ml/model_form.html', {'config': config})



@login_required
def predictions_list(request, model_name=None):
    """List predictions, filtered by model"""
    predictions = Prediction.objects.filter(user=request.user)
    
    if model_name:
        ml_model = get_object_or_404(MLModel, name=model_name)
        predictions = predictions.filter(ml_model=ml_model)
        config = get_model_config(model_name)
    else:
        config = None
    
    context = {
        'predictions': predictions,
        'model_name': model_name,
        'config': config
    }
    
    return render(request, 'ml/predictions_list.html', context)

# Update your model_prediction function in views.py

@login_required
def model_prediction(request, model_name):
    """Processes the prediction for both classification and regression"""
    if request.method != 'POST':
        return redirect('model_form', model_name=model_name)
    
    config = get_model_config(model_name)
    if not config:
        return redirect('index')
    
    try:
        # Check if this is a regression model (all car price models are regression)
        is_regression = model_name in [
            'Random_Forest_regression', 
            'SVM_regression', 
            'regression_linaire', 
            'Decision_Tree_regression',
            'XGB_regression' 
        ]
        
        if is_regression:
            # Use special regression feature preparation
            from .utils import prepare_regression_features, make_regression_prediction, interpret_regression_prediction
            
            features, input_dict = prepare_regression_features(model_name, request.POST)
            predicted_value = make_regression_prediction(model_name, features)
            result = interpret_regression_prediction(model_name, predicted_value)
            
            # Save prediction
            ml_model_instance, _ = MLModel.objects.get_or_create(
                name=model_name,
                defaults={
                    'display_name': config['display_name'],
                    'description': config['description'],
                    'model_file': config['model_file'],
                    'image_path': config['image_path']
                }
            )
            
            Prediction.objects.create(
                user=request.user,
                ml_model=ml_model_instance,
                input_data=input_dict,
                prediction_result={
                    'value': float(predicted_value),
                    'label': result['label'],
                    'description': result.get('description', '')
                }
            )
            
            context = {
                'config': config,
                'result': result,
                'input_data': input_dict,
                'model_name': model_name,
                'predicted_value': predicted_value,
                'is_regression': True
            }
            
        else:
            # Standard classification handling
            features, input_dict = prepare_input_features(model_name, request.POST)
            predicted_class = make_prediction(model_name, features)
            result = interpret_prediction(model_name, predicted_class)
            
            ml_model_instance, _ = MLModel.objects.get_or_create(
                name=model_name,
                defaults={
                    'display_name': config['display_name'],
                    'description': config['description'],
                    'model_file': config['model_file'],
                    'image_path': config['image_path']
                }
            )
            
            Prediction.objects.create(
                user=request.user,
                ml_model=ml_model_instance,
                input_data=input_dict,
                prediction_result={
                    'class': int(predicted_class),
                    'label': result['label'],
                    'description': result.get('description', '')
                }
            )
            
            context = {
                'config': config,
                'result': result,
                'input_data': input_dict,
                'model_name': model_name,
                'predicted_class': predicted_class,
                'is_regression': False
            }
        
        return render(request, 'ml/prediction_result.html', context)
    
    except Exception as e:
        import traceback
        print(f"Error in prediction: {str(e)}")
        print(traceback.format_exc())
        return render(request, 'ml/error.html', {'error': str(e)})

@login_required
def dashboard(request):
    """Dashboard with user statistics"""
    
    # Get all user's predictions
    user_predictions = Prediction.objects.filter(user=request.user)
    
    # Total predictions count
    total_predictions = user_predictions.count()
    
    # Count by model
    predictions_by_model = user_predictions.values(
        'ml_model__display_name', 
        'ml_model__name'
    ).annotate(count=Count('id')).order_by('-count')
    
    # Most used model
    most_used_model = predictions_by_model.first() if predictions_by_model else None
    
    # Recent predictions (last 5)
    recent_predictions = user_predictions[:5]
    
    # Last prediction
    last_prediction = user_predictions.first() if user_predictions.exists() else None
    
    # Predictions this week
    week_ago = timezone.now() - timedelta(days=7)
    predictions_this_week = user_predictions.filter(created_at__gte=week_ago).count()
    
    # Predictions today
    today = timezone.now().date()
    predictions_today = user_predictions.filter(created_at__date=today).count()
    
    context = {
        'total_predictions': total_predictions,
        'predictions_by_model': predictions_by_model,
        'most_used_model': most_used_model,
        'recent_predictions': recent_predictions,
        'last_prediction': last_prediction,
        'predictions_this_week': predictions_this_week,
        'predictions_today': predictions_today,
    }
    
    return render(request, 'dashboard.html', context)



@login_required
def download_predictions_pdf(request, model_name=None):
    """Download predictions as PDF"""
    predictions = Prediction.objects.filter(user=request.user)
    
    if model_name:
        ml_model = get_object_or_404(MLModel, name=model_name)
        predictions = predictions.filter(ml_model=ml_model)
        filename = f"predictions_{model_name}_{request.user.username}.pdf"
        title = f"Historique des Prédictions - {ml_model.display_name}"
    else:
        filename = f"predictions_{request.user.username}.pdf"
        title = "Historique de Toutes les Prédictions"
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    title_para = Paragraph(f"{title} - {request.user.username}", title_style)
    elements.append(title_para)
    elements.append(Spacer(1, 0.3*inch))
    
    metadata = Paragraph(
        f"<b>Date de génération:</b> {timezone.now().strftime('%d/%m/%Y %H:%M')}<br/>"
        f"<b>Nombre total de prédictions:</b> {predictions.count()}",
        styles['Normal']
    )
    elements.append(metadata)
    elements.append(Spacer(1, 0.3*inch))
    
    # Table header
    data = [['ID', 'Modèle', 'Données Entrées', 'Résultat', 'Date']]
    
    for pred in predictions:
        input_str = ', '.join([f"{k}: {v}" for k, v in pred.input_data.items()])
        result_str = pred.prediction_result.get('label', 'N/A')
        
        data.append([
            str(pred.id),
            pred.ml_model.display_name,
            input_str,
            result_str,
            pred.created_at.strftime('%d/%m/%Y %H:%M')
        ])
    
    table = Table(data, colWidths=[0.6*inch, 1.5*inch, 2.5*inch, 1.5*inch, 1.5*inch])
    
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#343a40')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))
    
    footer = Paragraph(
        "© 2025-2026 AI Platform. Pr. Mohammed AMEKSA - All rights reserved.",
        styles['Normal']
    )
    elements.append(footer)
    
    doc.build(elements)
    return response