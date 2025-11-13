from django.contrib import admin
from .models import predHistory, MLModel, Prediction

# Old model - keep registered
@admin.register(predHistory)
class PredHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'hauteur', 'n_roues', 'pred_result', 'created_at']
    list_filter = ['pred_result', 'created_at']
    search_fields = ['user__username']

# New models
@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'display_name']

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ml_model', 'get_result_label', 'created_at']
    list_filter = ['ml_model', 'created_at']
    search_fields = ['user__username']
    readonly_fields = ['input_data', 'prediction_result', 'created_at']
    
    def get_result_label(self, obj):
        return obj.prediction_result.get('label', 'N/A')
    get_result_label.short_description = 'Result'