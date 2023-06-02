from django.db import models
from django.contrib.auth.models import 
# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User)
    bio = models.TextField(blank=True, max_length=255)
    location= models.CharField(max_length=255)

    def __str__(self):
        return self.User
    