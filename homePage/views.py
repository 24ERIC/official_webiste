from django.shortcuts import render


from datetime import datetime
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')