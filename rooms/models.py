import uuid
from django.db import models

# Create your models here.
class Suite(models.Model):
    name = models.CharField(max_length=100)
    numofSuites = models.IntegerField(default=0)
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
    
    @staticmethod
    def suiterooms():
        for i in range(20):
            Suite.objects.create(
                name=f"Suite Room {i+1}")

class VIP(models.Model):
    name = models.CharField(max_length=100)
    pricepernight = models.IntegerField(default=1000)
    numberofmasterbedrooms = models.IntegerField(default=1)
    typeofbedinmastersbedroom = models.CharField(max_length=100 ,default="Queen size bed")
    numberofbedrooms = models.IntegerField(default=2)
    typeofbedinotherrooms = models.CharField(max_length=100, default="Double bed")
    numberofbathrooms = models.IntegerField(default=3)
    numberoflivingarea = models.IntegerField(default=1)
    kitchen = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def viprooms():
        for i in range(100):
            VIP.objects.create(
                name=f"VIP Room {i+1}")


class Standard(models.Model):
    name = models.CharField(max_length=100)
    pricepernight = models.IntegerField(default=500)
    numberofbedrooms = models.IntegerField(default=1)
    typeofbed = models.CharField(max_length=100, default="Double bed")
    numberofbathrooms = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    @staticmethod
    def standardRooms():
        for i in range(200):
            Standard.objects.create(
                name=f'Standard Room {i+1}')
            
class Book(models.Model):
    room_choice = [
        ('suite', 'suite'),
        ('vip', 'VIP'),
        ('standard', 'Standard')
    ]
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    room_type = models.CharField(max_length=10, choices=room_choice)
    check_in = models.DateField(help_text='yyyy-mm-dd')
    check_out = models.DateField(help_text='yyyy-mm-dd')
    number_of_rooms = models.IntegerField(default=1)
    booking_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    

    def __str__(self):
        return f'Name Of Customer = {self.customer_name} || Email = {self.customer_email} || Booking code = {self.booking_code}'