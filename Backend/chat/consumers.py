from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from accounts.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        query_string = self.scope['query_string'].decode()
        params = dict(param.split('=') for param in query_string.split('&'))
        rid = params.get('rid')
        print(rid)
        chat_history = await self.get_chat_history(rid)
        print(chat_history)
        self.room_group_name = rid
        await self.accept()
        await self.send(text_data=chat_history)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        

        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.close()

    # Handle message
    async def receive(self, text_data):
        # await self.send(text_data=json.dumps(text_data))
        params = json.loads(text_data)
        print(params['content'])

        rid = params['rid']
        content = params['content']
        time = ""
        myUid = params['myUid']
        
        # users = await self.get_user(rid)
        time = await self.save_message(myUid, rid, content)
        message = {
            'rid': rid,
            'content': content,
            'time': time,
            'myUid': myUid
        }

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'broadcast',
            'message': message,
        })


    # Send message to room group
    async def broadcast(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))

    @database_sync_to_async
    def save_message(self, myUid, rid, content) -> str:
        room = Room.objects.get(rid=rid)
        me = User.objects.get(uid=myUid)
        message = Message(user=me, room=room, content=content, time="")
        message.save()
        return message.time.strftime("%Y-%m-%d %H:%M:%S")

    @database_sync_to_async
    def get_user(self, rid) -> list:
        room = Room.objects.get(rid=rid)
        users = room.users.all()

        ret = []
        for user in users:
            ret.append(user)
        return ret
    
    @database_sync_to_async
    def get_chat_history(self, rid) -> str:
        room = Room.objects.get(rid=rid)
        msgs = Message.objects.filter(room=room).order_by('time')
        chat_history = []
        for msg in msgs:
            temp = {
                'uid': msg.user.uid,
                'content': msg.content,
                'time': msg.time.strftime("%Y-%m-%d %H:%M:%S")
            }
            chat_history.append(temp)
        return json.dumps(chat_history)
