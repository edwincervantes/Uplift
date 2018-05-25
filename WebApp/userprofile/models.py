from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateJoined = models.DateField(default=date.today)
    daysClean = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)

def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


