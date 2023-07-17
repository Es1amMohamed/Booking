from django.db import models

# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='home_page/')
    email = models.EmailField(max_length=254)
    image = models.ForeignKey('Image',related_name='home_page_image',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    address = ''
    fb_link = models.URLField(max_length=200)
    tw_link = models.URLField(max_length=200)
    in_link = models.URLField(max_length=200)
    map = ''
    
    def __str__(self):
        return self.site_name
 
 
 

class Image(models.Model):
   image = models.ImageField(upload_to='home_page/')
