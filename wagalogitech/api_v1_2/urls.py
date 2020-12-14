from django.urls import path, include
from . import views
from . import ApiV12Config

apps_name = ApiV12Config
urlpatterns = [
    path('', views.view_api_v1_2, name="api_v1_2_root"),
]
