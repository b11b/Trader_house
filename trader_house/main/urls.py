from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('help', views.help)
]