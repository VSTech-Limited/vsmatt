from django.contrib import admin
from .models import Profile, Contact


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'profile_pic', 'phone', 'facebook_link', 'twitter_link']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message']
