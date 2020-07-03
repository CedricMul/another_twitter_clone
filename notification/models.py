from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='notify_user')
