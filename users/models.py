from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
# Create your models here.
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Language, GENDER_CHOICES


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.first_name, ext)
    return os.path.join('uploads', 'users', "profile", filename)


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = ResizedImageField(
        default=os.path.join("uploads", "profile", "default.jpg"),
        upload_to=content_file_name,
        blank=True,
        size=[500, 500]
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True)
    dob = models.DateField(null=True, blank=True)
    github_url = models.URLField(max_length=300, blank=True, null=True)
    linkedin_url = models.URLField(max_length=300, blank=True, null=True)
    facebook_url = models.URLField(max_length=300, null=True, blank=True)
    twitter_url = models.URLField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
