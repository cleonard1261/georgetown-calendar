#!/usr/bin/python


from datetime import *
from dateutil import parser
#import MonthDelta

vdate = '2008-11-28'
vtime =  '13:30:00'

# need to figure out string to date and time conversions
dt = parser.parse(vdate+' '+vtime)
#date_object = datetime.strptime(vdate, '%Y-%m-%d')
print dt

#print dt + timedelta(months=1) 
print dt + timedelta(days=7)  # adding days   -- no problem
#print dt.year + 1             # adding years  -- no problem
						  # adding months -- big problem!!

if dt.month == 12:
    m =  1
    y = dt.year + 1
else:
    m = str(dt.month + 1)
    y = dt.year

print m
m = str(0) + str(m)
print m
print parser.parse(str(y) + '-' + m + '-' + str(dt.day) +' ' + str(vtime))
#print parser.parse(newDt)

