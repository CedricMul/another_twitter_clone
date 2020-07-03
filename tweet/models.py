from django.db import models
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    text = models.CharField(max_length=280)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='tweeted_user')
