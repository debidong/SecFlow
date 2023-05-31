from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .models import Forwarding

class MsgView(APIView):
    # implementation of forwarding msg
    def post(self, request):
        uid_from = request.data.get('uid_from')
        uid_to = request.data.get('uid_to')
        msg = request.data.get('msg')
