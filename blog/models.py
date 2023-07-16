from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    tag = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    residency_programme = models.TextField(max_length=10000)
    category = models.ForeignKey('Category',related_name='post_category',on_delete=models.CASCADE)
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name