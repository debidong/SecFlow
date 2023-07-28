import jwt
from utils import exists, set
from rest_framework.response import Response
from rest_framework import status
import time

SALT = "178wqesd46312fas"
TOKEN_EXPIRED = 10








def is_loggedin(func):
    def wrapper(self, request, *args, **kargs):
        try:
            token = request.headers['token']
            token = jwt.decode(token, algorithms='HS256', key='secret')
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        if exists(token['uid']) > 0:
            return func(self, request, *args, **kargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return wrapper

def create_token(uid: str):
    payload = {
        'uid': uid,
        'exp': int(TOKEN_EXPIRED+time.time())
    }
    token = jwt.encode(payload=payload, key=SALT, algorithm="HS256")
    headers = {
        'token': token,
        'access-control-expose-headers': 'token'
    }
    set(uid, 'logged')
    return Response(status=status.HTTP_200_OK, headers=headers)