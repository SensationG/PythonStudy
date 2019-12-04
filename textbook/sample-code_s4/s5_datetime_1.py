#---------------------------datetime--------------------------

from datetime import datetime, timedelta

# Find current time
dt = datetime.now() #呼叫电脑当前时间
print('current datetime:', dt)
print('current date    :', dt.date())#.hour .minute .second
print(dt.year, dt.month, dt.day)

# Create a datetime object for specific date and time
dt2 = datetime(2017, 3, 3, 0, 0, 0)#给一串数字建成时间
print('dt2 datetime:', dt2)

# compare datetime objects 对比时间先后
print('dt2 is later than now(): ', dt2 > dt)

# timedelta data type 时间快进相加
twodays = timedelta(days=2, hours=3)

dt_plus2 = dt + twodays #时间加减
print('dt_plus2 datetime:', dt_plus2)
print('dt_plus2 is later than now(): ', dt_plus2 > dt)

print() #时间转为字符串，设置输出格式
print("strftime(): Convert datetime object into strings....")
# Convert datetime object into strings
print(dt.strftime('%Y/%m/%d %H:%M:%S'))  # note that stfrtime doesn't begin with datetime.dateime
print(dt.strftime('%B %d, %Y')) # January 01, 2018
print(dt.strftime('%I:%M %p')) # 00:00 AM/PM #上午下午

print() #字符串转为时间
print("strptime():  Convert strings into datetime objects....")
# Convert strings into datetime objects
dt_object = datetime.strptime('March 4, 2017', '%B %d, %Y')
print(dt_object) #2017-03-04 00:00:00

# print as specific fromat :datatime转为特殊格式字串
print(dt_object.strftime('%B %d, %Y')) #type:str  March 04, 2017

# print in default format: xxxx-xx-xx
print('默认日期格式：',dt_object.date()) # 2017-03-04

# convert unix timestamp string to readable date.
print()
#将unix时间戳转为可读时间
print("Convert unix timestamp string to readable date....")

## get current timestamp since January 1, 1970
ts = datetime.now().timestamp() #从1970到现在的时间
print("local timestamp in secs: ", ts)

## convert timestamp to datetime object
dt4 = datetime.fromtimestamp(ts) #1575375241.094724

# print in default format
print('isoformat:',dt4.isoformat()) #2019-12-03T20:14:01.094724

# print in specific format
print(dt4.strftime('%Y-%m-%d %H:%M:%S'))  #2019-12-03 20:14:01

## convert timestamp to datetime object with specific timezone
from dateutil.tz import gettz, tzutc, tzlocal #转换时区 将当前时间转为不同时区时间

fmt = '%Y-%m-%d %H:%M:%S %z'
tpe_tz = gettz('Asia/Taipei')
ber_tz = gettz("Europe/Berlin")
utc_tz = gettz("UTC")   #定义国际标准时区

dt5 = datetime.fromtimestamp(ts, tzlocal())

# print in specific format
print(dt5.strftime('%Y-%m-%d %H:%M:%S %z'))

# Converting between timezones
print("\nUTC Time: ")
dt5_utc = dt5.astimezone(utc_tz) #tzutc() #转成国际标准时间
print(dt5_utc.strftime(fmt))

print("\nLocal Time in Berlin: ")
dt5_berlin = dt5.astimezone(ber_tz)#转成柏林时间
print(dt5_berlin.strftime(fmt)) 
print("\nLocal Time in Taipei: ")
dt5_taipei = dt5_berlin.astimezone(tpe_tz)#转成台北时间
print(dt5_taipei.strftime(fmt))
print()

# 如何取得今天日期的字串
today_str = datetime.now().strftime('%Y-%m-%d')
print("今天是： " + today_str)