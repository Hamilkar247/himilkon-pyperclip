from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import status, generics, mixins, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework import authtoken
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from .models import (

    Pomiar, LogPomiarowy, LogAdministracyjny, SeriaPomiarowa, Organizacja, SesjaUzytkownika,
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (

    PomiarSerializer, LogPomiarowySerializer, LogAdministracyjnySerializer,
    SeriaPomiarowaSerializer, UserSerializer, OrganizacjaSerializer, SesjaUzytkownikaSerializer

)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pomiary': reverse('pomiar-list', request=request, format=format),
        'organizacja': reverse('organizacja-list', request=request, format=format)
    })


class OrganizacjaViewSet(viewsets.ModelViewSet):

    queryset = Organizacja.objects.all()  # filter(id=1)
    serializer_class = OrganizacjaSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

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

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewsets automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


#This time we've used the ModelViewSet class in order to get the complete set of default read and write operations.
class PomiarViewSet(viewsets.ModelViewSet):
    """
    This viwset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions
    """

    queryset = Pomiar.objects.all()
    serializer_class = PomiarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # metoda potrzebna gdy chce użyc tego modelu w innym zrobie do pomiaru PrimaryKeyRelatedField
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SeriaPomiarowaViewSet(viewsets.ModelViewSet):
    queryset = SeriaPomiarowa.objects.all()
    serializer_class = SeriaPomiarowa
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SesjaUzytkownikaViewSet(viewsets.ModelViewSet):
    queryset = SesjaUzytkownika.objects.all()
    serializer_class = SesjaUzytkownikaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LogAdministracyjnyViewSet(viewsets.ModelViewSet):
    queryset = LogAdministracyjny.objects.all()
    serializer_class =  LogAdministracyjnySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


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


