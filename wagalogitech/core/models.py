from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Pomiar(models.Model):
    czyWazny = models.BooleanField(verbose_name="Czy ważny?")
    jednostka_miary = models.CharField(verbose_name="Jednostka miary", max_length=50)
    wartosc = models.CharField(max_length=300, verbose_name="wartość")
    data_pomiaru = models.DateTimeField(blank=False, verbose_name="data pomiaru", auto_now_add=True)
    sesja_uzytkownika = models.ForeignKey('SesjaUzytkownika', on_delete=models.CASCADE)
    seria_pomiarowa = models.ForeignKey('SeriaPomiarowa', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sesja_uzytkownika) + ' ' + str(self.seria_pomiarowa) + ' ' + str(
            self.data_pomiaru) + ' wart: ' + str(self.wartosc)

    def save(self, *args, **kwargs):
        czyWazny = 'table' if self.czyWazny else False
        super(Pomiar, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pomiar"
        verbose_name_plural = "Pomiary"
        ordering = ['data_pomiaru']


# class Uzytkownik(models.Model):
#    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    login = models.CharField(max_length=120, unique=True, verbose_name="Login")
#    haslo = models.CharField(max_length=120, unique=True, verbose_name="Haslo")
#    isSuperuser = models.BooleanField()
#
#    def __str__(self):
#        return self.login
#
#    # jednostka_organizacyjna = models.ForeignKey(JednostkaOrganizacyjna)
#    # def __str__(self):
#    #    return self.log
#
#    class Meta:
#        verbose_name = "Użytkownik"
#        verbose_name_plural = "Użytkownicy"


class Organizacja(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nazwa = models.CharField(max_length=200, verbose_name="Nazwa")
    opis = models.CharField(max_length=500, verbose_name="Opis")
    adres = models.CharField(max_length=200, verbose_name="Adres")

    # to bardziej szef szefow niz uzytkownik - potem trzeba pomyśleć czy nei trzeba by zrobić organizacja uzytkownik many to many
    # owner = models.ForeignKey('auth.User', related_name='pomiary', on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

    def save(self, *args, **kwargs):
        super(Organizacja, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Organizacja"
        verbose_name_plural = "Organizacje"
        ordering = ['id']


class SesjaUzytkownika(models.Model):
    start_sesji = models.DateTimeField(blank=False, verbose_name="start sesji")
    koniec_sesji = models.DateTimeField(blank=True, verbose_name="koniec sesji")
    owner = models.ForeignKey("User", related_name='sesjeuzytkownika', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner) + " " + str(self.start_sesji)

    def save(self, *args, **kwargs):
        super(SesjaUzytkownika, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Sesja Użytkownika"
        verbose_name_plural = "Sesje Użytkowników"
        ordering = ['start_sesji']


class LogAdministracyjny(models.Model):
    opis = models.CharField(max_length=500, verbose_name="Opis")
    data = models.DateField(blank=False, verbose_name="Data")
    czynnosc = models.CharField(max_length=200, verbose_name="Czynność")
    owner = models.ForeignKey("User", related_name="logiadministracyjne", on_delete=models.CASCADE)
    organizacja = models.ForeignKey(Organizacja, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Log Administracyjny"
        verbose_name_plural = "Logi Administracyjne"
        ordering = ['data']

    def __str__(self):
        return str(self.opis)

    def save(self, *args, **kwargs):
        super(LogAdministracyjny, self).save(*args, **kwargs)


class SeriaPomiarowa(models.Model):
    nazwa_serii = models.CharField(max_length=100, verbose_name="nazwa serii")
    opis = models.CharField(max_length=300, verbose_name="opis serii")
    czyZakonczona = models.BooleanField(verbose_name="Czy zakończono serie pomiarową?")
    organizacja = models.ForeignKey(Organizacja, on_delete=models.CASCADE)
    start_pomiaru = models.DateTimeField(blank=False, verbose_name="start pomiaru")
    koniec_pomiaru = models.DateTimeField(blank=True, verbose_name="koniec pomiaru")

    def __str__(self):
        return str(self.nazwa_serii)

    def save(self, *args, **kwargs):
        super(SeriaPomiarowa, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Seria Pomiarowa"
        verbose_name_plural = "Serie Pomiarowe"


class LogPomiarowy(models.Model):
    opis = models.CharField(max_length=500, verbose_name="Opis")
    data = models.DateField(verbose_name="data")
    czynnosc = models.CharField(max_length=300, verbose_name="Czynność")
    pomiar = models.ForeignKey(Pomiar, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.opis)

    def save(self, *args, **kwargs):
        super(LogPomiarowy, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Log Pomiarowy"
        verbose_name_plural = "Logi Pomiarowe"
