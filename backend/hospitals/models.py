from django.db import models

# Create your models here.
class hospitals(models.Model):

   

    name = models.CharField(max_length=255)

    phone = models.CharField(max_length=255)

    location = models.CharField(max_length=355)

    website = models.CharField(max_length=255)

    type = models.CharField(max_length=255)



    def _str_(self):

        return self.name
