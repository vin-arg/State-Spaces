from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
# Create your models here.
