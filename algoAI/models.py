from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class predHistory(models.Model):
    hauteur = models.FloatField()
    n_roues = models.IntegerField()
    pred_result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User:{self.user.username}, ID : {self.id}"
    
    class Meta:
        verbose_name = "Prediction History (Old)"
        verbose_name_plural = "Prediction Histories (Old)"

class MLModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=200)
    description = models.TextField()
    model_file = models.CharField(max_length=200)  # filename in models_ai folder
    scaler_file = models.CharField(max_length=200, blank=True, null=True)  # NEW: scaler filename
    image_path = models.CharField(max_length=200)  # path to card image
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # NEW: track updates
    
    def __str__(self):
        return self.display_name

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    input_data = models.JSONField()  # Store input features as JSON
    prediction_result = models.JSONField()  # Store prediction results as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.ml_model.name} - {self.id}"

