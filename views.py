from django.shortcuts import render
from .models import Home, Fish
from django.views.generic import ListView, DetailView


class HomeListView(ListView):
    model = Home


class HomeDetailView(DetailView):
    model = Home


class FishListView(ListView):
    model = Fish


class FishDetailView(DetailView):
    model = Fish


def index(request):
    text_head = 'На нашем сайте вы найдете место для своего лучшего отдыха'
    # Данные о домах
    homes = Home.objects.all()
    num_homes = Home.objects.all().count()

    # Данные об рыбах
    fishs = Fish.objects
    num_fishs = Fish.objects.count()

    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
               'homes': homes, 'num_homes': num_homes,
               'fishs': fishs, 'num_fishs': num_fishs}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = 'Сведения о базе отдыха'
    name = '"Зелёный угол"'
    rab1 = 'Чистый воздух'
    rab2 = 'Для любителей тихой охоты'
    rab3 = 'Баня она и в африке баня'
    rab4 = 'Что еще нужно для души'
    context = {'text_head': text_head, 'name': name,
               'rab1': rab1, 'rab2': rab2,
               'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = '"Зелёный угол"'
    address = 'Московская область, г.о.Егорьевск, дер.Иваново'
    tel = '111-222-333-444'
    email = 'greencorner@mail.ru'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
               'name': name, 'address': address,
               'tel': tel,
               'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)
