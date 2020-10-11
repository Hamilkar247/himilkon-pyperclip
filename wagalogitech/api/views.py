from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework import authtoken
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
    #    jednostkaOrganizacyjna = JednostkaOrganizacyjna.objects.all()
    #    serializer = serializers.JednostkaOrganizacyjnaSerializer(jednostkaOrganizacyjna, many=True)
    #    return Response(serializer.data)

    # def post(self, request):
    #    serializer = serializers.JednostkaOrganizacyjnaSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializers.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Uzytkownik(APIView):
    # queryset = Uzytkownik.objects.all()
    # serializer_class = UzytkownikSerializer
    # """
    # do uzupelnienia
    # """

    def get(self, uzytkownik_login):  # ,format=None):
        """
        zwraca liste uzytkownikow
        :param request:
        :param format:
        :return:
        """
        print(uzytkownik_login)
        queryset = Uzytkownik.objects.get(login=uzytkownik_login)
        serializers_class = UzytkownikSerializer
        # return Response('na buty teutatesa')#serializers_class.data)
        # uzytkownicy_loginy = [uzytkownik.login for uzytkownik in Uzytkownik.objects.all()]
        return Response(serializers_class)


# class UserList(generics.ListCreateAPIView):
#    queryset = Uzytkownik.objects.all()
#    serializer_class = UzytkownikSerializer
#
#    def list(self, request):
#        queryset = self.get_queryset()
#        serializer = UzytkownikSerializer(queryset, many=True)
#        return Response(serializer.data)


def response_jednostkaOrganizacyjna(request, jednostkaOrganizacyjna_id):
    try:
        jednostka = JednostkaOrganizacyjna.objects.filter(id=jednostkaOrganizacyjna_id)
        if not jednostka:
            print("nie ma jednostki o tej nazwie !")
    except ObjectDoesNotExist:
        return HttpResponse("Nie ma jednostki o tym id!")

    #return HttpResponse("nazwa jednostki to:" + nazwa_jednostki)
    return render(request, "api/")
