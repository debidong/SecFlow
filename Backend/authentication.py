
import jwt
from utils import exists
from rest_framework.response import Response
from rest_framework import status

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