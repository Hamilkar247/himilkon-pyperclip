from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PomiarViewSet, UserViewSet, api_root
from django.shortcuts import redirect
from django.views.generic import RedirectView

pomiar_list = PomiarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

pomiar_detail = PomiarViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})

pomiar_list = UserViewSet.as_view({
    'get': 'list'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('api/', api_root),
    path('api/pomiary/', pomiar_list, name="pomiar-list"),
    path('api/pomiary/<int:pk>/', pomiar_detail, name="pomiar-detail"),
    path('api/users/', user_list, name='user-list'),
    path('api/users/<int:pk>/', user_detail, name='user-detail')
])

#urlpatterns = [
#    path('jednostkiOrganizacyjne/', views.jednostka.as_view()),
#    #path('jednostkaOrganizacyjna/<int:id_jednostki>/', views.JednostkaOrganizacyjnaPojedynczy.as_view()),
#    #path('uzytkownicy/<str:uzytkownik_login>/', views.Uzytkownik.as_view()),
#    #path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna, name=""),
#    #path('users/', ListCreateAPIView.as_view(queryset=Uzytkownik.objects.all()
#    #, serializer_class=UzytkownikSerializer), name='user-list')
#    path('response_jednostkaOrganizacyjna/<int:jednostkaOrganizacyjna_id>/', views.response_jednostkaOrganizacyjna),
#    #===========https://www.django-rest-framework.org/tutorial/3-class-based-views/
#    path('api/pomiary/', views.PomiarList.as_view(),
#       name='pomiar-list'), # do zrobienia rediredct na tą stronę z 'api/pomiary'
#    path('api/pomiary/<int:pk>/', views.PomiarDetail.as_view(),
#       name='pomiar-detail'),
#    #==============https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
#    path('api/logpomiarowe', views.logpomiar_list), # do zrobienia rediredct na tą stronę z 'api/pomiary'
#    path('api/logpomiarowe/<int:pk>/', views.logpomiar_detail),#czemu pk?
#    #============== https://www.django-rest-framework.org/tutorial/3-class-based-views/
#    path('api/logadministracyjny', views.LogAdminList.as_view()),
#    path('api/logadministracyjny/<int:pk>/', views.LogAdminDetail.as_view()),
#    #============== http://127.0.0.1:8000/admin/api/seriapomiarowa/
#    path('api/seriepomiarowe', views.SeriaPomiarowaList.as_view()),
#    path('api/seriepomiarowe/<int:pk>/', views.SeriaPomiarowaDetail.as_view()),
#    #============== https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
#    path('api/users/', views.UserList.as_view(),
#       name='user-list'),
#    path('api/users/<int:pk>/', views.UserDetail.as_view(),
#       name='user-detail'),
#    #==========
#    path('api/', views.api_root)
#]
