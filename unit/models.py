from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='unit/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place',related_name='unit_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='unit_category',on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
count = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)
class UnitBook(models.Model):
    user = models.ForeignKey(User,related_name='book_owner',on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,related_name='book_unit',on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    adults = models.IntegerField(choices=count)
    children = models.IntegerField(choices=count)
    
    def __str__(self):
        return str(self.unit)