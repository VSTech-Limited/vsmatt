from django.db import models
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django_resized import ResizedImageField

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
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
CATEGORY_IMAGES_PATH = os.path.join("uploads", "shop", "category")
MARKER_IMAGES_PATH = os.path.join("uploads", "shop", "category", "marker")


# Create your models here.
# A Class called Team and Contact
# Team has a name, position, photo, facebook link, twitter link, and a created date, email and phone number
# Contact has a name, email, phone number, message, and a created date
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.first_name, ext)
    return os.path.join('uploads', 'JujaMall', 'team', "profile", filename)


def category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(CATEGORY_IMAGES_PATH, filename)


def markers_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(MARKER_IMAGES_PATH, filename)


class Team(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to=content_file_name)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Language(models.Model):
    name = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_addressed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = ResizedImageField(
        upload_to=category_file_name,
        blank=True,
        null=True,
        size=[100, 100]
    )
    created_by = models.ForeignKey('auth.User', related_name='category_author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Testimony(models.Model):
    user = models.ForeignKey('auth.User', related_name="user_testimony", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.description


# containes general information
class JujaMall(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='uploads/jujamall/logo', blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=256)
    set_current = models.BooleanField(default=False)
