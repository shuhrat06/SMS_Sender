from django.apps import AppConfig
import os

class SmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sms'

    def ready(self):
        # Scheduler faqat asosiy threadda ishga tushsin
        if os.environ.get('RUN_MAIN') == 'true':
            from .sender import start_sms_scheduler
            start_sms_scheduler()