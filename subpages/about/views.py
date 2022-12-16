from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse

def index(request):
    
    return render(request, 'contact.html')