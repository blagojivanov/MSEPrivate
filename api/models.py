from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username + " " + self.email + " " + self.password
