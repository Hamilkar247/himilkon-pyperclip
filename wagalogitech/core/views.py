from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def core_root(request):
    return HttpResponse("Waga - LOGITECH")