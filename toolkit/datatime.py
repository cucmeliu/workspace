所有日期、时间的api都在datetime模块内。

1. 日期输出格式化 datetime => string

import datetime

now = datetime.datetime.now()

now.strftime('%Y-%m-%d %H:%M:%S')

输出

'2015-04-07 19:11:21'

strftime是datetime类的实例方法。



2. 日期输出格式化 string => datetime

import datetime

t_str = '2015-04-07 19:11:21'

d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')

strptime是datetime类的静态方法。



3. 日期比较操作

在datetime模块中有timedelta类，这个类的对象用于表示一个时间间隔，比如两个日期或者时间的差别。

构造方法：

import datetime

datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

所有的参数都有默认值0，这些参数可以是int或float，正的或负的。

可以通过 timedelta.days、tiemdelta.seconds 等获取相应的时间值。

timedelta 类的实例，支持加、减、乘、除等操作，所得的结果也是 timedelta 类的实例。比如：

import datetime

year = datetime.timedelta(days=365)

ten_years = year *10

nine_years = ten_years - year

同时，date、time和datetime类也支持与timedelta的加、减运算。

datetime1 = datetime2 + timedelta

timedelta = datetime1 - datetime2

这样，可以很方便的实现一些功能。



4. 两个日期相差多少天。

import datetime

d1 = datetime.datetime.strptime('2015-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')

d2 = datetime.datetime.strptime('2015-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')

delta = d1 - d2

print delta.days

输出：3



5. 今天的n天后的日期。

import datetime

now = datetime.datetime.now()

delta = datetime.timedelta(days=3)

n_days = now + delta

print n_days.strftime('%Y-%m-%d %H:%M:%S')

输出：

2015-04-10 19:16:34



#coding=utf-8

import datetime

now=datetime.datetime.now()

print now



#将日期转化为字符串

datetime => string

import datetime

now=datetime.datetime.now()

print now.strftime('%Y-%m-%d %H:%M:%S')



#将字符串转换为日期 string => datetime

import datetime

t_str = '2015-03-05 16:26:23'

d=datetime.datetime.strptime(t_str,'%Y-%m-%d %H:%M:%S')

print d

#在datetime模块中有timedelta类，这个类的对象用于表示一个时间间隔，比如两个日#期或者时间的差别。



#计算两个日期的间隔

import datetime

d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')

d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')

delta = d1 - d2

print delta.days print delta



#今天的n天后的日期

import datetime

now=datetime.datetime.now()

delta=datetime.timedelta(days=3)

n_days=now+delta

print n_days.strftime('%Y-%m-%d %H:%M:%S')

datetime的好处是可以实现方便的时间运算,比如 endTime - starTime,这在时间duration计算时非常方便.
