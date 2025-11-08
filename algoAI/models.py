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

