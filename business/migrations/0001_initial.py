# Generated by Django 4.0.8 on 2022-11-11 20:15

import business.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[500, 500], upload_to=business.models.business_file_name)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_addressed', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='business.businessprofile')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[100, 100], upload_to=business.models.bs_category_file_name)),
                ('marker', models.ImageField(blank=True, null=True, upload_to=business.models.markers_file_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_category_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Business Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='BusinessBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_service_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('slug', models.SlugField()),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[500, 500], upload_to=business.models.business_branch_file_name)),
                ('is_approved', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='business.businessprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='business.businesscategory')),
            ],
        ),
        migrations.CreateModel(
            name='BranchReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='business.businessbranch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
