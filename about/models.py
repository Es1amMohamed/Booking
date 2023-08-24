from django.db import models

# Create your models here.


class About(models.Model):
    image_1 = models.ImageField("about/")
    image_2 = models.ImageField("about/")
    comments = models.TextField(max_length=500)

    def __str__(self):
        return str(self.id)
