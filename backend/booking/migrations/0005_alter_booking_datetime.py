# Generated by Django 3.2 on 2022-08-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20220815_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='%Y-%m-%d %H:%M:%S'),
        ),
    ]
