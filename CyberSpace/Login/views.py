from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User

class UserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        uid = request.data.get('uid')
        
        new_user = User()
        new_user.set_user_info(username=username, password=password, uid=uid)
        new_user.save()

        return Response({'status':'true'},status=status.HTTP_200_OK)
    def get(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        login = User(username=username, password=password)
        if login != None:
            return Response({'status':'true'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'false'}, status=status.HTTP_401_UNAUTHORIZED)        

class ListUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
