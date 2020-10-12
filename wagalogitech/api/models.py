from django.db import models
import uuid


# uuid Universal Unique Identifier python library
# which helps in generating random objects of 128 bits


class JednostkaOrganizacyjna(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nazwa = models.CharField(max_length=200, verbose_name="Nazwa")
    opis = models.CharField(max_length=500, verbose_name="Opis")

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Jednostka Organizacyjna"
        verbose_name_plural = "Jednostki Organizacyjne"


class Uzytkownik(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=120, unique=True, verbose_name="Login")
    haslo = models.CharField(max_length=120, unique=True, verbose_name="Haslo")
    isSuperuser = models.BooleanField()

    def __str__(self):
        return self.login

    # jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna)
    # def __str__(self):
    #    return self.log

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"


class SesjaUzytkownika(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    # pomiar = models.ForeignKey(Pomiar, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sesja Użytkownika"
        verbose_name_plural = "Sesje Użytkowników"


class LogAdministracyjny(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    opis = models.CharField(max_length=500, verbose_name="Opis")
    data = models.DateField(blank=False, verbose_name="Data")
    czynnosc = models.CharField(max_length=200, verbose_name="Czynność")
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, verbose_name="Użytkownik")
    jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna, on_delete=models.CASCADE,
                                                verbose_name="Jednostka organizacyjna")

    class Meta:
        verbose_name = "Log Administracyjny"
        verbose_name_plural = "Logi Administracyjne"


class SeriaPomiarowa(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nazwa_sesji = models.CharField(max_length=100, verbose_name="nazwa sesji")

    # jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Seria Pomiarowwa"
        verbose_name_plural = "Serie Pomiarowe"


# ======= https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
class Pomiar(models.Model):
    # stworzona = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    czyWazny = models.BooleanField(verbose_name="Czy ważny?")
    wartosc = models.CharField(max_length=300, verbose_name="wartość")
    data_pomiaru = models.DateTimeField(blank=False, verbose_name="data pomiaru", auto_now_add=True)
    #sesja_uzytkownika = models.ForeignKey(SesjaUzytkownika, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data_pomiaru)

    class Meta:
        verbose_name = "Pomiar"
        verbose_name_plural = "Pomiary"
        ordering = ['data_pomiaru']


# ======= https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer

class LogPomiarowy(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    opis = models.CharField(max_length=500)
    data = models.DateField()
    pomiar = models.ForeignKey(Pomiar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Log Pomiarowy"
        verbose_name_plural = "Logi Pomiarowe"
