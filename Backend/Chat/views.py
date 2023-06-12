from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import jwt
import utils
from Login.models import User
from .models import *
from .serializer import UserSerializer

# dashboard
class TokenView(APIView):
    # token -> user info
    def get(self, request):
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
        
class ReminderView(APIView):
    def get(self, request):
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            user = User.objects.all().get(uid=token['uid'])
            reminders = Reminder.objects.filter(user=user)
            topics = []
            for reminder in reminders:
                print(reminder.topic)
                topics.append(reminder.topic)
            params = {
                'reminder': topics
            }
            return Response(params, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
class AddReminderView(APIView):
    def post(self, request):
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
        
class DelReminderView(APIView):
    def post(self, request):
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
        
class ListUsersView(APIView):
    def get(self, request):
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
        token = request.headers['token']
        token = jwt.decode(token, algorithms='HS256', key='secret')
        if utils.exists(token['uid']) > 0:
            uid = request.data.get('uid')
            try:
                user = User.objects.all().get(uid=uid)
                if not user == None:
                    serializer = UserSerializer(user)
                    params = {
                        'user': serializer.data
                    }
                    return Response(params, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)