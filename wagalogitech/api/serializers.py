from rest_framework import serializers
from .models import (
    JednostkaOrganizacyjna,
)


class JednostkaOrganizacyjnaSerializer(serializers.ModelSerializer):

    class Meta:
        model = JednostkaOrganizacyjna
        fields =  "__all__"
        #exclude = [ 'id', ]
        #fields = ['id', 'nazwa', 'opis']