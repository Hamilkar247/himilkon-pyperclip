from django.forms import forms
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from core.models import Organizacja, Pomiar

# Create your views here.
from django.template import loader
from requests import Response
from rest_framework import serializers
from rest_framework.decorators import api_view

#from .forms import PomiarForm
#from ..api.serializers import OrganizacjaSerializer


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
    return render(request, 'front/organizacje.html', context)#template, context)

#@api_view(['GET', 'POST'])
#def list_organizacja(request):
#    if request.method == "GET":
#        organizacje = Organizacja.objects.all()
#        serializer_class = OrganizacjaSerializer(organizacje, many=True)
#        return Response(serializer_class.data)
#    else:
#        serializer_class = OrganizacjaSerializer(data=request.data)
#        if serializer_class.is_valid():
#            serializer_class.save()
#            return Response(serializer_class.data, status=201) #Successfult post
#        return Response(serializer_class.errors, status=400) #Invalid data
def organizacja_detail(request, organizacja_id):
    organizacja = get_object_or_404(Organizacja, pk=organizacja_id)
    return render(request, "front/organizacja_detail.html", {'organizacja': organizacja})
#
#
#@api_view(['GET','DELETE','PUT'])
#def organizacja_details(request, nazwa):
#    try:
#        organizacja = Organizacja.objects.get(nazwa=nazwa)
#    except:
#        return Response(status=404)
#
#    if request.method == 'GET':
#        serializer_class = OrganizacjaSerializer(organizacja)
#        return Response(serializer_class.data)
#    elif request.method == 'PUT': #UPDATE
#        serializer_class = OrganizacjaSerializer(organizacja, data=request.data)
#        if serializer_class.is_valid():
#            serializer_class.save() #Update table in db
#            return Response(serializer_class.data)
#        return Response(serializer_class.errors, status=400) #Bad request
#    elif request.method == 'DELETE':
#        organizacja.delete()
#        return Response(status=204)


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


def leftPanel(request):
    return render(request, "front/leftPanel.html")


def przyklad(request):
    return render(request, "front/przyklad.html")