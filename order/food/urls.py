from django.urls import path
from . import views

urlpatterns = [
    path('list', views.GetFoods, name='list'),
    path('detail/<int:pk>', views.DetailFood, name='detail')
]