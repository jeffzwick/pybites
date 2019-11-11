import calendar
import datetime


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    born = datetime.date.weekday(date)
    return (calendar.day_name[born])

print(weekday_of_birth_date(datetime.date(1974, 11, 11)))
