from django.urls import path
from .views import *

# /api/chat/
urlpatterns = [
    path('chatroom/<str:rid>', RoomView.as_view()),
    path('chatroom', RoomIdView.as_view())
]