from manage import run_scrapers
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


# @sched.scheduled_job('interval', minutes=55)
# def timed_job():
#     print('cron started')
#     run_scrapers()
#     print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=0)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=2)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=4)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=6)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=14)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=16)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=18)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=20)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=22)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=24)
def scheduled_job():
    print('cron started')
    run_scrapers()
    print('cron finished')

sched.start()