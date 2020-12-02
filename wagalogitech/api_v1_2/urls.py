from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_api_v1_2, name="api_v1_2_root"),
]
