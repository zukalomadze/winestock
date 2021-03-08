from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from wine import views

router = DefaultRouter()
router.register(r'wine', views.WineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
