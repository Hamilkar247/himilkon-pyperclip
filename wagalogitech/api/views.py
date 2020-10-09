from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import (

JednostkaOrganizacyjna,
Uzytkownik,

)
from .serializers import (

JednostkaOrganizacyjnaSerializer,
UzytkownikSerializer

)

class JednostkaOrganizacyjna(generics.ListAPIView):

   queryset = JednostkaOrganizacyjna.objects.all()
   serializer_class = JednostkaOrganizacyjnaSerializer

   # def get(self, request):
   #     jednostkaOrganizacyjna = JednostkaOrganizacyjna.objects.all()
   #     serializer = serializers.JednostkaOrganizacyjnaSerializer(jednostkaOrganizacyjna, many=True)
   #     return Response(serializer.data)

   # def post(self, request):
   #     serializer = serializers.JednostkaOrganizacyjnaSerializer(data=request.data)
   #     if serializer.is_valid():
   #         serializers.save()
   #         return Response(serializer.data, status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST


class Uzytkownik(generics.ListAPIView):

   queryset = Uzytkownik.objects.all()
   serializer_class = UzytkownikSerializer