from django.urls import path
from . import views
app_name = 'rooms'

urlpatterns = [
    path('', views.block_list, name="block_list"),
    path('blocks/<int:pk>/', views.block_detail, name="block_detail"),
    path('rooms/<int:pk>/', views.room_detail, name="room_detail"),
]
