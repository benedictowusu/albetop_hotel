import uuid
from django.db import models

# Create your models here.
class Book(models.Model):
    room_type_choices = [
        ('suite', 'Suite'),
        ('vip', 'VIP'),
        ('standard', 'Standard'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    room_type = models.CharField(max_length=10, choices=room_type_choices)
    checkin = models.DateField()
    checkout = models.DateField()
    booking_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    number_of_rooms = models.IntegerField(default=1)

    def __str__(self):
        print(f'Booking of {self.room_type} done. Your booking code is {self.booking_code}')