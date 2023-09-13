from django.urls import path
from . import views

urlpatterns = [
    path('', views.json_sorting, name='json_sorting'),
]
