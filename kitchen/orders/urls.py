from django.urls import path
from . import views

urlpatterns = [
    path('list', views.store_order, name='store'),
    path('db', views.check, name='db'),
    path('detail/<int:pk>', views.detail, name='detail')
]