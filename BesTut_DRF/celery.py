import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BesTut_DRF.settings')

app = Celery('BesTut_DRF')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule={
        'send-mail-everyday-at-22':{
            'task':'api.tasks.send_mail_func',
            'schedule':crontab(hour=22,minute=31)
        },
    }


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')