# application/usecases/meters/generate_and_save_report/_service.py

import os
from io import BytesIO
from datetime import datetime
from typing import Optional

from reportlab.pdfgen import canvas  # install reportlab if you haven’t already
from django.conf import settings

from meter_reading_manager.domain.meters.queries import get_readings_for_meter
from meter_reading_manager.interfaces.web.views import MeterReadingSerializer
from meter_reading_manager.data.models import MeterReading, Meter


def generate_and_save_report(*, meter_id: int) -> Optional[str]:
    """
    1. Fetch all readings for the given meter (via domain query)
    2. Serialize them to a list of dicts
    3. Build a PDF in memory
    4. Save the PDF to disk under MEDIA_ROOT/reports/meter_<meter_id>_<timestamp>.pdf
    Returns the full filesystem path of the saved PDF, or None if meter does not exist.
    """
    # 1. Load Meter (this will raise if not found; caller may catch)
    try:
        meter = Meter.objects.get(pk=meter_id)
    except Meter.DoesNotExist:
        return None

    # 2. Get all readings (you already have a domain query)
    readings_qs = get_readings_for_meter(meter)  # returns List[MeterReading]

    # 3. Serialize readings to plain dicts
    serialized_readings = MeterReadingSerializer(instance=readings_qs, many=True).data

    # 4. Build PDF in memory
    pdf_bytes = _build_pdf(meter_name=meter.name, readings=serialized_readings)

    # 5. Determine a filesystem path
    #    e.g. <MEDIA_ROOT>/reports/meter_<id>_<YYYYMMDD_HHMMSS>.pdf
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"meter_{meter_id}_{timestamp}.pdf"
    reports_dir = os.path.join(settings.MEDIA_ROOT, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    file_path = os.path.join(reports_dir, filename)

    # 6. Write bytes to that path
    with open(file_path, "wb") as f:
        f.write(pdf_bytes)

    return file_path


def _build_pdf(*, meter_name: str, readings: list) -> bytes:
    """
    Simple PDF: header + each reading on its own line.
    `readings` is a list of dicts, each with keys: 
      'id', 'meter_name', 'reading_value', 'reading_date', 'created_at'.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 800, f"Report for Meter: {meter_name}")
    p.setFont("Helvetica", 12)

    y = 780
    for rd in readings:
        line = f"{rd['reading_date']}: {rd['reading_value']}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.read()
