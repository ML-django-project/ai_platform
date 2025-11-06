from django.db import models

# Create your models here.

class predHistory(models.Model):
    hauteur = models.FloatField()
    n_roues = models.IntegerField()
    pred_result = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"id : {self.id}"

