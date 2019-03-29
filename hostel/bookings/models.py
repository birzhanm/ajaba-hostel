import datetime
from django.db import models

# Create your models here.
class Booking(models.Model):
    tenant = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.tenant.first_name + ' ' + self.tenant.last_name + '-' + self.room.number
