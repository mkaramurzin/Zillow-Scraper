from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.views.decorators.csrf import csrf_exempt
from csv import writer
from django.http import HttpResponse
import os

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "scraper/index.html")
    

    url = request.POST['url']
    file = 'hosuing.csv'
    with open(file, 'w', encoding='utf-8', newline='') as f:
        w = writer(f)
        header = ['Title', 'Location', 'Price']
        w.writerow(header)

    with open(file, 'rt', encoding='utf-8', newline='') as f:
        data = f.read()

    os.remove(file)
    response = HttpResponse(data)
    response['Content-Disposition'] = 'attachment; filename="housing.csv"'
    return response