# This file is  implement dashboard. There are views for modules
# including UserList, Reminder

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import utils
from auth import is_loggedin
from accounts.models import User
from .models import *
from .serializer import UserSerializer, InboxSerializer
# 
# All APIs receive request with TOKEN as header
# 


class InfoView(APIView):
    @is_loggedin
    def get(self, request):
        try:
        # Return current user info.
            user = utils.get_user_from_token(request)
            params = {
                'username': user.username,
                'uid': user.uid
            }
            return Response(params, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
# Handle the request for reminder module.
class ReminderView(APIView):
    @is_loggedin
    def get(self, request):
        # Return all reminders which match the user in database.
        try:
            user = utils.get_user_from_token(request)
            reminders = Reminder.objects.filter(user=user)
            topics = []
            for reminder in reminders:
                topics.append(reminder.topic)
            params = {
                'reminder': topics
            }
            return Response(params, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @is_loggedin
    def post(self, request):
        # Add or delete a reminder with matched user.
        try:
            topic = request.data.get('topic')
            print(topic)
            user = utils.get_user_from_token(request)
            action = request.data.get('action')
            if action == 'add':
                assert topic != None
                reminder = Reminder(topic=topic, user=user)
                reminder.save()
                return Response(status=status.HTTP_200_OK)
            elif action == 'delete':
                # Maybe there are many reminders with the same topic
                reminders = Reminder.objects.filter(topic=topic)
                for reminder in reminders:
                    reminder.delete()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        
# Handle the request for userList.
class ListUsersView(APIView):
    @is_loggedin
    def get(self, request):
        # Return all registered users.
        # Abandoned method, seldom called.
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            params = {
                'user': serializer.data
            }
            return Response(params, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @is_loggedin
    def post(self, request):
        # Search a user by its uid and return the user.
        try:
            uid = request.data.get('uid')
            try:
                user = User.objects.get(uid=uid)
                if not user == None:
                    serializer = UserSerializer(user)
                    params = {
                        'user': serializer.data,
                    }
                    return Response(params, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Handle friend requests.
class FriendRequestView(APIView):
    @is_loggedin
    def post(self, request):
        # Send friend request to a user by its id.
        try:
            sender_uid = utils.get_uid_from_token(request=request)
            if sender_uid == request.data.get('user'):
                # Invaild: User is sending friend request to himself
                params = {
                    'status': 'false'
                }
                return Response(params, status=status.HTTP_400_BAD_REQUEST)
            else:
                sender = User.objects.get(uid=sender_uid)
                receiver = User.objects.get(uid=request.data.get('user'))
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
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Handle the request of friend request management.
class FriendRequestStatusView(APIView):
    @is_loggedin
    def post(self, request):
        # Agree or refuse a friend request.
        # Receive FR sender and anwser from request.
        try:
                anwser = request.data.get('anwser')
                sender = User.objects.get(uid=request.data.get('sender'))
                receiver = utils.get_user_from_token(request)
                if anwser == 'agree':
                    FriendRequest.objects.get(sender=sender).delete()
                    sender.friend.add(receiver)
                    receiver.friend.add(sender)
                elif anwser == 'refuse':
                    FriendRequest.objects.get(sender=sender).delete()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# Handle the request for Inbox module.
class InboxView(APIView):
    @is_loggedin
    def get(self, request):
        # Return friend requests.
        try:
            user = utils.get_user_from_token(request=request)

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
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Handle the request for friend module.
class FriendView(APIView):
    @is_loggedin
    def get(self, request):
        # Return all friends of current user.
        try:
            user = utils.get_user_from_token(request=request)
            friends = user.friend.all()
            serializer = UserSerializer(friends, many=True)
            params = {
                'friends': serializer.data
            }
            return Response(params, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)