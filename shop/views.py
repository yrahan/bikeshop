#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Mimmi!<br>You're at the awesome Bikeshop homepage.")
