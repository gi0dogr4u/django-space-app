# Generated by Django 4.2 on 2023-04-29 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallery_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
