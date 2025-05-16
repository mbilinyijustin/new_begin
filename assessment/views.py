from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Assessment

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
