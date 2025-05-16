from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Assessment
from django.shortcuts import render, get_object_or_404
from .models import SoilAssessment

def assessment_result(request, assessment_id):
    assessment = get_object_or_404(SoilAssessment, pk=assessment_id)
    return render(request, 'assessment_result.html', {'assessment': assessment})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        ph = request.POST.get('ph')
        temperature = request.POST.get('temperature')
        moisture = request.POST.get('moisture')
        npk = request.POST.get('npk')
        Assessment.objects.create(
            user=request.user,
            soil_ph=ph,
            soil_temperature=temperature,
            soil_moisture=moisture,
            soil_npk=npk
        )
        return redirect('dashboard')
    return render(request, 'dashboard.html')


def new_assessment(request):
    return render(request, 'new_assessment.html')


def save_assessment(request):
    if request.method == 'POST':
        # Collect and process form data
        ph = request.POST['ph']
        moisture = request.POST['moisture']
        fertility = request.POST['fertility']
        farm_size = request.POST['farm_size']
        weather = request.POST['weather']

        # Save or process data as needed
        # Example: SoilAssessment.objects.create(...)

        return redirect('dashboard')  # or a results page

