# Generated by Django 2.1.1 on 2018-09-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20180925_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='taking_request',
            field=models.BooleanField(blank=True),
        ),
    ]
