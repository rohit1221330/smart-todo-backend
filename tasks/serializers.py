from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Token ke andar custom information (username) add karein
        token['username'] = user.username
        return token
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
        read_only_fields = ['user']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # Password ko extra secure banayein (taaki API response mein na dikhe)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Yeh function naya user banate waqt password ko hash (encrypt) kar dega
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['username'],
            password=validated_data['password']
        )
        return user