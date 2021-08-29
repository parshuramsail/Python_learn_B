import  datetime
import pytz
today=datetime.date.today()
print(today)
birthday=datetime.date(1996,7,15)
print(birthday)

# find days since birth
day_since_birth=(today-birthday)
print(day_since_birth)

# adding 10 days to current days
tdelta=datetime.timedelta(days=10)
print(today+tdelta)
print(today.day)

# saturday=5
print(today.weekday())
#monday=0 ,sunday=6

print(datetime.time(7,2,20,15))
# datetime.date(Y,M,D)
# datetime.time(H,M,S,MS)
# datetime.datetime(Y,M,D,H,M,S,MS)

# tdelta=datetime.timedelta(days=10)  # adding days
hour_delta=datetime.timedelta(hours=10) # adding hours
print(datetime.datetime.now()+hour_delta )

# TIMEZONE
datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific=datetime_today.astimezone(pytz.timezone("Indian/Mahe"))
print(datetime_pacific)
#for tz in pytz.all_timezones:
 #   print(tz)
