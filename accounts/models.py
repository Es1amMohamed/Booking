from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def get_tokens_for_user(sender, **kwargs):
#     refresh = RefreshToken.for_user(User)

#     return {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     }
