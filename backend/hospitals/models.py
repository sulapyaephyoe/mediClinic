from django.db import models

# Create your models here.
class hospitals(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.FileField(upload_to='photos/')
    video = models.FileField(upload_to='videos/')

    def _str_(self):
        return self.name
