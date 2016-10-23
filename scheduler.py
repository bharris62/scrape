from manage import run_scrapers
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=360)
def timed_job():
    print('cron started')
    run_scrapers()
    print('cron finished')

sched.start()