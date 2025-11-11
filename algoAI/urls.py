from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('regLog_details/', views.regLog_details, name='reglog_details'),
    path('regLog_atelier/', views.regLog_atelier, name="reglog_atelier"),
    path('reglog_tester/', views.regLog_tester, name='reglog_tester'),
    path('reglog_prediction', views.regLog_prediction, name='reglog_prediction'),
    path('preds/', views.preds_list, name='preds_list'),
    path('preds/download-pdf/', views.download_predictions_pdf, name='download_predictions_pdf'),
]