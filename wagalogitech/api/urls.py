from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.shortcuts import redirect
from django.views.generic import RedirectView

urlpatterns = [
    path('jednostkiOrganizacyjne/', views.jednostka.as_view()),
    #path('jednostkaOrganizacyjna/<int:id_jednostki>/', views.JednostkaOrganizacyjnaPojedynczy.as_view()),
    #path('uzytkownicy/<str:uzytkownik_login>/', views.Uzytkownik.as_view()),
    #path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna, name=""),
    #path('users/', ListCreateAPIView.as_view(queryset=Uzytkownik.objects.all()
    #, serializer_class=UzytkownikSerializer), name='user-list')
    path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna),
    #===========https://www.django-rest-framework.org/tutorial/3-class-based-views/
    path('api/pomiary/', views.PomiarList.as_view()), # do zrobienia rediredct na tą stronę z 'api/pomiary'
    path('api/pomiary/<int:pk>/', views.PomiarDetail.as_view()),
    #==============https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
    path('api/logpomiarowe', views.logpomiar_list), # do zrobienia rediredct na tą stronę z 'api/pomiary'
    path('api/logpomiarowe/<int:pk>/', views.logpomiar_detail),#czemu pk?
    #============== https://www.django-rest-framework.org/tutorial/3-class-based-views/
    path('api/logadministracyjny', views.LogAdminList.as_view()),
    path('api/logadministracyjny/<int:pk>/', views.LogAdminDetail.as_view()),
    #============== http://127.0.0.1:8000/admin/api/seriapomiarowa/
    path('api/seriepomiarowe', views.SeriaPomiarowaList.as_view()),
    path('api/seriepomiarowe/<int:pk>/', views.SeriaPomiarowaDetail.as_view()),
    #============== https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)