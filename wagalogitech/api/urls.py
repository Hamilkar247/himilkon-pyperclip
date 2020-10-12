from django.urls import path
from . import views

urlpatterns = [
    path('jednostkiOrganizacyjne/', views.jednostka.as_view()),
    #path('jednostkaOrganizacyjna/<int:id_jednostki>/', views.JednostkaOrganizacyjnaPojedynczy.as_view()),
    path('uzytkownicy/<str:uzytkownik_login>/', views.Uzytkownik.as_view()),
    #path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna, name=""),
    #path('users/', ListCreateAPIView.as_view(queryset=Uzytkownik.objects.all()
    #, serializer_class=UzytkownikSerializer), name='user-list')
    path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna),
    #==============https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
    path('api/pomiary', views.pomiar_list),
    path('api/pomiary/<int:pk>/', views.pomiar_detail),
    path('api/logpomiarowe', views.logpomiar_list),
    path('api/logpomiarowe/<int:pk>/', views.logpomiar_detail)#czemu pk?
]

