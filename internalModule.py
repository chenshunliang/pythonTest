from datetime import datetime, timezone, timedelta
import re
from collections import namedtuple, Counter
import hashlib

now = datetime.now()
timestamp = now.timestamp()
print(now)
print(timestamp)
print(datetime.fromtimestamp(timestamp))


def to_timestasp(dt_str, tz_str):
    cdate = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    r = re.match(r'^UTC\+(\d+):00$', tz_str)
    hour = r.group(1)
    utcdate = cdate.replace(tzinfo=timezone(timedelta(hours=int(hour))))
    return utcdate.timestamp()


t = to_timestasp('2015-6-1 08:10:30', 'UTC+7:00')
print(t)
assert t == 1433121030.0, t

# nametuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

c = Counter()
for i in 'programmer':
    c[i] += 1
print(c)

# md5
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())
