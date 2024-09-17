import os
from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона не было,
    # но теперь чу-чут есть и возвращается не просто текст)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'<h1><span style = "color: 01ff2d">Текущее время:</span></h1> <br>{current_time}')


    # по аналогии с `time_view`, написан код,
    # который возвращает список файлов в рабочей 
    # директории
def workdir_view(request):
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    return HttpResponse(f'<h1>Содержимое рабочей директории:</h1><p>{files_list}</p>')