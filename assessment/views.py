from django.shortcuts import render, redirect
from .forms import SoilAssessmentForm
from .models import Assessment


def submit_soil_assessment(request):
    if request.method == 'POST':
        form = SoilAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # This line is important!
    else:
        form = SoilAssessmentForm()

    return render(request, 'submit_assessment.html', {'form': form})  # <-- This must be returned!


def success(request):
    return render(request, 'success.html')


def home(request):
    if request.method == 'POST':
        soil_type = request.POST.get('soil_type')
        moisture_level = request.POST.get('moisture_level')
        fertility = request.POST.get('fertility')
        farm_size = request.POST.get('farm_size')

        # Make sure all fields are present
        if all([soil_type, moisture_level, fertility, farm_size]):
            Assessment.objects.create(
                soil_type=soil_type,
                moisture_level=moisture_level,
                fertility=fertility,
                farm_size=farm_size
            )
            return redirect('success')

    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')
