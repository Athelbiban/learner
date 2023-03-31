from datetime import datetime, timedelta


date = datetime(*map(int, input().split())) + timedelta(days=int(input()))
print(date.year, date.month, date.day)
