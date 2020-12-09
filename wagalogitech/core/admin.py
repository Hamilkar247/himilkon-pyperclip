from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

# Register your models here.
from .models import Organizacja, SesjaUzytkownika, \
    LogAdministracyjny, SeriaPomiarowa, Pomiar, LogPomiarowy

admin.site.register(Organizacja)
admin.site.register(User, UserAdmin)
admin.site.register(SesjaUzytkownika)
admin.site.register(LogAdministracyjny)
admin.site.register(SeriaPomiarowa)
admin.site.register(Pomiar)
admin.site.register(LogPomiarowy)
