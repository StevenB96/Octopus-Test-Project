# interfaces/tasks/meters/generate_report_task.py

from meter_reading_manager.celery import shared_task

from meter_reading_manager.application.usecases.meters.generate_and_save_report import generate_and_save_report

@shared_task
def generate_report_for_meter(meter_id: int):
    """
    Celery task entry point. Given a meter_id, calls the application
    use-case to build and save a PDF. Returns the saved file path.
    """
    # You could catch exceptions here if you want to log failures
    print('Meter ID:', meter_id)
    file_path = generate_and_save_report(meter_id=meter_id)
    return file_path