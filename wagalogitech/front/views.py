from django.http import HttpResponse
from django.shortcuts import render
from api.models import Organizacja

# Create your views here.
from django.template import loader
from requests import Response


def front_root(request):
    return HttpResponse("Waga - LOGITECH")


def login(request):
    return HttpResponse("Login")


def organizacje(request):
    organizacje_list = Organizacja.objects.all()
    template = loader.get_template('front/index.html')
    context = {
        'organizacje_list': organizacje_list
    }
    return HttpResponse(template.render(context, request))


def szczegoly(request, organizacja_id):
    query_set=Organizacja.objects.get(pk=organizacja_id)
    output="Nazwa:" + str(query_set.nazwa) + " Opis:"+ str(query_set.opis)
    return HttpResponse(output)
