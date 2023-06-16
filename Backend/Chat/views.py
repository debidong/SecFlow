# This file is used to implement dashboard. There are views for modules
# including UserList, Reminder

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import jwt
import utils
from Login.models import User
from .models import *
from .serializer import UserSerializer, InboxSerializer

# TokenView is used to handle the request for id check.
class TokenView(APIView):
    def get(self, request):
        # Input: token
        # Output: {uid, username}
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')

        if utils.exists(token['uid']) > 0:
            user = User.objects.all().get(uid=token['uid'])
            params = {
                'username': user.username,
                'uid': user.uid,
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
# ReminderView is used to handle the request for reminder module.
# When it's called, it will return a list of current reminders.
class ReminderView(APIView):
    def get(self, request):
        # Input: token
        # Output: reminder
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            user = User.objects.all().get(uid=token['uid'])
            reminders = Reminder.objects.filter(user=user)
            topics = []
            for reminder in reminders:
                topics.append(reminder.topic)
            params = {
                'reminder': topics
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

# This class is used to handle the request for reminder module.
# When it's called, it will add a reminder for the user.
class AddReminderView(APIView):
    def post(self, request):
        # Input: token, topic
        # Output: none
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            user = User.objects.all().get(uid=token['uid'])
            reminder = Reminder(topic=request.data.get('topic'), user=user)
            print(reminder.topic)
            reminder.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

# This class is used to handle the request for reminder module.
# When it's called, it will delete a reminder for the user.       
class DelReminderView(APIView):
    def post(self, request):
        # Input: token, topic
        # Output: none
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            topic = request.data.get('topic')
            reminders = Reminder.objects.filter(topic=topic)
            for reminder in reminders:
                reminder.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
# This class is used to handle the request for friend module.
class ListUsersView(APIView):
    def get(self, request):
        # Return a list of all users in database.
        # Input: token
        # Output: user
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            params = {
                'user': serializer.data
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    
    def post(self, request):
        # Select a user by its id.
        # Input: token, uid
        # Output: user
        # Status: 200 if the token is valid, 203 if the token is invalid
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            uid = request.data.get('uid')
            try:
                user = User.objects.all().get(uid=uid)
                if not user == None:
                    serializer = UserSerializer(user)
                    params = {
                        'user': serializer.data,
                    }
                    return Response(params, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

# This class is used to handle the request for friend module.
class FriendView(APIView):
    def post(self, request):
        # Send friend request to a user by its id.
        if utils.is_loggedin(request):
            sender_uid = utils.get_user_id(request=request)
            if sender_uid == request.data.get('user'):
                # Invaild: User is sending friend request to himself
                params = {
                    'status': 'false'
                }
                return Response(params, status=status.HTTP_400_BAD_REQUEST)
            else:
                sender = User.objects.all().get(uid=sender_uid)
                receiver = User.objects.all().get(uid=request.data.get('user'))
                try:
                    friendRequest = FriendRequest.objects.get(sender=sender, receiver=receiver)
                    # Invaild: User is sending friend request twice
                    params = {
                        'status': 'already sent'
                    }
                    return Response(params, status=status.HTTP_400_BAD_REQUEST)
                except:
                    friendRequest = FriendRequest(sender=sender, receiver=receiver)
                    friendRequest.save()
                    params = {
                        'status': 'true'
                    }
                    return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
class InboxView(APIView):
    def get(self, request):
        if utils.is_loggedin(request):
            user = utils.get_user(request=request)

            friend_requests = FriendRequest.objects.filter(receiver=user)
            requests = {}
            for i in friend_requests:
                requests.update({i.sender.uid: i.sender.username})
            params = {
                'inbox': {
                    'friend_requests': requests
                }
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
