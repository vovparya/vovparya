from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    products = {
        'items': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'third_task/shop.html', products)


def cart(request):
    return render(request, 'third_task/cart.html')
