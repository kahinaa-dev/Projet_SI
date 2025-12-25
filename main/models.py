from django.db import models

class Shipment(models.Model):
    name = models.CharField(max_length=100)
    shipment_number = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.FloatField()
    service = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    estimated_delivery = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.shipment_number}"
