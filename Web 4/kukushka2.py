import datetime

import schedule


def job(hour, string, interval):
    start, end = interval

    if start is not None:
        if start >= end:
            if start <= hour <= 23 or 00 <= hour <= end:
                pass
        else:
            if start <= hour <= end:
                pass

    h = hour % 12
    if h == 0:
        h = 12

    for i in range(h):
        print(string)


string = input("Введите сообщение, которое нужно выводить ")
interval = input("Введите интревал, когда не нужно ничего выводить в "
                 "формате \"hh-hh\" или нажмите Enter")

if interval is "":
    interval_start, interval_end = None, None
else:
    interval_start, interval_end = map(int, interval.split('-'))

schedule.every().hour.at(":03").do(job,
                                   hour=datetime.datetime.now().hour,
                                   string=string,
                                   interval=(interval_start, interval_end))

while True:
    schedule.run_pending()
