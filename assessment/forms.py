from django import forms
from .models import SoilAssessment

class SoilAssessmentForm(forms.ModelForm):
    class Meta:
        model = SoilAssessment
        fields = ['ph', 'moisture', 'fertility', 'farm_size', 'weather']
        widgets = {
            'ph': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 6.5'}),
            'moisture': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 30.00'}),
            'fertility': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. N:20 P:30 K:40'}),
            'farm_size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2.5'}),
            'weather': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. sunny'}),
        }
