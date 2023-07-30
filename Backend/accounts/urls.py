from .views import *
from django.urls import path

urlpatterns = [
    path('register', UserView.as_view()),
    path('register/code', CodeView.as_view()),
    path('', TokenView.as_view()),
    path('<str:uid>', TokenView.as_view())
]