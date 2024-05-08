from django.urls import path
from .views import combined_data_view

urlpatterns = [
    path('combined-data/', combined_data_view, name='combined_data'),
]