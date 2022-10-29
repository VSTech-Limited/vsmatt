# Generated by Django 4.0.8 on 2022-10-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_team_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='jujamall',
            old_name='linked_in',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='jujamall',
            old_name='twitter_handle',
            new_name='twitter',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='photo',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='description',
        ),
        migrations.AddField(
            model_name='contact',
            name='is_addressed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]