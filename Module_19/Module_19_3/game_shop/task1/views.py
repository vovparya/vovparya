from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game

def index(request):
    return render(request, 'index.html')

def shop(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'shop.html', context)

def cart(request):
    # Реализуйте логику корзины
    return render(request, 'cart.html')

def register(request):
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Получаем список существующих пользователей из базы данных
            existing_users = Buyer.objects.filter(name=username)

            # Проверки
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif existing_users.exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Создаём нового пользователя
                Buyer.objects.create(name=username, age=age, balance=0)
                return render(request, 'welcome.html', {'username': username})
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)
