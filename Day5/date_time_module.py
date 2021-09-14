import datetime

curtime = datetime.time(2,30)

print(curtime.hour)
print(curtime.minute)
print(curtime)

curdate = datetime.date.today()

print(curdate)
print(curdate.day)
print(curdate.month)
print(curdate.year)
print(curdate.ctime())

# -------------------------------------------------------------

from datetime import datetime

mydatetime = datetime(2021,9,14,2,45,40)

print(mydatetime)

print(mydatetime.replace(year=2022))
