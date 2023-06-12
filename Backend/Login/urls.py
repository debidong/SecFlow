from .views import *
from django.urls import path

urlpatterns = [
    path('register', UserView.as_view(), name='post'),
    path('', TokenView.as_view())
]