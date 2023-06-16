from rest_framework import serializers
from Login.models import User
from .models import FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'uid']
        # fields = '__all__'

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver', 'accepted']
                  