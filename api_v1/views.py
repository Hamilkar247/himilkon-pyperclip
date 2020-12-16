# Create your views here.
from rest_framework import permissions, viewsets, generics, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import Pomiar, LogPomiarowy, LogAdministracyjny \
    , SeriaPomiarowa, Organizacja, SesjaUzytkownika, User

from .permissions import IsOwnerOrReadOnly
from .serializers import (

    PomiarSerializer, LogPomiarowySerializer, LogAdministracyjnySerializer,
    UserSerializer, OrganizacjaSerializer, SesjaUzytkownikaSerializer, SeriaPomiarowaSerializer

)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pomiar': reverse('pomiar-list', request=request, format=format),
        'organizacja': reverse('organizacja-list', request=request, format=format),
        'sesjaUzytkownika': reverse('sesjaUzytkownika-list', request=request, format=format),
        'logAdministracyjny': reverse('logAdministracyjny-list', request=request, format=format),
        'seriaPomiarowa': reverse('seriaPomiarowa-list', request=request, format=format),
        'logPomiarowy': reverse('logPomiarowy-list', request=request, format=format),
    })


class PomiarViewSet(viewsets.ModelViewSet):
    queryset = Pomiar.objects.all()
    serializer_class = PomiarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # metoda potrzebna gdy chce użyc tego modelu w innym zrobie do pomiaru PrimaryKeyRelatedField
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrganizacjaViewSet(viewsets.ModelViewSet):
    queryset = Organizacja.objects.all()  # filter(id=1)
    serializer_class = OrganizacjaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
    serializer_class = LogAdministracyjnySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SeriaPomiarowaViewSet(viewsets.ModelViewSet):
    queryset = SeriaPomiarowa.objects.all()
    serializer_class = SeriaPomiarowaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # example URL http://127.0.0.1:8000/api/v1/seriaPomiarowa/1/pomiary
    @action(methods=['get'], detail=True, permission_classes=[
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
    def pomiary(self, request, pk):
        ser_pom = SeriaPomiarowa.objects.get(pk=pk)
        pomiary = Pomiar.objects.filter(seria_pomiarowa=ser_pom)
        serializer = PomiarSerializer(pomiary, many=True)
        return Response(serializer.data)


class LogPomiarowyViewSet(viewsets.ModelViewSet):
    queryset = LogPomiarowy.objects.all()
    serializer_class = LogPomiarowySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
