from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_form, name='candidate_form'),
    path('success/', views.success, name='success'),
]