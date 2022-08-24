from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(max_length=255, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')