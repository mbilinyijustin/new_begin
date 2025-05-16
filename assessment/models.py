from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    soil_ph = models.DecimalField(max_digits=4, decimal_places=2)
    soil_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2)
    soil_npk = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
