from .views import *
from django.urls import include, path

urlpatterns = [
    path('register', UserView.as_view(), name='post'),
    path('', UserView.as_view(), name='get')
]