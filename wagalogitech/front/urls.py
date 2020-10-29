from django.urls import path, include
from . import views
#router = DefaultRouter()
#router.register(r'main', views.FrontViewSet)

urlpatterns = [
    path('front_root', views.front_root, name='front_root'),
    path('home', views.home, name="login"),
    path('', views.home, name="login"),
    path('organizacje/', views.organizacje, name="organizacje"),
    path('organizacje/<int:organizacja_id>', views.szczegoly, name="organizacje")
]