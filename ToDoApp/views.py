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
    def list(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=self.get_serializer(queryset,many=True)
        if queryset.exists():
            return custom200("✅ Data retrieved successfully",serializer.data)
        else:
            return custom404(request,serializer.errors)
    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return custom200("✅ Task created successfully",serializer.data)
        else:
            return custom404(request,serializer.errors)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class TaskEditDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return custom200("✅ Task retrieved successfully",serializer.data)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return custom200("✅ Task updated successfully", serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return custom200("✅ Task deleted successfully")