from rest_framework import viewsets, generics
from .models import Task
from .serializers import TaskSerializer, UserSerializer, MyTokenObtainPairSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny  # Naya import
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView 


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Permission add kiya

    def get_queryset(self):
        """
        Yeh view sirf usi user ke tasks return karega jo logged in hai.
        """
        return self.request.user.tasks.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Jab koi naya task banega, toh use current user ke naam par save karega.
        """
        serializer.save(user=self.request.user)
        
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Taaki bina login ke bhi koi is view ko access kar sake
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer