# interfaces/tasks/meters/generate_report_task.py

import logging
from celery import shared_task
from meter_reading_manager.application.usecases.meters.generate_and_save_report import generate_and_save_report

logger = logging.getLogger(__name__)

@shared_task
def generate_report_for_meter(meter_id: int):
    logger.info(f"[TASK] Generating report for meter ID {meter_id}")
    try:
        file_path = generate_and_save_report(meter_id=meter_id)
        logger.info(f"[TASK] Report generated: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"[TASK] Failed to generate report: {e}")
        raise
