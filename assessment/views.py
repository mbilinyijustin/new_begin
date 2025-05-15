from django.shortcuts import render, redirect
from .forms import SoilAssessmentForm

def submit_soil_assessment(request):
    if request.method == 'POST':
        form = SoilAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # This line is important!
    else:
        form = SoilAssessmentForm()

    return render(request, 'submit_assessment.html', {'form': form})  # <-- This must be returned!
