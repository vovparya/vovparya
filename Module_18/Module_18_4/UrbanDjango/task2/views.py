# task2/views.py

from django.shortcuts import render
from django.views import View  # Для классового представления


# Функциональное представление
def function_based_view(request):
    return render(request, 'second_task/function_view.html')


# Классовое представление
class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_view.html')
