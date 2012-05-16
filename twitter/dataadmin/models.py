# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from tweetsmodel import TweetsManager

class Tweets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=450)
    screen_name = models.CharField(max_length=765)
    followers_count = models.IntegerField()
    created_at = models.DateTimeField()
    objects = models.Manager()
    tweet = TweetsManager()
    class Meta:
        db_table = u'tweets'
        
class Tweetsiphone(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=450)
    screen_name = models.CharField(max_length=765)
    followers_count = models.IntegerField()
    created_at = models.DateTimeField()
    objects = models.Manager()
    tweet = TweetsManager()
    class Meta:
        db_table = u'tweetsiphone'

