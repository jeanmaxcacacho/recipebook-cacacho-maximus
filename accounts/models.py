from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def bio_length(length_num):
    if value < 255: raise ValidationError("Bio should be at least 255 characters long.")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500, validators=[bio_length])


    def __str__(self):
        return self.name
