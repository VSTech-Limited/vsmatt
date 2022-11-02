from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
from django.urls import reverse
from django_resized import ResizedImageField

from business.models import BUSINESS_IMAGES_PATH, BusinessBranch

PRODUCTS_IMAGES_PATH = os.path.join("uploads", "shop", "products", "primary")
PRODUCTS_SECONDARY_IMAGES_PATH = os.path.join("uploads", "shop", "products", "secondary")
CATEGORY_IMAGES_PATH = os.path.join("uploads", "shop", "category", 'Product')
RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]


def category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    return os.path.join(CATEGORY_IMAGES_PATH, filename)


def product_secondary_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.product.branch.slug, instance.id, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.product.business.name, "branch", 'products', 'secondary',
                        filename)


def product_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.slug, instance.id, instance.category.slug, ext)
    return os.path.join(BUSINESS_IMAGES_PATH, instance.branch.name, 'branch', 'products', 'primary', filename)


class ProductCategory(models.Model):
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
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    tags = models.ManyToManyField('core.Tag', related_name="products", blank=True)
    branch = models.ManyToManyField(BusinessBranch, related_name='products', blank=True)
    image = ResizedImageField(
        upload_to=product_file_name,
        blank=True,
        null=True,
        size=[500, 500]
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=4
    )

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_discount(self, rate=25):
        return "%.2f" % (self.price * Decimal((100 + rate) / 100))

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.id, self.slug]
        )

    def iter_full_stars(self) -> range:
        return range(int(str(self.rating)))

    def iter_empty_stars(self) -> range:
        return range(len(self.iter_full_stars()), 5)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=4
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    review = models.TextField()


class ProductSecondaryImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="secondary_images")
    image = ResizedImageField(
        upload_to=product_secondary_image_name,
        blank=False,
        null=False,
        size=[500, 500]
    )
