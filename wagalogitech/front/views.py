from django.forms import forms
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from core.models import Organizacja, Pomiar

from django.template import loader


def front_root(request):
    return HttpResponse("Waga - LOGITECH")


def kokpit(request):
    template = loader.get_template('front/kokpit.html')
    return render(request, 'front/kokpit.html')


def logout(request):
    return HttpResponse("Logout")


def organizacje(request):
    organizacje_list = Organizacja.objects.all()
    template = loader.get_template('front/organizacje.html')
    context = {
        'organizacje_list': organizacje_list
    }
    return render(request, 'front/organizacje.html', context)#template, context)


def organizacja_detail(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/organizacja_detail.html", {'organizacja': organizacja})


def organizacje_nowy(request):
    return render(request, "front/organizacje_nowy.html")


def pomiary(request):
    pomiary_list = Pomiar.objects.all()
    template = loader.get_template('front/pomiary.html')
    context = {
        'pomiary_list': pomiary_list,
    }
    return render(request, 'front/pomiary.html', context)


def pomiary_nowy(request):
    return render(request, "front/pomiary_nowy.html")


def pomiary_detail(request, pomiar_id):
    pomiar = get_object_or_404(Pomiar, pk=pomiar_id)
    return render(request, "front/pomiar_detail.html", {'pomiar': pomiar})


def szczegoly(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/szczegoly.html", {'organizacja': organizacja})


def leftPanel(request):
    return render(request, "front/leftPanel.html")


def przyklad(request):
    return render(request, "front/przyklad.html")
