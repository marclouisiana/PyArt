# Generated by Django 2.1.1 on 2018-09-25 14:28

import art.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20180922_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='requests',
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=art.models.user_directory_path),
        ),
    ]
