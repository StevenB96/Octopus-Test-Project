# File: meter_reading_manager/interfaces/web/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # List all Meters
    path(
        "",
        views.MeterListView.as_view(),
        name="meter-list"
    ),

    # Show all readings for a given meter
    path(
        "meters/<int:meter_id>/readings/",
        views.MeterReadingListView.as_view(),
        name="meter-readings"
    ),

    # Render & post the “submit a new reading” form
    path(
        "readings/submit/",
        views.SubmitReadingView.as_view(),
        name="submit-reading"
    ),

    # Create a pdf report for a given meter
    path(
        "meters/<int:meter_id>/create-report/",
        views.CreatePdfReportView.as_view(),
        name="create-pdf-report",
    ),
]
