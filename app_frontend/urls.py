# app_frontend/urls.py
from django.urls import path
from .views import index, functions

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('functions/', functions, name='functions'),

]