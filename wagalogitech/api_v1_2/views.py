from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view_api_v1_2(request):
    return HttpResponse("api v1_2")