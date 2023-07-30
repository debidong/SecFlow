import redis
import jwt
from accounts.models import User
from config import JWT_KEY

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def set(key: str, value:str, **kwargs):
    if 'ex' in kwargs:
        redis_client.set(key,value,ex=kwargs['ex'])
    else:
        redis_client.set(key,value)

def get(key:str) -> str:
    return redis_client.get(key).decode()

def delete(key:str):
    redis_client.delete(key)

def exists(key:str):
    return redis_client.exists(key)

def keys():
    return redis_client.keys('*')
    
def get_uid_from_token(request) -> str:
    token = request.headers['token']
    token = jwt.decode(token, algorithms='HS256', key=JWT_KEY)
    return token['uid']

def get_user_from_token(request) -> User:
    token = request.headers['token']
    token = jwt.decode(token, algorithms='HS256', key=JWT_KEY)
    return User.objects.get(uid=token['uid'])