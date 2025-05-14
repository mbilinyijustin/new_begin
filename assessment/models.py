from django.db import models

# Create your models here.
class SoilAssessment(models.Model):
    farmer_name = models.CharField(max_length=100)
    soil_nutrient_npk = models.CharField(max_length=100)
    soil_moisture = models.FloatField(help_text="Percentage (%)")
    soil_ph = models.FloatField()
    soil_temperature = models.FloatField(help_text="Temperature in °C")
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_name} - {self.submission_date.strftime('%Y-%m-%d')}"

