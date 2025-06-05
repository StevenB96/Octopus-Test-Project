# File: meter_reading_manager/interfaces/web/forms.py

from django import forms
from meter_reading_manager.data.models import Meter


class MeterReadingForm(forms.Form):
    """
    Form for users to submit a new MeterReading.
    """
    meter = forms.ModelChoiceField(
        queryset=Meter.objects.all(),
        label="Select Meter",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    reading_value = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Reading Value",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    reading_date = forms.DateField(
        label="Reading Date",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
