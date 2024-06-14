# cron_job.py
from apscheduler.schedulers.blocking import BlockingScheduler
from parser import parse_logs

scheduler = BlockingScheduler()
scheduler.add_job(parse_logs, 'cron', hour=0)  # Запуск каждый день в полночь
scheduler.start()
