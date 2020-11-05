from django.urls import path, include
from . import views
#router = DefaultRouter()
#router.register(r'main', views.FrontViewSet)

urlpatterns = [
    path('front_root', views.front_root, name='front_root'),
    path('home', views.home, name="login"),
    path('', views.home, name="login"),
    path('organizacje/', views.organizacje, name="organizacje"),
    path('organizacje/<int:organizacja_id>', views.organizacja_detail, name="organizacja_detail"),
    path('pomiary/', views.pomiary, name="pomiary"),
#    path('post/ajax/pomiar', postPomiar, name="post_pomiar"),
    path('pomiary/<int:pomiary_id>', views.pomiary_detail, name="pomiary"),
    path('upperPanel', views.upperPanel, name="upperPanel")
]