from django.urls import path
from model_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('tempTag/', views.tempTag, name='tempTag'),
    path('student/', views.student, name='student')
]