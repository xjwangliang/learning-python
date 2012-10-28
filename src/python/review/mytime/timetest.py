#encoding=utf-8
import time

now = time.time()

print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)


now = time.localtime(time.time())

print time.asctime(now)                         #Fri Oct 26 11:18:12 2012
print time.strftime("%y/%m/%d %H:%M", now)      #12/10/26 11:18
print time.strftime("%a %b %d", now)            #Fri Oct 26
print time.strftime("%c", now)                  #Fri Oct 26 11:18:12 2012
print time.strftime("%I %p", now)               #11 AM
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)#2012-10-26 11:18:12 CST

# do it by hand...
year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "%04d-%02d-%02d" % (year, month, day)                                     #2012-10-26
print "%02d:%02d:%02d" % (hour, minute, second)                                 #11:18:12
print ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday       #FRI 300


#最好的方式
#不好之处在于年不是４位
print r'%y/%m/%d %H:%M的方式　',time.strftime("%y/%m/%d %H:%M:%S", now)      #12/10/26 11:18
print r'%Y/%m/%d %H:%M:%S的方式　',time.strftime("%Y-%m-%d %H:%M:%S", now)



t0 = time.time()
tm = time.localtime(t0)

print 'tm ', tm #tm  time.struct_time(tm_year=2012, tm_mon=10, tm_mday=26, tm_hour=11, tm_min=27, tm_sec=15, tm_wday=4, tm_yday=300, tm_isdst=0)

print 't0 ',t0  #1351222035.08
print time.mktime(tm)#1351222035.0


#http://wiki.woodpecker.org.cn/moin/PythonStandardLib/chpt1#eg-1-66