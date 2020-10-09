from rest_framework import serializers
from .models import (
    JednostkaOrganizacyjna,
    Uzytkownik,
)


class JednostkaOrganizacyjnaSerializer(serializers.ModelSerializer):

    class Meta:
        model = JednostkaOrganizacyjna
        fields =  "__all__"
        #exclude = [ 'id', ]
        #fields = ['id', 'nazwa', 'opis']


class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = "__all__"
