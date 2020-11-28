# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import permissions, viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.shortcuts import redirect

from core.models import Pomiar, LogPomiarowy, LogAdministracyjny \
    , SeriaPomiarowa, Organizacja, SesjaUzytkownika

from .permissions import IsOwnerOrReadOnly
from .serializers import (

    PomiarSerializer, LogPomiarowySerializer, LogAdministracyjnySerializer,
    UserSerializer, OrganizacjaSerializer, SesjaUzytkownikaSerializer

)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pomiary': reverse('pomiar-list', request=request, format=format),
        'organizacja': reverse('organizacja-list', request=request, format=format)
    })


# This time we've used the ModelViewSet class in order to get the complete set of default read and write operations.
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


#class OrganizacjeList(APIView):
#    """
#    List all snippets, or create a new snippet.
#    """
#    def get(self, request, format=None):
#        organizacja = Organizacja.objects.all()
#        serializer = OrganizacjaSerializer(organizacja, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, format=None):
#        serializer = OrganizacjaSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#class OrganizacjeDetail(APIView):
#    """
#    Retrieve, update or delete a snippet instance.
#    """
#    def get_object(self, pk):
#        try:
#            return Organizacja.objects.get(pk=pk)
#        except Organizacja.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk, format=None):
#        organizacja = self.get_object(pk)
#        serializer = OrganizacjaSerializer(organizacja)
#        return Response(serializer.data)
#
#    def put(self, request, pk, format=None):
#        organizacja = self.get_object(pk)
#        serializer = OrganizacjaSerializer(organizacja, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk, format=None):
#        organizacja = self.get_object(pk)
#        organizacja.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizacjaViewSet(viewsets.ModelViewSet):
    queryset = Organizacja.objects.all()  # filter(id=1)
    serializer_class = OrganizacjaSerializer

    def post(self, request):
        print("cokolwiek")


#class Get_organization_List(APIView):
#    def get(self, request):
#        organizacje = Organizacja.objects.all()
#        serializer_class = OrganizacjaSerializer
#
#
#@csrf_exempt # w przyszlosci trzeba znalezc inny sposób - to nie jest zbyt zalecane
#def dodajOrganizacje(request):
#    organizacje = Organizacja(nazwa=request.POST['nazwa'], opis=request.POST['opis'])
#    organizacje.save()
#    return redirect('/')



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewsets automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SesjaUzytkownikaViewSet(viewsets.ModelViewSet):
    queryset = SesjaUzytkownika.objects.all()
    serializer_class = SesjaUzytkownikaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LogAdministracyjnyViewSet(viewsets.ModelViewSet):
    queryset = LogAdministracyjny.objects.all()
    serializer_class = LogAdministracyjnySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SeriaPomiarowaViewSet(viewsets.ModelViewSet):
    queryset = SeriaPomiarowa.objects.all()
    serializer_class = SeriaPomiarowa
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class LogPomiarowyViewSet(viewsets.ModelViewSet):
    queryset = LogPomiarowy.objects.all()
    serializer_class = LogPomiarowySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
