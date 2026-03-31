from datetime import timezone

from django.db import models

# Create your models here.
class Message(models.Model):
    sender=models.CharField(max_length=156)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.sender}:{self.message[:]}"
