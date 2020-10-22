from django.urls import path, include
from .views import FrontViewSet

router = DefaultRouter()
router.register(r'main', views.FrontViewSet)

urlpatterns = [
    path('front/', include(router.urls)),
]