import datetime
from django.db import models
from django.db.models import F
from accounts.models import Profile
from bookings.models import Booking


# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    num_levels = models.IntegerField()

    def get_total_capacity(self):
        count=0
        for room in self.room_set.all():
            count += room.get_total_capacity()
        return count

    def get_available_capacity(self, specific_date=datetime.date.today()):
        count=0
        for room in self.room_set.all():
            count += room.get_available_capacity(specific_date)
        return count

    def __str__(self):
        return self.name


class Room(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    level = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)


    def get_total_capacity(self):
        return self.capacity

    def get_available_capacity(self, specific_date=datetime.date.today()):
        num_bookings = self.booking_set.filter(start_date__lte=specific_date, end_date__gte=specific_date).count()
        num_available = self.capacity - num_bookings
        return num_available

    def __str__(self):
        return self.block.name + ":" + self.number
