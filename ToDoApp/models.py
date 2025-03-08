from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES=[
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    description=models.TextField(blank=True,null=True)
    due_date=models.DateField()
    priority=models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='Medium')
    created_at=models.DateTimeField(default=timezone.now)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

    