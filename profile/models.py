from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def avatar_user_path(instance, filename):
    return f'avatars/{instance.user.username}/{filename}'


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    pic = models.ImageField(upload_to=avatar_user_path, default='media/avatars/default/default.png')
    fb_url = models.CharField(max_length=100, blank=True)
    tw_url = models.CharField(max_length=100, blank=True)
    ig_url = models.CharField(max_length=100, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(_, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(_, instance,  **kwargs):
    instance.profile.save()
