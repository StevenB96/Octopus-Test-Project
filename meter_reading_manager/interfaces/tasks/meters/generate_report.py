# interfaces/tasks/meters/generate_report_task.py

import logging
from meter_reading_manager.celery import app
from meter_reading_manager.application.usecases.meters.generate_and_save_report import generate_and_save_report

logger = logging.getLogger(__name__)

@app.task(name='generate_report_for_meter')
def generate_report_for_meter(meter_id: int):
    """
    Celery task to generate and save a meter report.
    Returns the file path of the generated report.
    """
    logger.info(f"[TASK] Generating report for meter ID {meter_id}")
    try:
        file_path = generate_and_save_report(meter_id=meter_id)
        logger.info(f"[TASK] Report generated at: {file_path}")
        return file_path
    except Exception as e:
        logger.exception(f"[TASK] Failed to generate report for meter {meter_id}: {e}")
        raise
