from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        path('dashboard/', views.dashboard, name='dashboard'),

    path('about/', views.about, name='about'),

    path('model/<str:model_name>/', views.model_overview, name='model_overview'),
    
    path('model/<str:model_name>/details/', views.model_details, name='model_details'),
    path('model/<str:model_name>/atelier/', views.model_atelier, name='model_atelier'),
    
    path('model/<str:model_name>/form/', views.model_form, name='model_form'),
    path('model/<str:model_name>/predict/', views.model_prediction, name='model_prediction'),
    
    path('predictions/', views.predictions_list, name='predictions_list'),
    path('predictions/<str:model_name>/', views.predictions_list, name='model_predictions_list'),
    path('predictions/download/', views.download_predictions_pdf, name='download_predictions_pdf'),
    path('predictions/<str:model_name>/download/', views.download_predictions_pdf, name='download_model_predictions_pdf'),
]