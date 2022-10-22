from turtle import title
from django.db import models
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

LANGUAGE_CHOICES = (
    ('English', 'English'),
    ('Swahili', 'Swahili'),
    ('Dholuo', 'Dholuo'),
    ('Kikuyu', 'Kikuyu'),
    ('Kamba', 'Kamba'),
    ('Ekegusii', 'Ekegusii'),
    ('Kalenjin', 'Kalenjin'),
    ('Kimiiru', 'Kimiiru'),
    ('Oluluhyia', 'Oluluhyia'),
    ('Kipokomo', 'Kipokomo'),
    ('Kigiryama', 'Kigiryama'),
    ('Kiembu', 'Kiembu'),
    ('Kalenjin', 'Kalenjin'),
    ('Maasai', 'Maasai'),
    ('Turkana', 'Turkana'),
    ('Rendille', 'Rendille'),
    ('Somali', 'Somali'),
)
GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)
# Create your models here.
# A Class called Team and Contact
# Team has a name, position, photo, facebook link, twitter link, and a created date, email and phone number
# Contact has a name, email, phone number, message, and a created date
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.first_name, ext)
    return os.path.join('uploads', 'JujaMall', 'team', "profile", filename)


class Team(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Language(models.Model):
    name = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_pic = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    github_link = models.URLField(max_length=300, blank=True, null=True)
    linked_in_link = models.URLField(max_length=300, blank=True, null=True)
    facebook_link = models.URLField(max_length=300, null=True, blank=True)
    twitter_link = models.URLField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='category_author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('title',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Testimony(models.Model):
    user = models.ForeignKey('auth.User', related_name="user_testimony", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

