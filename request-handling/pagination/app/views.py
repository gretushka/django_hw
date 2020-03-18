from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
import urllib.parse


def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    bus_stations = []
    with open('data-398-2018-08-30.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    current_page_num = int(request.GET.get('page',1))
    paginator=Paginator(bus_stations,20,4)
    current_page=paginator.page(current_page_num)
    if current_page.has_next():
        params = urllib.parse.urlencode({'page': current_page_num + 1})
        next_page_url = "?%s" % params
    else:
        next_page_url = None
    if current_page.has_previous():
        params = urllib.parse.urlencode({'page': current_page_num - 1})
        prev_page_url = "?%s" % params
    else:
        prev_page_url = None
    return render_to_response('index.html', context={
        'bus_stations': current_page.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

