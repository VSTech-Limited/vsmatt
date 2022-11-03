from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django_resized import ResizedImageField
import os

BS_CATEGORY_IMAGES_PATH = os.path.join("uploads", "shop", "category", 'business')
MARKER_IMAGES_PATH = os.path.join("uploads", "shop", "category", "marker")
BUSINESS_IMAGES_PATH = os.path.join("uploads", "shop", "business")


def bs_category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BS_CATEGORY_IMAGES_PATH, filename)


def markers_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(MARKER_IMAGES_PATH, filename)


def business_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.name, 'main', filename)


def business_branch_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.business.name, 'branch', filename)


class BusinessCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = ResizedImageField(
        upload_to=bs_category_file_name,
        blank=True,
        null=True,
        size=[100, 100]
    )
    marker = models.ImageField(upload_to=markers_file_name, blank=True, null=True)
    created_by = models.ForeignKey('auth.User', related_name='business_category_author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'Business Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('business:category', args=[self.slug])


class BusinessProfile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    image = ResizedImageField(
        upload_to=business_file_name,
        blank=True,
        null=True,
        size=[500, 500]
    )

    def get_absolute_url(self):
        return reverse(
            'business:own_business_detailed',
            args=[self.slug]
        )

    def __str__(self):
        return self.name

    def geolocation(self):
        return f"{self.latitude}, {self.longitude}"


class BusinessBranch(models.Model):
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name="branch")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BusinessCategory, related_name='businesses', on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    image = ResizedImageField(
        upload_to=business_branch_file_name,
        blank=True,
        null=True,
        size=[500, 500]
    )
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def geolocation(self):
        return f"{self.latitude}, {self.longitude}"
