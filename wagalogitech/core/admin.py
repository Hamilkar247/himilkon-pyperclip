from django.contrib import admin

# Register your models here.
from .models import Organizacja, SesjaUzytkownika, \
    LogAdministracyjny, SeriaPomiarowa, Pomiar, LogPomiarowy

admin.site.register(Organizacja)
#admin.site.register(User)
admin.site.register(SesjaUzytkownika)
admin.site.register(LogAdministracyjny)
admin.site.register(SeriaPomiarowa)
admin.site.register(Pomiar)
admin.site.register(LogPomiarowy)
