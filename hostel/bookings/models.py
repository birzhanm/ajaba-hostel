import datetime
from django.db import models
from accounts.models import Tenant

# Create your models here.
class Booking(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return tenant.first_name + ' ' + tenant.last_name + '-' + room.number
