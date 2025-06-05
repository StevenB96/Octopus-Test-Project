# File: meter_reading_manager/application/usecases/meters/submit_reading/_service.py

from datetime import date
from meter_reading_manager.data.models import Meter
from meter_reading_manager.domain.meters.operations import create_reading, ReadingAlreadyExistsError
from django.core.exceptions import ObjectDoesNotExist


def submit_meter_reading(*, meter_id: int, reading_value: float, reading_date: date):
    """
    Use-case: Submit a new meter reading.

    Parameters:
        meter_id (int): Primary key of the Meter to record a reading for.
        reading_value (float): The numeric value of the reading.
        reading_date (date): The date the reading was taken.

    Raises:
        Meter.DoesNotExist: If no Meter with the given ID exists.
        ReadingAlreadyExistsError: If a reading for that meter on that date already exists.
    """
    try:
        meter = Meter.objects.get(pk=meter_id)
    except ObjectDoesNotExist:
        raise Meter.DoesNotExist(f"No Meter found with id={meter_id}")

    # Delegate creation (and duplicate-check) to the domain layer
    return create_reading(meter=meter, reading_value=reading_value, reading_date=reading_date)
