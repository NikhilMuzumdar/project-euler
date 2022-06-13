import datetime as dt

start = dt.datetime.strptime('01 Jan 1901', "%d %b %Y")
end = dt.datetime.strptime('31 Dec 2000', "%d %b %Y")

delta = end - start
sundays = [(start + dt.timedelta(days=i)) for i in range(delta.days+1) if (start + dt.timedelta(days=i)).weekday() == 6 and (start + dt.timedelta(days=i)).day == 1]

print(len(sundays))
