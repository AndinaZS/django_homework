from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    path = settings.BUS_STATION_CSV
    with open(path, encoding='UTF-8') as file:
        data = []
        reader = csv.DictReader(file)
        for el in reader:
            dct = {'Name': el['Name'],
                   'Street': el['Street'],
                   'District': el['District']}
            data.append(dct)

    paginator = Paginator(data, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
