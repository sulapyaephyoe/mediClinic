# Generated by Django 3.2 on 2022-08-18 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0011_hospitals_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitals',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='longitude',
        ),
    ]