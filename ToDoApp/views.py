from django.shortcuts import render
from .mixins import*
from rest_framework.views import APIView
from .models import*
from .serializers import*
from rest_framework import generics,permissions
# Create your views here.
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Simply return the queryset for the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This method is called when creating a new Task
        serializer.save(user=self.request.user)

class TaskEditDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)