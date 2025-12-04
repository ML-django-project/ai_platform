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
    """Download predictions as PDF - Compact version with key fields only"""
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
    
    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        wordWrap='CJK'
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
    
    # Define key fields to show based on model type
    def format_input_compact(input_data):
        """Show only the most important 3-4 fields"""
        key_fields = []
        
        # For car price models
        if 'Make' in input_data:
            key_fields = [
                f"{input_data.get('Make', '')} {input_data.get('Model', '')}",
                f"{input_data.get('Year', '')}",
                f"{input_data.get('Mileage', '')} km"
            ]
        # For heart disease models
        elif 'Age' in input_data:
            key_fields = [
                f"Age: {input_data.get('Age', '')}",
                f"BP: {input_data.get('Systolic_BP', '')}/{input_data.get('Diastolic_BP', '')}",
                f"Chol: {input_data.get('Cholesterol_Total', '')}"
            ]
        else:
            # Generic fallback - show first 3 items
            items = list(input_data.items())[:3]
            key_fields = [f"{k}: {v}" for k, v in items]
        
        return ', '.join(key_fields)
    
    # Table header
    data = [['ID', 'Modèle', 'Principales Données', 'Résultat', 'Date']]
    
    for pred in predictions:
        # Format input data compactly
        input_str = format_input_compact(pred.input_data)
        input_para = Paragraph(input_str, cell_style)
        
        # Format result
        result_str = pred.prediction_result.get('label', 'N/A')
        
        # Format model name
        model_name_short = pred.ml_model.display_name
        if len(model_name_short) > 30:
            model_name_short = model_name_short[:27] + "..."
        model_para = Paragraph(model_name_short, cell_style)
        
        data.append([
            str(pred.id),
            model_para,
            input_para,
            result_str,
            pred.created_at.strftime('%d/%m/%Y\n%H:%M')
        ])
    
    # Balanced column widths
    table = Table(data, colWidths=[0.4*inch, 1.8*inch, 2.8*inch, 1.3*inch, 0.9*inch])
    
    table.setStyle(TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#343a40')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Body styling
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center ID
        ('ALIGN', (1, 1), (-2, -1), 'LEFT'),    # Left align text columns
        ('ALIGN', (-1, 1), (-1, -1), 'CENTER'), # Center date
        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        
        # Padding
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Add note about data
    note = Paragraph(
        "<i>Note: Seules les principales données sont affichées dans ce rapport. "
        "Pour voir tous les détails, consultez l'historique en ligne.</i>",
        ParagraphStyle('Note', parent=styles['Normal'], fontSize=8, textColor=colors.grey)
    )
    elements.append(note)
    elements.append(Spacer(1, 0.2*inch))
    
    footer = Paragraph(
        "© 2025-2026 AI Platform. Pr. Mohammed AMEKSA - All rights reserved.",
        styles['Normal']
    )
    elements.append(footer)
    
    doc.build(elements)
    return response