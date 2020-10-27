from django.forms import forms
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from api.models import Organizacja, Pomiar

# Create your views here.
from django.template import loader
from requests import Response
from rest_framework import serializers

from .forms import PomiarForm


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
    template = loader.get_template('front/organizacje.html')
    context = {
        'organizacje_list': organizacje_list
    }
    return render(request, template, context)


def organizacja_detail(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/organizacja_detail.html", {'organizacja': organizacja})


def pomiary(request):
    form = PomiarForm()
    pomiary_list = Organizacja.objects.all()
    template = loader.get_template('front/pomiary.html')
    context = {
        'form': form,
        'pomiary_list': pomiary_list,
    }
    return render(request, template, context)


def postPomiar(request):
    #request should be ajax and method should be POST
    if request.is_ajax and request.method == "POST":
        #get the form data
        form = PomiarForm(request.POST)
        #save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            #serialize in new pomiar object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    #some error occured
    return JsonResponse({"error": ""}, status=400)


def pomiary_detail(request, pomiar_id):
    pomiar = get_object_or_404(Pomiar, pk=pomiar_id)
    return render(request, "front/pomiar_detail.html", {'pomiar': pomiar})


def szczegoly(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/szczegoly.html", {'organizacja': organizacja})

#class MyForm(forms.Form):
#    a = forms.CharField(max_length=20)
#
#
#def form_example(request):
#    form = MyForm()
#    if request.method=='POST':
#        form = MyForm(request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
#            a = cd.get('a')