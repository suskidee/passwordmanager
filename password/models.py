from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class New(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


