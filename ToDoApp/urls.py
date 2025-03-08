from django.urls import path
from .views import *
urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskEditDelete.as_view(), name='task-detail'),
]
