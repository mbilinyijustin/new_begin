from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'assessment'
urlpatterns = [
    path('create/', views.create_assessment, name='create'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-assessment/', views.new_assessment, name='new_assessment'),
    path('save-assessment/', views.save_assessment, name='save_assessment'),
    path('assessment/<int:assessment_id>/result/', views.assessment_result, name='assessment_result'),
    path('new/', views.new_soil_assessment, name='new_soil_assessment'),
    path('result/<int:pk>/', views.assessment_result, name='assessment_result'),  # You'll need this view too
]
