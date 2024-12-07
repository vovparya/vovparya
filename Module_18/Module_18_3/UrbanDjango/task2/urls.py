# task2/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.function_based_view, name='function_view'),
    path('class/', views.ClassBasedView.as_view(), name='class_view'),
]
