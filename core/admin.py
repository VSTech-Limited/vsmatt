from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass

