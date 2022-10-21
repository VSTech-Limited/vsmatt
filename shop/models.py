from django.db import models
# Create your models here.

class Cartegory:
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
