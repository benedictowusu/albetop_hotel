from django.db import models

# Create your models here.
class Suite(models.Model):
    name = models.CharField(max_length=100, default="Suite")
    pricepernight = models.IntegerField(default=2500)
    numberofmasterbedrooms = models.IntegerField(default=1)
    typeofbedinmastersbedroom = models.CharField(max_length=100, default="King size bed")
    numberofbedrooms = models.IntegerField(default=4)
    typeofbedinotherrooms = models.CharField(max_length=100, default="Double bed")
    numberofbathrooms = models.IntegerField(default=4)
    numberoflivingarea = models.IntegerField(default=2)
    kitchen = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class VIP(models.Model):
    name = models.CharField(max_length=100)
    pricepernight = models.IntegerField(default=100)
    numberofmasterbedrooms = models.IntegerField(default=1)
    typeofbedinmastersbedroom = models.CharField(max_length=100 ,default="Queen size bed")
    numberofbedrooms = models.IntegerField(default=2)
    typeofbedinotherrooms = models.CharField(max_length=100, default="Double bed")
    numberofbathrooms = models.IntegerField(default=3)
    numberoflivingarea = models.IntegerField(default=1)
    kitchen = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Standard(models.Model):
    name = models.CharField(max_length=100)
    pricepernight = models.IntegerField(default=500)
    numberofbedrooms = models.IntegerField(default=1)
    typeofbed = models.CharField(max_length=100, default="Double bed")
    numberofbathrooms = models.IntegerField(default=1)

    def __str__(self):
        return self.name
