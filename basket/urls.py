from django.urls import path
from basket import views

urlpatterns = [
    path('basket/<int:pk>', views.BasketDetail.as_view(), name='register'),
]