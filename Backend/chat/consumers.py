from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        query_string = self.scope['query_string'].decode()
        params = dict(param.split('=') for param in query_string.split('&'))
        rid = params.get('rid')
        print(rid)
        

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
    # 处理接收到的消息
        params = json.loads(text_data)
        print(params['msg'])
        rid = params['rid']
        content = params['content']
        time = params['time']
        myUid = params['myUid']
        
        self.send(text_data=json.dumps({
            
        }))

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
