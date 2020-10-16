from django.contrib import admin
from .models import JednostkaOrganizacyjna
#from django.contrib.auth.models import User
from .models import SesjaUzytkownika
from .models import SeriaPomiarowa
from .models import Pomiar
from .models import LogPomiarowy
from .models import LogAdministracyjny

admin.site.register(JednostkaOrganizacyjna)
#admin.site.register(User)
admin.site.register(SesjaUzytkownika)
admin.site.register(LogAdministracyjny)
admin.site.register(SeriaPomiarowa)
admin.site.register(Pomiar)
admin.site.register(LogPomiarowy)

