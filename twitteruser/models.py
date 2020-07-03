from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    name = models.CharField(
        max_length=30,
        null=True,
        blank=True
        )
    following = models.ManyToManyField(
        'TwitterUser',
        symmetrical=False,
        related_name='following_user'
        )
    def __str__(self):
        return self.name
