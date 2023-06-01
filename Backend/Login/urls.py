from .views import *
from django.urls import include, path

urlpatterns = [
    path('register', UserView.as_view(), name='post'),
    path('', TokenView.as_view()),
    path('userList', ListUsersView.as_view())
]