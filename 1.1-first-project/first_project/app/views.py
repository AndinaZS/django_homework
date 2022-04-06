import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_files = os.listdir(path='.')
    msg = 'В текущей директории находятся файлы: '
    for file in list_files:
        if '.' in file:
            msg += f'-- {file} '
    print(msg)
    return HttpResponse(msg)
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории


    #raise NotImplemented
