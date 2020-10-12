from datetime import timezone

from rest_framework import serializers
from .models import (
    JednostkaOrganizacyjna,
    Uzytkownik, Pomiar, SesjaUzytkownika, LogPomiarowy,
)


class JednostkaOrganizacyjnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JednostkaOrganizacyjna
        fields = "__all__"
        # exclude = [ 'id', ]
        # fields = ['id', 'nazwa', 'opis']


class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = "__all__"


# class PomiarSerializer(serializers.ModelSerializer):
#    id = serializers.IntegerField(read_only=True)
#    czyWazny = serializers.BooleanField()
#    wartosc = serializers.CharField(max_length=300)
#    data_pomiaru = serializers.DateTimeField()
#    #sesja_uzytkownika = serializers.ForeignKey(SesjaUzytkownika, on_delete=models.CASCADE)
#    def create(self, validated_data):
#        '''
#        Create and return a new 'Pomiar' instance, given the validated data.
#        :param validated_data:
#        :return:
#        '''
#        return Pomiar.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        """
#        Update and return an existing 'Pomiar' instance, given the validated data
#        :param instance:
#        :param validated_data:
#        :return:
#        """
#        instance.czyWazny = validated_data.get('czyWazny', instance.czyWazny)
#        instance.wartosc = validated_data.get('wartosc', instance.wartosc)
#        instance.data_pomiaru = validated_data.get('data_pomiaru', instance.data_pomiaru)
#        instance.save()
#        return instance
#
#
#    class Meta:
#        model = Pomiar
#        fields = "__all__"

# ================ https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
class PomiarSerializer(serializers.ModelSerializer):
    """
    An automatically determined set of fields.
    Simple default implementations for the create() and update() methods.
    """

    class Meta:
        model = Pomiar
        fields = "__all__"
        # field = ['id', 'czyWazny', 'wartosc', 'data_pomiaru'] #niestety bledogenny zapis


class LogPomiarowySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogPomiarowy
        fields = "__all__"
