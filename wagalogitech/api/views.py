# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (

    Pomiar, LogPomiarowy, LogAdministracyjny, SeriaPomiarowa, Organizacja, SesjaUzytkownika,
)
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


class OrganizacjaViewSet(viewsets.ModelViewSet):
    queryset = Organizacja.objects.all()  # filter(id=1)
    serializer_class = OrganizacjaSerializer


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
