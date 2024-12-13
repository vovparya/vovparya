from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название игры')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    size = models.IntegerField(verbose_name='Размер (МБ)')

    def __str__(self):
        return self.title


class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Баланс')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name
