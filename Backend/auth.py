import jwt
import time
from config import JWT_KEY
from utils import exists, set, get

from rest_framework.response import Response
from rest_framework import status

from accounts.models import User

TOKEN_EXPIRED = 10*60*60 # 1 hour

def is_loggedin(func):
    def check_token(self, request, *args, **kargs):
        try:
            token_from_request = jwt.decode(request.headers['token'], algorithms='HS256', key=JWT_KEY)
            token_from_db = jwt.decode(get(token_from_request['uid']), algorithms='HS256', key=JWT_KEY)
            if token_from_request == token_from_db:
                return func(self, request, *args, **kargs)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return check_token

def create_token(uid: str) -> str:
    if User.exists(uid):
        payload = {
            'uid': uid,
            'last-login': int(time.time())
        }
        token = jwt.encode(payload=payload, key=JWT_KEY, algorithm="HS256")
        set(uid, token, ex=TOKEN_EXPIRED)
        return token
    else:
        return ""
