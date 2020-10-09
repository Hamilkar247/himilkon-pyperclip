from django.urls import path
from . import views

urlpatterns = [
    path('jednostkaOrganizacyjna/', views.JednostkaOrganizacyjna.as_view()),
    path('uzytkownicy/', views.Uzytkownik.as_view()),
]