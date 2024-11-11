from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('help', views.help),
    path('tavern', views.index)
]