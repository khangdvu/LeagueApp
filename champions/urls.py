from django.urls import  path
from . import views

urlpatterns = [
    path('champions/', views.index, name = 'index'),
]
