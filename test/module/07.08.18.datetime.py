# -*- coding: utf-8 -*-
#datetime模块，时间获取
# datetime：当前日期和时间，默认时区为None

from datetime import datetime
from _datetime import timedelta, timezone

###### 获取当前时间
now = datetime.now()
print('now datetime =', now)

##### 获取指定时间
dt = datetime(2017, 8, 18, 10, 18, 0)
print('Certain datetime =', dt)

##### datestamp：当前时区的当前时间到当前时区1970.1.1.00.00的秒数
now_second = now.timestamp()
print('now time to 1970.1.1.00.00 second =', now_second)

##### datestamp转到datetime
#### 转到当前时区的datetime
now2 = datetime.fromtimestamp(now_second)
print('now datetime =', now2)
#### 转到utc时区的datetime
utc_now2 = datetime.utcfromtimestamp(now_second)
print('now utc datetime =', utc_now2)

##### str转datetime
dt = datetime.strptime('2015-08-09 10:11:12', '%Y-%m-%d %H:%M:%S')
print('Certain datetime =', dt)
str_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print('Certain datetime str =', str_dt)
##### datetime加减
dt = dt - timedelta(days=2, hours=12)
print('Certain datetime =', dt)

#####时区转换
#先转到含有时区的datetime
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC datetime =', utc_dt)

# 转到相应的时区datetime
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('Beijin datetime =', bj_dt)
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('Tokyo datetime =', tokyo_dt)
print('END')