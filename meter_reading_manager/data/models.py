# File: meter_reading_manager/data/models.py

from django.db import models


class Meter(models.Model):
    """
    Represents a physical meter (e.g. electricity or gas).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MeterReading(models.Model):
    """
    Represents a single reading for a given meter.
    """
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name="readings")
    reading_value = models.DecimalField(max_digits=10, decimal_places=2)
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-reading_date"]

    def __str__(self):
        return f"{self.meter.name} – {self.reading_value} on {self.reading_date}"
