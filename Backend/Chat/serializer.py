from rest_framework import serializers
from Login.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'uid']
        # fields = '__all__'