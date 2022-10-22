from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_pic', 'bio', 'phone_number')
    list_filter = ('user', 'bio', 'phone_number')
    search_fields = ('user', 'bio', 'phone_number')
    raw_id_fields = ('user',)
