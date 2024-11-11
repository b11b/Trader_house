from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('user/', UserCreate.as_view(), name='user-create')
]