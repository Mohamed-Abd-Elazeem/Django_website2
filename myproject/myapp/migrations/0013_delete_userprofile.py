# Generated by Django 4.2.11 on 2024-04-15 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_userprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]