from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'description', 'phone')
    list_filter = ('user', 'description', 'phone')
    search_fields = ('user', 'description', 'phone')
    raw_id_fields = ('user',)
