import datetime
from django.db import models
from account.models import Manager, Tenant
from bookings.models import Booking


# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    num_levels = models.IntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def get_total_capacity(self):
        count=0
        for room in self.room_set.all():
            count += room.get_total_capacity()
        return count

    def get_available_capacity(self, date=datetime.date.today()):
        count=0
        for room in self.room_set.all():
            count += room.get_available_capacity(date)
        return count

    def __str__(self):
        print self.name


class Room(models.Model):
    block = models.ForeignKey(Block)
    number = models.CharField(max_length=50)
    level = models.IntegerField()
    capacity = models.IntegerField()

    def get_total_capacity(self):
        return self.capacity

    def get_available_capacity(self, date=datetime.date.today()):
        num_bookings = self.booking_set.filter(date__gte=F('start_date'), date__lte=F('end_date')).count()
        num_available = self.capacity - num_bookings
        return num_available
