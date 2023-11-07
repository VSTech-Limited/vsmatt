from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','gender', 'image', 'phone_number', 'dob', 'created_at')
    list_filter = ('user', 'gender', 'languages')
    autocomplete_fields = ('user',)
    search_fields = ('user', 'bio', 'phone_number')
    date_hierarchy = 'created_at'
