from django.conf import settings
from django.db import models
from django.forms import DateTimeField

from user.models import User



class Todo(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return self.content