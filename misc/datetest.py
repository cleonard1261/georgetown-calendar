#!/usr/bin/python


from datetime import *
from dateutil import parser
#import MonthDelta

vdate = '2007-10-28'
vtime =  '13:30:00'

# need to figure out string to date and time conversions
dt = parser.parse(vdate+' '+vtime)
#date_object = datetime.strptime(vdate, '%Y-%m-%d')
print dt

#print dt + timedelta(months=1) 
print dt + timedelta(days=7)  # adding days   -- no problem
#print dt.year + 1             # adding years  -- no problem
						  # adding months -- big problem!!
print int(dt.month)
if int(dt.month) in [1,3,5,7,8,10,12]:
    dt = dt.replace(day=31)
    if int(dt.month) == 12:
        #dt.replace(month=1)
        dt = dt.replace(year=int(dt.year + 1), month=1)
        print "in here: ", dt
    else:		
        dt.replace(month=int(dt.month+1))
    print "this is: ", dt
elif int(dt.month) in [4,6,9,11]:
    print 'month number ', dt.month, 'has 30 days.'
elif int(dt.year) % 4 == 0:
	print "it's a leap year and Feb as 29 days."
else:
	print "Feb has 28 days."
						  
if dt.month == 12:
    m =  1
    y = dt.year + 1
else:
    m = str(dt.month + 1)
    y = dt.year

#print m
m = str(0) + str(m)
#print m
#print parser.parse(str(y) + '-' + m + '-' + str(dt.day) +' ' + str(vtime))
yr = int(dt.year + 1)
#print dt.replace(month=01)
#print dt.replace(year=yr)

