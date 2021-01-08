from django.urls import path

from . import views

urlpatterns = [
    path('', views.champions, name='champions'),
]
