from django.db import models
import uuid


# uuid Universal Unique Identifier python library
# which helps in generating random objects of 128 bits


class JednostkaOrganizacyjna(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nazwa = models.CharField(max_length=200, verbose_name="Nazwa")
    opis = models.CharField(max_length=500, verbose_name="Opis")

    def __str__(self):
        return self.nazwa

class Uzytkownik(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=120, unique=True, verbose_name="Login")
    haslo = models.CharField(max_length=120, unique=True, verbose_name="Haslo")
    isSuperuser = models.BooleanField()

    def __str__(self):
        return self.login

    # jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna)
    #def __str__(self):
    #    return self.log


class SesjaUzytkownika(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    # pomiar = models.ForeignKey(Pomiar, on_delete=models.CASCADE)
    uzytkownik = models.ForeiggnKey(Uzytkownik, on_delete=models.CASCADE)


class LogAdministracyjny(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    opis = models.CharField(max_length=500, verbose_name="Opis")
    data = models.DateField(blank=False, verbose_name="Data")
    czynnosc = models.CharField(max_length=200, verbose_name="Czynność")
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, verbose_name="Użytkownik")
    jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna, on_delete=models.CASCADE,
                                                verbose_name="Jednostka organizacyjna")


class SeriaPomiarowa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nazwa_sesji = models.CharField(max_length=100, verbose_name="nazwa sesji")
    #jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna, on_delete=models.CASCADE)


class Pomiar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    czyWazny = models.BooleanField(verbose_name="Czy ważny?")
    wartosc = models.CharField(max_length=300, verbose_name="wartość")
    data_pomiaru = models.DateField(blank=False, verbose_name="data pomiaru")
    sesja_uzytkownika = models.ForeignKey(SesjaUzytkownika, on_delete=models.CASCADE)


class LogPomiarowy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    opis = models.CharField(max_length=500)
    data = models.DateField()
    pomiar = models.ForeignKey(Pomiar, on_delete=models.CASCADE)
