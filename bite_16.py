from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date_jump = PYBITES_BORN + timedelta(days=100)
    year_jump = PYBITES_BORN + timedelta(days=365)
    while True:
        yield date_jump
        date_jump += timedelta(days=100)
        if date_jump > year_jump:
            yield year_jump
            year_jump += timedelta(days = 365)

for date in gen_special_pybites_dates():
    if date > datetime(year=2019, month=3, day=1):
        break
    print(date)

"""
Use generator to return dates
return every 100 days from PYBITES_BORN
return every birthday of PYBITES_BORN
until 2/27/2019

***** ANSWER IN A SIMPLER FORM ******

def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)

"""