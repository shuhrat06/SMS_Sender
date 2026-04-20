from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from api.models import NewSms, SendedSms
import subprocess
import os
import time
import re



def send_sms():
    while NewSms.objects.all().exists():
        new_smses = NewSms.objects.all()[:10]
        for sms in new_smses:
            try:
                command = ['termux-sms-send', '-n', sms.phone, sms.msg]
                result = subprocess.run(
                    command,
                    timeout=15,  # 15 soniya timeout
                    capture_output=True,
                    text=True
                )    
            except subprocess.TimeoutExpired:
                print("SMS jo'natish vaqti o'tib ketdi", sms.phone, "--", sms.msg)
            except Exception as e:
                print(f"Kutilmagan xatolik: {str(e)}", sms.phone, "--", sms.msg)
            else:
                SendedSms.objects.create(
                    phone = sms.phone,
                    msg = sms.msg
                )
                sms.delete()
    else:
        print("Jo'natish uchun sms mavjud emas!")



def start_sms_scheduler():
    """
    Schedulerni ishga tushirish
    """
    scheduler = BackgroundScheduler()
    
    # Har 5 sekundda yangi SMSlarni tekshirish
    scheduler.add_job(
        send_sms,
        'interval',
        seconds=5,
        id='sms_processor',
        replace_existing=True
    )
    
    scheduler.start()
    print("🚀 SMS Scheduler ishga tushdi! Har 5 sekundda tekshiradi.")