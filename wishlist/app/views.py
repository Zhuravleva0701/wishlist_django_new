from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.decorators.http import require_http_methods

"""Основной функционал приложения описан функциями получения всех обьектов,
добавления нового обьекта, обновления и удаления по айди"""


def index(request):
    wishlist = Item.objects.all()
    return render(request, 'wishlist/index.html', {'wishlist': wishlist, 'title': 'Главная страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    price = request.POST['price']
    item = Item(title=title, description=description, price=price)
    item.save()
    return redirect('index')


def update(request, item_id):
    item = Item.objects.get(id=item_id)
    item.is_complete = not item.is_complete
    item.save()
    return redirect('index')


def delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('index')