from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import status, generics, mixins
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
    Pomiar, LogPomiarowy, LogAdministracyjny, SeriaPomiarowa,
)
from .serializers import (

    JednostkaOrganizacyjnaSerializer,
    UzytkownikSerializer, PomiarSerializer, LogPomiarowySerializer, LogAdministracyjnySerializer,
    SeriaPomiarowaSerializer

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


# already mixed-in generic views  https://www.django-rest-framework.org/tutorial/3-class-based-views/
class PomiarList(generics.ListCreateAPIView):
    """ List all pomiar, or create a new pomiar"""
    queryset = Pomiar.objects.all()
    serializer_class = PomiarSerializer


# already mixed-in generic view https://www.django-rest-framework.org/tutorial/3-class-based-views/
class PomiarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pomiar.objects.all()
    serializer_class = PomiarSerializer


# mixins https://www.django-rest-framework.org/tutorial/3-class-based-views/
class SeriaPomiarowaList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = SeriaPomiarowa.objects.all()
    serializer_class = SeriaPomiarowaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# mixins https://www.django-rest-framework.org/tutorial/3-class-based-views/
class SeriaPomiarowaDetail(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = SeriaPomiarowa.objects.all()
    serializer_class = SeriaPomiarowaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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


# https://www.django-rest-framework.org/tutorial/3-class-based-views/
class LogAdminList(APIView):
    def get(self, request, format=None):
        logadmin = LogAdministracyjny.objects.all()
        serializer = LogAdministracyjnySerializer(logadmin, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogAdministracyjnySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# https://www.django-rest-framework.org/tutorial/3-class-based-views/
class LogAdminDetail(APIView):
    def get_object(self, pk):
        try:
            return LogAdministracyjny.objects.get(pk=pk)
        except Pomiar.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        logadmin = self.get_object(pk)
        serializer = LogAdministracyjnySerializer(logadmin)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        logadmin = self.get_object(pk)
        serializer = LogAdministracyjnySerializer(logadmin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        logadmin = self.get_object(pk)
        logadmin.delete()
        return Response(status.HTTP_204_NO_CONTENT)


