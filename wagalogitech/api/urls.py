from django.urls import path
from . import views

urlpatterns = [
    path('jednostkiOrganizacyjne/', views.JednostkaOrganizacyjna.as_view()),
    path('uzytkownicy/<str:uzytkownik_login>/', views.Uzytkownik.as_view()),
    path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna, name=""),
    #path('users/', ListCreateAPIView.as_view(queryset=Uzytkownik.objects.all()
    #, serializer_class=UzytkownikSerializer), name='user-list')
]