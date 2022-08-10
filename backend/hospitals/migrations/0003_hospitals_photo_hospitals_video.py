# Generated by Django 4.0.5 on 2022-08-05 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_remove_hospitals_location_hospitals_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitals',
            name='photo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitals',
            name='video',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]