from datetime import timezone

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Organizacja,
    Pomiar, SesjaUzytkownika, LogPomiarowy, LogAdministracyjny, SeriaPomiarowa,
)

class OrganizacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacja
        fields = "__all__"
        # exclude = [ 'id', ]
        # fields = ['id', 'nazwa', 'opis']


class UserSerializer(serializers.ModelSerializer):
    pomiary = serializers.PrimaryKeyRelatedField(many=True, queryset=Pomiar.objects.all())

    class Meta:
        model = User
        fields = "__all__" #['id', 'username', 'pomiary']


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
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pomiar
        fields = "__all__"
        # field = ['id', 'czyWazny', 'wartosc', 'data_pomiaru'] #niestety bledogenny zapis


class LogPomiarowySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogPomiarowy
        fields = "__all__"


#=========== https://www.django-rest-framework.org/tutorial/3-class-based-views/

class LogAdministracyjnySerializer(serializers.ModelSerializer):
    class Meta:
        model =  LogAdministracyjny
        fields = "__all__"


#=========== https://www.django-rest-framework.org/tutorial/3-class-based-views/

class SeriaPomiarowaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriaPomiarowa
        fields = "__all__"
