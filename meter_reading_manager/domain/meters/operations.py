# File: meter_reading_manager/domain/meters/operations.py

from datetime import date
from meter_reading_manager.data.models import Meter, MeterReading


class ReadingAlreadyExistsError(Exception):
    """Raised when trying to create a reading for a date that already exists."""
    pass


def create_reading(*, meter: Meter, reading_value: float, reading_date: date) -> MeterReading:
    """
    Creates a new MeterReading for the given Meter on reading_date. Raises ReadingAlreadyExistsError
    if a reading for that meter on that date already exists.
    """
    existing = MeterReading.objects.filter(meter=meter, reading_date=reading_date).first()
    if existing:
        raise ReadingAlreadyExistsError(
            f"A reading for meter {meter.id} on {reading_date} already exists."
        )

    new_reading = MeterReading.objects.create(
        meter=meter,
        reading_value=reading_value,
        reading_date=reading_date
    )
    return new_reading
