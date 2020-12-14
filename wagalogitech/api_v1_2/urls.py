from django.urls import path, include
from . import views
from .apps import ApiV12Config

app_name = ApiV12Config.name
urlpatterns = [
    path('', views.view_api_v1_2, name="api_v1_2_root"),
]
