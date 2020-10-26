from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from api.models import Organizacja

# Create your views here.
from django.template import loader
from requests import Response


def front_root(request):
    return HttpResponse("Waga - LOGITECH")


def home(request):
    template = loader.get_template('front/home.html')
    return render(request, 'front/home.html')


def login(request):
    template = loader.get_template('front/login.html')
    return render(request, 'front/login.html')


def logout(request):
    return HttpResponse("Logout")


def organizacje(request):
    organizacje_list = Organizacja.objects.all()
    template = loader.get_template('front/index.html')
    context = {
        'organizacje_list': organizacje_list
    }
    return render(request, 'front/organizacje.html', context)

def szczegoly(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/szczegoly.html", {'organizacja': organizacja})
