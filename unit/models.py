from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=100, unique= True)
    image = models.ImageField(upload_to='unit/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place',related_name='unit_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='unit_category',on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null= True, blank= True)
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
       
        super(Unit, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("unit:unit_detail", kwargs={"slug": self.slug})
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class UnitBook(models.Model):
    user = models.ForeignKey(User,related_name='book_owner',on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,related_name='book_unit',on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    adults = models.IntegerField()
    children = models.IntegerField()
    
    def __str__(self):
        return str(self.unit)
    
    