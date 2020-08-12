# Function converts the input date and time from computer format into a given format.

from datetime import datetime

def date_time(time):
    date_time_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')
    if date_time_obj.hour == 1:
        h = 'hour'
    else:
        h = 'hours'
    if date_time_obj.minute == 1:
        m = 'minute'
    else:
        m = 'minutes'
    return date_time_obj.strftime('{} %B %Y year {} {} {} {}').format(date_time_obj.day, date_time_obj.hour, h, date_time_obj.minute, m)

