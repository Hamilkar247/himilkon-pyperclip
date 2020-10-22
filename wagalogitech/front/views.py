from django.shortcuts import render

# Create your views here.
from requests import Response


def front_root(request, format=None):
    return Response("Dzieńdobry")