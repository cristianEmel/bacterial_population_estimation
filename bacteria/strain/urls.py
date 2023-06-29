from django.urls import path

from .views import population, StrainViewSet
from django.urls import re_path as url

urlpatterns = [
    path("count_replication/", population, name="count_replication"),
    path('strains/', StrainViewSet.as_view({'get': 'list', 'post': 'create'}), name='strain-list'),
    path('strains/<int:pk>/', StrainViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='strain-detail'),
]