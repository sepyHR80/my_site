from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post(models.Model):
    #image
    #author  
    title = models.CharField(max_length =255)
    content = models.TextField()
    #tag
    #category
    counted_views = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    publish_date = models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)