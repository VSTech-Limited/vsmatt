# Generated by Django 4.0.8 on 2022-10-28 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birth_date',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='facebook_link',
            new_name='facebook_url',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='github_link',
            new_name='github_url',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='linked_in_link',
            new_name='linkedin_url',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='twitter_link',
            new_name='twitter_url',
        ),
    ]