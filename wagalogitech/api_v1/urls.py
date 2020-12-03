from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  PomiarViewSet, UserViewSet, OrganizacjaViewSet, api_root
from django.shortcuts import redirect
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pomiary', views.PomiarViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'organizacje', views.OrganizacjaViewSet)
router.register(r'sesjeuzytkownika', views.SesjaUzytkownikaViewSet)
router.register(r'logiadministracyjny', views.LogAdministracyjnyViewSet)
router.register(r'seriepomiarowe', views.SeriaPomiarowaViewSet)
router.register(r'logipomiarowe', views.LogPomiarowyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

