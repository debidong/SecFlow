from django.db import models
from queue import Queue

class Forwarding(models.Model):
    msg_queue1 = Queue(maxsize=50)
    msg_queue2 = Queue(maxsize=50)
    session = models.CharField

    def set_session(self, session: str):
        self.session = session

    def msg_in(self, msg_queue:Queue):
        try:
            if msg_queue.full:
                return {'status':'False', 'error':'bufferfull'}
            else:
                msg_queue.put()
        except:
            return {'status':'False', 'error':'unknownerror'}
    
    def msg_out(self, msg_queue:Queue):
        try:
            if msg_queue.empty:
                return {'status':'False', 'error':'bufferempty'}
            else:
                msg_queue.get()
        except:
            return {'status':'False', 'error':'unknownerror'}
        
class History(models.Model):
    pass
