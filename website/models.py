from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    birth = models.DateField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Comments(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200]+'...'