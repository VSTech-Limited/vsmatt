from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
# Create your models here.
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.first_name, ext)
    return os.path.join('uploads', 'users', "profile", filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    image = ResizedImageField(
        default=os.path.join("uploads", "profile", "default.jpg"),
        upload_to=content_file_name,
        blank=True,
        size=[500, 500]
    )
    phone = PhoneNumberField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile...'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
