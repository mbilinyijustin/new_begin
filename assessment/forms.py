from django import forms
from .models import SoilAssessment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SoilAssessmentForm
class SoilAssessmentForm(forms.ModelForm):
    class Meta:
        model = SoilAssessment
        fields = ['farmer_name', 'soil_nutrient_npk', 'soil_moisture', 'soil_ph', 'soil_temperature']
        widgets = {
            'farmer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'soil_nutrient_npk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10-20-10'}),
            'soil_moisture': forms.NumberInput(attrs={'class': 'form-control'}),
            'soil_ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'soil_temperature': forms.NumberInput(attrs={'class': 'form-control'}),
        }

@login_required
def new_soil_assessment(request):
    if request.method == 'POST':
        form = SoilAssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.user = request.user
            assessment.save()
            return redirect('assessment_result', pk=assessment.pk)
    else:
        form = SoilAssessmentForm()
    return render(request, 'assessment/new_assessment.html', {'form': form})
