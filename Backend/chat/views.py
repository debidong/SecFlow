from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from accounts.models import User
from authentication import is_loggedin
import random

class SKeyView(APIView):
    # Check the secret key
    def post(self, request):
        pass

class RoomIdView(APIView):
    # Create a room
    @is_loggedin
    def post(self, request):
        # Get the user of friend & me
        # try:
        friend = User.objects.get(uid=request.data.get('uid'))
        me = User.objects.get(uid=request.data.get('myUid'))
        room = Room.objects.filter(users=friend).filter(users=me)
        if room.exists():
            room = room.get()
            params = {
                'rid': room.rid,
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            # Chatroom doesn't exist, creating a new one
            rid = str(random.randint(0,1125899906842624))
            room = Room(rid=rid)
            room.save()
            room.users.add(friend, me)
            

            params = {
                'rid': rid
            }
            print('Chatroom created: ' + rid)
            return Response(params, status=status.HTTP_201_CREATED)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    # Join in a room
    @is_loggedin
    def get(self, request):
        pass

    # Delete a room
    @is_loggedin
    def delete(self, request, rid):
        try:
            room = Room.objects.get(rid=rid)
            if room:
                room.delete()
                print('Chatroom deleted: ' + rid)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)