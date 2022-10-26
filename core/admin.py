from django.contrib import admin
from .models import Contact, Category, Tag, JujaMall, Team


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(JujaMall)
class JujaMallAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'twitter_handle', 'facebook', 'linked_in', 'instagram', 'github', 'email',
                    'address']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'photo']