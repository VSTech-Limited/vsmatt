from django.db import models
import os
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# A Class called Team and Contact
# Team has a name, designation, photo, facebook link, twitter link, and a created date, email and phone number
# Contact has a name, email, phone number, message, and a created date
from account.models import Profile


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.first_name, ext)
    return os.path.join('uploads', 'JujaMall', 'team', "profile", filename)


class Team(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='team')
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=content_file_name)
    created_date = models.DateTimeField(auto_now_add=True)
    # added
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
