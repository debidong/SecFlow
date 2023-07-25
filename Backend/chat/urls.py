from django.urls import re_path, path
from .views import *
from . import consumers

# websocket_urlpatterns = [
#     # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
#     re_path('ws/chat', consumers.ChatConsumer.as_asgi()),
# ]

# /api/chat/
urlpatterns = [
    path('chatroom/<str:rid>', RoomView.as_view()),
    path('chatroom', RoomIdView.as_view())
]