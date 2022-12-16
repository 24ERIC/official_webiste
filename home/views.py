from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse

from json import dumps

def index(request):
    # create data dictionary
    dataDictionary = {
    'hello': 'World',
    'geeks': 'forgeeks',
    'ABC': 123,
    456: 'abc',
    14000605: 1,
    'list': ['geeks', 4, 'geeks'],
    'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    # dump data
    dataJSON = dumps(dataDictionary)
    return render(request, 'home.html', {'data': dataJSON})