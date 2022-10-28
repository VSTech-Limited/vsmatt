from django.contrib import admin
from .models import Contact, Category, Tag, JujaMall, Team


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message']
    search_fields = ['name', 'email', 'phone_number', 'message']
    date_hierarchy = 'created_at'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug', 'created_by']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['slug']


@admin.register(JujaMall)
class JujaMallAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'phone_number', 'twitter', 'facebook', 'linkedin', 'instagram', 'github', 'email', 'address']
    list_editable = ['logo', 'phone_number', 'twitter', 'facebook', 'linkedin', 'instagram', 'github', 'email', 'address']



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'image']
    list_editable = ['position', 'image']
    search_fields = ['user', 'position']
    list_filter = ['position', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'