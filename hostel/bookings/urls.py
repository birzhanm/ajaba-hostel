from django.urls import path
from . import views
app_name = "bookings"

urlpatterns = [
    path('room/<int:pk>/checkin/', views.checkin, name='checkin'),
]
