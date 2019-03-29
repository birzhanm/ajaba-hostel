from django.urls import path
from . import views
app_name = "bookings"

urlpatterns = [
    path('checkin/<int:pk>', views.checkin, name='checkin'),
]
