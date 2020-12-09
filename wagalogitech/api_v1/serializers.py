from datetime import timezone

from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import (
    Organizacja,
    Pomiar, SesjaUzytkownika, LogPomiarowy, LogAdministracyjny, SeriaPomiarowa,
    User,
)


class PomiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pomiar
        fields = "__all__"
        # field = ['id', 'czyWazny', 'wartosc', 'data_pomiaru'] #niestety bledogenny zapis


class OrganizacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacja
        fields = "__all__"
        # exclude = [ 'id', ]
        # fields = ['id', 'nazwa', 'opis']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # ['id', 'username', 'pomiary']


class SesjaUzytkownikaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SesjaUzytkownika
        fields = '__all__'


class LogAdministracyjnySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LogAdministracyjny
        fields = "__all__"


class SeriaPomiarowaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriaPomiarowa
        fields = "__all__"


class LogPomiarowySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogPomiarowy
        fields = "__all__"
