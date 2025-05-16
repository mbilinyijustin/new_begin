from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    soil_ph = models.DecimalField(max_digits=4, decimal_places=2)
    soil_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2)
    soil_npk = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class SoilAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    moisture = models.DecimalField(max_digits=5, decimal_places=2, help_text="Moisture in %")
    fertility = models.CharField(max_length=100, help_text="e.g. N:20 P:30 K:40")
    farm_size = models.DecimalField(max_digits=6, decimal_places=2, help_text="Farm size in acres")
    weather = models.CharField(max_length=100, help_text="e.g. sunny, rainy")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soil Assessment by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"