from django.urls import path, include
from . import views
#router = DefaultRouter()
#router.register(r'main', views.FrontViewSet)

urlpatterns = [
    path('front_root', views.front_root, name='front_root'),
    path('kokpit', views.kokpit, name="kokpit"),
    path('', views.kokpit, name="login"),
    path('organizacje/', views.organizacje, name="organizacje"),
    path('organizacje/<int:organizacja_id>', views.organizacja_detail, name="organizacja_detail"),
    path('organizacje/nowy', views.organizacje_nowy, name="organizacje_nowy"),
    path('organizacje/data/arrays.txt', views.data_arrays, name="data_arrays.txt"),
    path('pomiary/', views.pomiary, name="pomiary"),
    path('pomiary/<int:pomiar_id>', views.pomiary_detail, name="pomiary"),
    path('pomiary/nowy', views.pomiary_nowy, name="pomiary_nowy"),
    path('leftPanel', views.leftPanel, name="leftPanel"),
    path('przyklad', views.przyklad, name="przyklad"),
]