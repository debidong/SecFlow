# Generated by Django 4.2.1 on 2023-07-24 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_online_room_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='rid',
        ),
    ]