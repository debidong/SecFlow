from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User

class UserView(APIView):
    # register
    def post(self, request):
        uid = request.data.get('uid')
        password = request.data.get('password')
        username = request.data.get('username')
        uid_check = User.objects.all().filter(uid=uid)
        if uid_check.exists():
            return Response({'status':'occupied'},status=status.HTTP_200_OK)
        else:
            new_user = User()
            new_user.set_user_info(username=username, password=password, uid=uid)
            new_user.save()
            return Response({'status':'true'},status=status.HTTP_200_OK)
    # login
    def get(self, request):
        uid = request.query_params['uid']
        password = request.query_params['password']
        login_check = User.objects.all().filter(uid=uid)
        print(uid)
        print(password)
        if not login_check.exists():
            return Response({'status':'user-not-exist'}, status=status.HTTP_200_OK)
        else:
            login_check = login_check.filter(password=password)
            if not login_check.exists():
                return Response({'status':'password-not-correct'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':'true'}, status=status.HTTP_200_OK)     

class ListUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
