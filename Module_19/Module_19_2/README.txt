Согласно заданию:
"Также напишите список QuerySet запросов в порядке вызовов,
которые использовали для внесения изменений в БД."
________________________________________________________

# Запуск интерактивной оболочки Django
python manage.py shell
________________________________________________________

# 1. Импорт моделей.
from task1.models import Buyer, Game
________________________________________________________

# 2. Создание покупателей
buyer1 = Buyer.objects.create(
    name='Ilya',
    balance=1500.05,
    age=24
)

buyer2 = Buyer.objects.create(
    name='terminator2000',
    balance=42.15,
    age=52
)

buyer3 = Buyer.objects.create(
    name='Ubivator432',
    balance=0.5,
    age=16  (Младше 18 лет)
)
________________________________________________________

# 3. Создание игр
game1 = Game.objects.create(
    title='Cyberpunk 2077',
    cost=31,
    size=46.2,
    description='Game of the year',
    age_limited=True
)

game2 = Game.objects.create(
    title='Mario',
    cost=5,
    size=0.5,
    description='Old Game',
    age_limited=False  (Без ограничения возраста)
)

game3 = Game.objects.create(
    title='Hitman',
    cost=12,
    size=36.6,
    description='Who kills Mark?',
    age_limited=True
)
________________________________________________________

# 4. Связывание покупателей с играми

# 4.1. Покупатель "Ilya" (buyer1) получает все игры
game1.buyer.add(buyer1)
game2.buyer.add(buyer1)
game3.buyer.add(buyer1)

# 4.2. Покупатель "terminator2000" (buyer2) получает игры с ограничением по возрасту
game1.buyer.add(buyer2)
game3.buyer.add(buyer2)

# 4.3. Покупатель "Ubivator432" (buyer3, младше 18 лет) получает только игру без ограничения возраста
game2.buyer.add(buyer3)
________________________________________________________

# Проверка результатов
# Покупатели, приобрёвшие каждую игру
print(game1.buyer.all())  # buyer1, buyer2
print(game2.buyer.all())  # buyer1, buyer3
print(game3.buyer.all())  # buyer1, buyer2

# Игры, приобретённые каждым покупателем
print(buyer1.games.all())  # game1, game2, game3
print(buyer2.games.all())  # game1, game3
print(buyer3.games.all())  # game2

