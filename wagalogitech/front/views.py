from django.http import HttpResponse
from django.shortcuts import render
from api.models import Organizacja

# Create your views here.
from requests import Response


def front_root(request):
    return HttpResponse("Waga - LOGITECH")


def login(request):
    return HttpResponse("Login")


def organizacje(request):
    query_set=Organizacja.objects.all()
    output=', '.join([q.nazwa for q in query_set])
    return HttpResponse("Organizacje:"+output)


def szczegoly(request, organizacja_id):
    query_set=Organizacja.objects.get(pk=organizacja_id)
    output="Nazwa:" + str(query_set.nazwa) + " Opis:"+ str(query_set.opis)
    return HttpResponse(output)
