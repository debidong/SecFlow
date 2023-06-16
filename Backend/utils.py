import redis
import jwt
from Login.models import User

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def set(key: str, value:str):
    redis_client.set(key,value)

def get(key:str):
    return redis_client.get(key)

def delete(key:str):
    redis_client.delete(key)

def exists(key:str):
    return redis_client.exists(key)

def keys():
    return redis_client.keys('*')

def is_loggedin(request) -> bool:
    token = request.headers['token']
    token = jwt.decode(token, algorithms='HS256', key='secret')
    if exists(token['uid']) > 0:
        return True
    else:
        return False
    
def get_user_id(request) -> str:
    token = request.headers['token']
    token = jwt.decode(token, algorithms='HS256', key='secret')
    return token['uid']

def get_user(request) -> User:
    token = request.headers['token']
    token = jwt.decode(token, algorithms='HS256', key='secret')
    return User.objects.get(uid=token['uid'])