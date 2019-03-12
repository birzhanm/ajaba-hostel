from django.urls import path
from . import views
app_name = 'rooms'

urlpatterns = [
    path('', views.block_list, name="block_list"),
    path('<int:pk>/', views.block_detail, name="block_detail"),
]
