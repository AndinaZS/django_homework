from django.shortcuts import render, redirect

from phones.models import Phone

SORTING_FIELD = {'name': 'name',
                 'id': 'id',
                 'min_price': 'price',
                 'max_price': '-price'}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    field = request.GET.get('sort', 'id')
    context = {'phones': [phone for phone in Phone.objects.all().order_by(SORTING_FIELD[field])]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
