import os
from celery import Celery

# This must point to your correct settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octupus_test_project.settings')

app = Celery('octupus_test_project')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
