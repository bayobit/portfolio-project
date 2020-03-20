from django.db import models

# Create your models here.
class Blog(models.Model):
    title =  models.CharField(max_length = 200)
    pubdate = models.DateTimeField(null = True, blank = True)
    body = models.TextField(default = 'DEFAULT VALUE', blank = True, null=True)
    image = models.ImageField(upload_to = 'images/')
    