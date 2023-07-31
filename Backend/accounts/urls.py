from .views import *
from django.urls import path

# /api/accounts/
urlpatterns = [
    path('register', UserView.as_view()),
    path('register/code', CodeView.as_view()),
    path('', TokenView.as_view()),
    path('<str:uid>', UserView.as_view())
]