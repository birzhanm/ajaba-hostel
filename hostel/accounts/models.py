import datetime
from bookings.models import Booking
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50, null=True, blank=True)

    def is_tenant(self):
        is_staff = self.user.is_staff()
        is_tenant = not is_staff
        return is_tenant

    def get_bookings(self, specific_date=datetime.date.today()):
        bookings = self.booking_set.filter(start_date__lte=specific_date, end_date__gte=specific_date)
        return bookings

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, **kwargs):
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
        instance.profile.save()
