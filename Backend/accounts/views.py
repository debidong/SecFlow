# Handle request for accounts, including registration, login, logout, and deletion

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import User
from chat.models import Room, Message
from dashboard.models import Reminder, FriendRequest

import jwt
import utils
from auth import is_loggedin
from auth import create_token

from .mail import send_email, get_random_code


# Handle request for code for email verification
class CodeView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if utils.exists(email):
            return Response({'status':'too-many-requests'},status=status.HTTP_400_BAD_REQUEST)
        code = get_random_code()
        utils.set(email, code, ex=300)
        ret = send_email(email, "auth-code" ,{'code': code})
        if ret == True:
            return Response({'status': 'true'},status=status.HTTP_200_OK)
        else:
            return Response({'status': 'email-error'},status=status.HTTP_400_BAD_REQUEST)

# Handle request for accounts
class UserView(APIView):
    # Create a new account
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        uid = request.data.get('uid')
        password = request.data.get('password')
        username = request.data.get('username')
        # Already exists an account with this email
        if User.objects.filter(email=email).exists():
            return Response({'status':'occupied'},status=status.HTTP_400_BAD_REQUEST)
        if not User.exists(uid):
            if utils.exists(email) and utils.get(email) == code:    
                user = User(email=email, uid=uid, username=username)
                user.set_password(password)
                user.save()
                return Response({'status':'true'},status=status.HTTP_200_OK)
            # else, code is incorrect
            return Response({'status':'code-error'},status=status.HTTP_400_BAD_REQUEST)
        # else, account with this uid already exists
        return Response({'status':'occupied'},status=status.HTTP_400_BAD_REQUEST)
    
    # Delete account
    @is_loggedin
    def delete(self, request, uid):
        uid_ = utils.get_uid_from_token(request)
        
        # If someone tries to delete someone else's account
        if uid_ != uid:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if User.exists(uid=uid):
            user = User.objects.get(uid=uid)
            Room.objects.filter(users=user).delete()
            Message.objects.filter(user=user).delete()
            Reminder.objects.filter(user=user).delete()


            
            FriendRequest.objects.filter(sender=user).delete()
            FriendRequest.objects.filter(receiver=user).delete()
            User.objects.get(uid=uid).delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Handle request for login
class TokenView(APIView):

    # Handle request for login
    # Return a token for authentication,
    # if the user exists and the password is correct
    def post(self, request):
        password = request.data.get('password')
        uid: str = request.data.get('uid')            
        if User.exists(uid):
            if User.check_password(uid=uid, password=password):
                if utils.exists(uid) > 0:
                    token = utils.get(uid)
                else:
                    token = create_token(uid)
                headers = {
                    'token': token,
                    'access-control-expose-headers': 'token'
                }
                return Response(status=status.HTTP_200_OK, headers=headers)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Handle request for logout
    @is_loggedin
    def delete(self, request, uid):
        uid_ = utils.get_uid_from_token(request)
        if uid_ == uid:
            utils.delete(uid)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
                
