from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import SoilAssessmentForm
from .models import Assessment
from .models import SoilAssessment


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password,
                                        confirm_password=confirm_password)
        login(request, user)  # Optional: log user in after registration
        return redirect('dashboard')  # Redirect to dashboard or home page

    return render(request, 'register.html')


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
