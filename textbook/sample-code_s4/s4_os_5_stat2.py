# -*- coding: UTF-8 -*-

import os
import time
import datetime
from dateutil.tz import gettz

st = os.stat("s4_os_2_path.py")
print(st)
#print(time.localtime(st.st_mtime))
#print(time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(st.st_mtime)))
print("datetime tzinfo: " , datetime.datetime.now().tzinfo)
mtime = datetime.datetime.fromtimestamp(st.st_mtime, gettz("Asia/Taipei"))
print(mtime.strftime("%Y-%m-%d %H:%M:%S %z"))

now = datetime.datetime.now(gettz("Asia/Taipei"))
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S %z"))

"""
import pytz
import datetime
 
local_tz = pytz.timezone("Asia/Hong_Kong")
datetime_without_tz = datetime.datetime.strptime("2018-02-14 12:34:56", "%Y-%m-%d %H:%M:%S")
datetime_with_tz = local_tz.localize(datetime_without_tz, is_dst=None) # No daylight saving time
datetime_in_utc = datetime_with_tz.astimezone(pytz.utc)
 
print(datetime_without_tz)
print(datetime_with_tz)
print(datetime_in_utc)
str1 = datetime_without_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str2 = datetime_with_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str3 = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')
 
print ('Without Timzone : %s' % (str1))
print ('With Timezone   : %s' % (str2))
print ('UTC Datetime    : %s' % (str3))

for tz in pytz.all_timezones:
    if tz.startswith("Asia"):
        print (tz)

print(pytz.country_timezones('tw'))
"""
