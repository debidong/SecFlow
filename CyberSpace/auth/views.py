from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User

# # Create your views here.
# from django.http import HttpResponse

# def login(request):
#     return HttpResponse("Login.")

# def signup(request):
#     return HttpResponse("signup.")

class LoginView(APIView):
    def get(self):
        pass

class ListUsersView(APIView):
    def get(self):
        users = User.objects.all
        serializer = UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)