import redis

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
