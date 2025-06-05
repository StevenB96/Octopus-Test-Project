# File: meter_reading_manager/domain/meters/queries.py

from typing import Optional, List
from meter_reading_manager.data.models import Meter, MeterReading


def get_last_reading(meter: Meter) -> Optional[MeterReading]:
    """
    Returns the most recent MeterReading for the given Meter, or None if none exist.
    """
    return meter.readings.order_by("-reading_date").first()


def get_readings_for_meter(meter: Meter) -> List[MeterReading]:
    """
    Returns all MeterReading instances for the given Meter, ordered by date descending.
    """
    return list(meter.readings.all())
