from datetime import datetime, timedelta

# Find current time
dt = datetime.now()
print('current datetime:', dt)
print('current date    :', dt.date())
print(dt.year, dt.month, dt.day)

# Create a datetime object for specific date and time
dt2 = datetime(2017, 3, 3, 0, 0, 0)
print('dt2 datetime:', dt2)

# compare datetime objects
print('dt2 is later than now(): ', dt2 > dt)

# timedelta data type
twodays = timedelta(days=2, hours=3)

dt_plus2 = dt + twodays 
print('dt_plus2 datetime:', dt_plus2)
print('dt_plus2 is later than now(): ', dt_plus2 > dt)

print()
print("strftime(): Convert datetime object into strings....")
# Convert datetime object into strings
print(dt.strftime('%Y/%m/%d %H:%M:%S'))  # note that stfrtime doesn't begin with datetime.dateime
print(dt.strftime('%B %d, %Y')) # January 01, 2018
print(dt.strftime('%I:%M %p')) # 00:00 AM/PM

print()
print("strptime():  Convert strings into datetime objects....")
# Convert strings into datetime objects
dt_object = datetime.strptime('March 4, 2017', '%B %d, %Y')
print(dt_object)

# print as specific fromat
print(dt_object.strftime('%B %d, %Y'))

# print in default format: xxxx-xx-xx
print(dt_object.date())

# convert unix timestamp string to readable date.
print()
print("Convert unix timestamp string to readable date....")

## get current timestamp since January 1, 1970
ts = datetime.now().timestamp()
print("local timestamp in secs: ", ts)

## convert timestamp to datetime object
dt4 = datetime.fromtimestamp(ts)

# print in default format
print(dt4.isoformat())

# print in specific format
print(dt4.strftime('%Y-%m-%d %H:%M:%S'))

## convert timestamp to datetime object with specific timezone
from dateutil.tz import gettz, tzutc, tzlocal

fmt = '%Y-%m-%d %H:%M:%S %z'
tpe_tz = gettz('Asia/Taipei')
ber_tz = gettz("Europe/Berlin")
utc_tz = gettz("UTC")

dt5 = datetime.fromtimestamp(ts, tzlocal())

# print in specific format
print(dt5.strftime('%Y-%m-%d %H:%M:%S %z'))

# Converting between timezones
print("\nUTC Time: ")
dt5_utc = dt5.astimezone(utc_tz) #tzutc() 
print(dt5_utc.strftime(fmt))

print("\nLocal Time in Berlin: ")
dt5_berlin = dt5.astimezone(ber_tz)
print(dt5_berlin.strftime(fmt))

print("\nLocal Time in Taipei: ")
dt5_taipei = dt5_berlin.astimezone(tpe_tz)
print(dt5_taipei.strftime(fmt))
print()

# 如何取得今天日期的字串
today_str = datetime.now().strftime('%Y-%m-%d')
print("今天是： " + today_str)