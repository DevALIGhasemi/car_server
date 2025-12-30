from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    imei = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name      = models.CharField(max_length=255)
    car       = models.ForeignKey(Car, on_delete=models.CASCADE)
    latitude  = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.name} ({self.latitude}, {self.longitude})"
