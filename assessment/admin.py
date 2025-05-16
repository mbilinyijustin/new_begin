from django.contrib import admin
from .models import Assessment
from django.contrib import admin
from .models import SoilAssessment

@admin.register(SoilAssessment)
class SoilAssessmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'ph', 'moisture', 'fertility', 'farm_size', 'weather', 'created_at']
    list_filter = ['weather', 'created_at']
    search_fields = ['user__username', 'fertility']

# Register your models here.
admin.site.register(Assessment)
