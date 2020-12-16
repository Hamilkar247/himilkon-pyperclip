from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  PomiarViewSet, UserViewSet, OrganizacjaViewSet, api_root
from django.shortcuts import redirect
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from . import views
from .apps import ApiV1Config

router = DefaultRouter()
router.register(r'pomiar', views.PomiarViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'organizacja', views.OrganizacjaViewSet)
router.register(r'sesjaUzytkownika', views.SesjaUzytkownikaViewSet)
router.register(r'logAdministracyjny', views.LogAdministracyjnyViewSet)
router.register(r'seriaPomiarowa', views.SeriaPomiarowaViewSet)
router.register(r'logPomiarowy', views.LogPomiarowyViewSet)

app_name = ApiV1Config.name
urlpatterns = [
    path('', include(router.urls)),
]

