from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import status, generics
from rest_framework import authtoken
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import (

    JednostkaOrganizacyjna,
    Uzytkownik,
    Pomiar, LogPomiarowy,
)
from .serializers import (

    JednostkaOrganizacyjnaSerializer,
    UzytkownikSerializer, PomiarSerializer, LogPomiarowySerializer

)


class jednostka(generics.ListAPIView):
    queryset = JednostkaOrganizacyjna.objects.all()  # filter(id=1)
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


# class JednostkaOrganizacyjnaPojedynczy(generics.ListAPIView, id_jednostki):
#   queryset = JednostkaOrganizacyjna.objects.filter(id=id_jednostki)
#   serializer_class = JednostkaOrganizacyjnaSerializer

# ========https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
@csrf_exempt
def jedorg_list(request):
    '''List all jednostek organizacyjnych'''
    if request.method == 'GET':
        jednostka = JednostkaOrganizacyjna.objects.all()
        serializer = JednostkaOrganizacyjnaSerializer(jednostka, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JednostkaOrganizacyjnaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
##def jednostka_detail(request, id_jednostki):
#    """
#    Retrieve, update or delete a code snippet
#    """
#    try:
#        snippet = JednostkaOrganizacyjna.objects.get(id=pk)

# =======================

class Uzytkownik(APIView):
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer

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


# def response_jednostkaOrganizacyjna(request, jednostkaOrganizacyjna_id):
# try:
# jednostka = JednostkaOrganizacyjna.objects.filter(id=jednostkaOrganizacyjna_id)
# if not jednostka:
#     print("nie ma jednostki o tej nazwie !")
# except ObjectDoesNotExist:
#   return HttpResponse("Nie ma jednostki o tym id!")

# return HttpResponse("nazwa jednostki to:" + nazwa_jednostki)
#    return render(request, "api/jednostkaOrganizacyjna.html")

def response_jednostkaOrganizacyjna(request, jednostkaOrganizacyjna_id):
    queryset = JednostkaOrganizacyjna.objects.all()
    serializer_class = JednostkaOrganizacyjnaSerializer
    # print(jed_org)
    return HttpResponse("witam:" + str(jednostkaOrganizacyjna_id))


# ================ https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#pulling-it-all-together
@api_view(['GET', 'POSt'])
def pomiar_list(request):
    """ List all pomiar, or create a new snippet """
    if request.method == 'GET':
        pomiar = Pomiar.objects.all()
        serializer = PomiarSerializer(pomiar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PomiarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pomiar_detail(request, pk):
    '''
    Retrieve, update or delete a code snippet
    :param request:
    :param pk:
    :return:
    '''
    try:
        pomiar = Pomiar.objects.get(pk=pk)
    except Pomiar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PomiarSerializer(pomiar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PomiarSerializer(pomiar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pomiar.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def logpomiar_list(request):
    if request.method == 'GET':
        logpomiar = LogPomiarowy.objects.all()
        serializer = LogPomiarowySerializer(logpomiar, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PomiarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@csrf_exempt
def logpomiar_detail(request, pk):
    try:
        logpomiar = LogPomiarowy.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LogPomiarowySerializer(logpomiar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LogPomiarowySerializer(logpomiar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        logpomiar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
