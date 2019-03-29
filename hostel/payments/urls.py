from django.urls import path
from . import views
urlpatterns = [
    path('checkin', views.checkin, name='checkin'),
]
