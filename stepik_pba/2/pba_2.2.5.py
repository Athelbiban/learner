import datetime as dt


year, month, day = (int(i) for i in input().split())

x = dt.datetime(year, month, day)
y = dt.timedelta(days=day, months=month, years=year)