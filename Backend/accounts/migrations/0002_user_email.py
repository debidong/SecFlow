# Generated by Django 4.2.1 on 2023-07-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='default@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]