from django.db import models

# Create your models here.
# A Class called Team and Contact
# Team has a name, designation, photo, facebook link, twitter link, and a created date, email and phone number
# Contact has a name, email, phone number, message, and a created date

class Team(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/')
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

class Contact(models.Model):
    pass
