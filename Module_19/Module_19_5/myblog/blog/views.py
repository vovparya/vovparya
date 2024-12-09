from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    post_list = Post.objects.all()

    # Получаем количество элементов на странице из GET-параметра 'num', по умолчанию 5
    num = request.GET.get('num', 5)
    try:
        num = int(num)
    except ValueError:
        num = 5  # Если значение невалидное, используем 5

    paginator = Paginator(post_list, num)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'num': num,  # Передаём 'num' в контекст
    }
    return render(request, 'blog/post_list.html', context)
