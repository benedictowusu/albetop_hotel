from django.db import models
from django.contrib.auth.models import User
from rooms.models import Standard, Suite, VIP
import uuid

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=255)

class Standard(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, default=None)
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE)

class Suite(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE, default=None)
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE)

class VIP(models.Model):
    vip = models.ForeignKey(VIP, on_delete=models.CASCADE, default=None)
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE)   

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_rooms = models.PositiveIntegerField(default=1)
    booking_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'Booking for {self.room} successful from {self.checkIn} to {self.checkout}'
    
    def save(self, *args, **kwargs):
        if not self.booking_code:
            self.booking_code = str(uuid.uuid4()) #generate code
        super().save(*args, **kwargs)
    