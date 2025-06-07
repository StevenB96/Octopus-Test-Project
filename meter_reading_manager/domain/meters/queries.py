# File: meter_reading_manager/domain/meters/queries.py

from typing import Optional, List
from meter_reading_manager.data.models import Meter, MeterReading


def get_last_reading(meter: Meter) -> Optional[MeterReading]:
    """
    Returns the most recent MeterReading for the given Meter, or None if none exist.
    """
    return meter.readings.order_by("-reading_date").first()


def list_all_meters() -> List[Meter]:
    """
    Return Meter instances.
    """
    return list(Meter.objects.all())


def get_readings_for_meter(meter: Meter) -> List[MeterReading]:
    """
    Return all MeterReading instances for the given Meter,
    ordered by reading_date descending (newest first).
    """
    # Use the reverse FK relation and explicit ordering
    qs = meter.readings.order_by("-reading_date")
    return list(qs)
