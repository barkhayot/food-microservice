from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data', views.get_data, name='data')
]