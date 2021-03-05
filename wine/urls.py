from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from wine import views

urlpatterns = [
    path('wine/', views.WineList.as_view(), name='wine list'),
    path('wine/<int:pk>', views.WineDetail.as_view(), name='wine detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)