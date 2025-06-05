# meter_reading_manager/urls.py

from django.urls import path, include

app_name = 'meter_reading_manager'

urlpatterns = [
    path("", include("meter_reading_manager.interfaces.web.urls")),
]