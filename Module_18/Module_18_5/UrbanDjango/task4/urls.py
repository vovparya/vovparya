from django.contrib import admin
from django.urls import path
from task4.views import index, shop, cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('index/', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]
