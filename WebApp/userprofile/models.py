from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daysClean = models.IntegerField(default=0)
    #supporting = ArrayField(models.CharField(max_length=500, blank=True))
    securityQuestion1 = models.CharField(max_length=500)
    securityQuestion2 = models.CharField(max_length=500)
    securityAnswer1 = models.CharField(max_length=500)
    securityAnswer2 = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()