from django.contrib import admin
from .models import Contact, Language, Tag, Vsmatt, Team


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message', 'is_addressed', 'created_at']
    list_filter = ['is_addressed', 'created_at']
    search_fields = ['name', 'email', 'phone_number', 'message']
    date_hierarchy = 'created_at'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Vsmatt)
class VsmattAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'phone_number', 'twitter', 'linkedin', 'github', 'email', 'address']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'image', 'created_at', 'updated_at']
    search_fields = ['user', 'position']
    list_filter = ['position', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.site_header = "BizBoost Admin"