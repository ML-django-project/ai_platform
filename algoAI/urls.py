from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('regLog_details/', views.regLog_details, name='reglog_details'),
    path('regLog_atelier/', views.regLog_atelier, name="reglog_atelier"),
    path('reglog_tester/', views.regLog_tester, name='reglog_tester'),
    path('reglog_prediction', views.regLog_prediction, name='reglog_prediction'),
]