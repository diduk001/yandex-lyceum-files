import datetime

import schedule


def job(hour):
    h = hour % 12
    if h == 0:
        h = 12

    for i in range(h):
        print("Ку")


schedule.every().hour.at(":00").do(job, hour=datetime.datetime.now().hour)

while True:
    schedule.run_pending()