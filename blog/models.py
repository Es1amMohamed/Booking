from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, related_name="post_author", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to="post/")
    tag = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    residency_programme = models.TextField(max_length=10000)
    category = models.ForeignKey(
        "Category", related_name="post_category", on_delete=models.CASCADE
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
