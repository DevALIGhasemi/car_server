from django.db import models

class Account(models.Model):
    name         = models.CharField(max_length=255)
    car          = models.CharField(max_length=255)
    year         = models.IntegerField()
    phone        = models.CharField(max_length=255)
    Subscription = models.CharField(max_length=255)
    image        = models.ImageField(upload_to='media',null=True)
    uniq         = models.CharField(max_length=255)
    def __str__(self):
        return self.name