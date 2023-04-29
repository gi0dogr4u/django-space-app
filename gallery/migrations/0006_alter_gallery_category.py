# Generated by Django 4.2 on 2023-04-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_gallery_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.IntegerField(choices=[(1, 'Star'), (2, 'Galaxy'), (3, 'Planet'), (4, 'Nebula'), (5, 'Earth')], verbose_name='Categories of Astronomy Events'),
        ),
    ]
