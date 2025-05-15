from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('', views.submit_soil_assessment, name='submit_soil_assessment'),
    path('success/', views.success, name='success'),
]
