# Generated by Django 4.2 on 2023-04-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('legend', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]
