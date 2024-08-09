from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories

#Create your views here.
def index(request):
    # categories= Categories.objects.all()


    context: dict[str, str] = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        # 'categories': categories

    }


    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас ',
        'content': 'О нас',
        'text_on_page': 'Тект о нашем магазине, почему выбрать нужно именно нас'

    }


    return render(request, 'main/about.html', context)