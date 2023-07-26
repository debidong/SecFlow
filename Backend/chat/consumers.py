from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from accounts.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        query_string = self.scope['query_string'].decode()
        params = dict(param.split('=') for param in query_string.split('&'))
        rid = params.get('rid')
        print(rid)
        

    def disconnect(self, close_code):
        self.close()

    # Handle the message
    async def receive(self, text_data):
        await self.send(text_data=json.dumps(text_data))
        params = json.loads(text_data)
        print(params['content'])
        rid = params['rid']
        content = params['content']
        time = params['time']
        myUid = params['myUid']
        
        user = await self.get_user(myUid)
        await self.save_message(user, rid, content, time)

    async def chat_message(self, event):
        # 发送消息给客户端
        message = event['message']

        await self.send(text_data=message)

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         # 处理接收到的消息
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': text_data
#             }
#         )

#     async def chat_message(self, event):
#         # 发送消息给客户端
#         message = event['message']

#         await self.send(text_data=message)

    @database_sync_to_async
    def save_message(self, user, rid, content, time):
        room = Room.objects.get(rid=rid)
        message = Message(user=user, room=room, content=content, time=time)
        message.save()

    @database_sync_to_async
    def get_user(self, myUid):
        return User.objects.get(uid=myUid)
