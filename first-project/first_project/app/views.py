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
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now(tz=None)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg_list='<br/>'.join(os.listdir(path='.'))
    msg=f'Содержимое рабочей директории: <br/>{msg_list}'
    return HttpResponse(msg)