#!/usr/bin/python
# gtcal.events
# Events class hierarchy
#
# Author:
# Created:
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: events.py [] @georgetown.edu $

"""
Events class hierarchy
"""

##########################################################################
## Imports
##########################################################################

from datetime import *
#from  dateutil import relativedelta
from  dateutil import parser
import time



ZODIAC = {
    1: "Aries",
    2: "Taurus",
    3: "Gemini",
    4: "Cancer",
    5: "Leo",
    6: "Virgo",
    7: "Libra",
    8: "Scorpio",
    9: "Sagittarius",
    10: "Capricorn",
    11: "Aquarius",
    12: "Pisces"
}

##########################################################################
## Event Classes
##########################################################################

class Event(object):
    """
    Base event class that contains all properties and behavior of events.
    """

    def __init__(self, eventname, eventdate, eventtime):
        self.eventname = eventname
        self.eventdate = eventdate   
        self.eventtime = eventtime

    def __str__(self):
        pass

class RecurringEvent(Event):
    """
    Event that repeats for a fixed amount of time.
    """
   
    # events can occur daily, weekly, monthly, and yearly.
    def __init__(self, eventname, eventdate, eventtime,recurs='weekly'):
        self.eventname = eventname
        self.eventtime = eventtime
        self.eventdate = eventdate
        self.recurs    = recurs

        #from  dateutil import parser
        self.dt = parser.parse(self.eventdate+' '+self.eventtime)

    def isleapyear(self,year):
        if year % 4 == 0:
            return True
        else:
            return False

    def end_of_month(self):
        if int(self.dt.month + 1) in [3,5,7,8,10,12,13]:
            if int(self.dt.month+1) == 13:
                self.dt = self.dt.replace(year=int(self.dt.year + 1), month=1, day=31)
            else:
                self.dt = self.dt.replace(month=int(self.dt.month+1),day=31)
        elif int(self.dt.month+1) in [4,6,9,11]:
            self.dt = self.dt.replace(month=int(self.dt.month+1),day=30)
        elif self.isleapyear(int(self.dt.year)):
            self.dt = self.dt.replace(month=int(self.dt.month+1), day=29)
        else:
            self.dt = self.dt.replace(month=int(self.dt.month+1), day=28)

    def next_event(self):
        if self.recurs == 'weekly':
            self.dt = self.dt + timedelta(days=7)
        elif self.recurs == 'daily':
            self.dt = self.dt + timedelta(days=1)
        elif self.recurs == 'last_day_of_cal_month':
            self.end_of_month()
        elif self.recurs == 'last_bus_day_of_cal_month':
            self.end_of_month()
            while not self.dt.weekday() < 6:
               self.dt = self.dt - timedelta(days=1)
        else:
            self.dt = self.dt.replace(year=int(self.dt.year+1))
        return self.dt

class Birthday(RecurringEvent):
    """
    An anniversary for someone's birthday, recurring every year
    """
    def __init__(self,bday):
        self.bday = bday

        self.byear = int(self.bday.split("-")[0])
        self.bmth  = int(self.bday.split("-")[1])
        self.dday  = int(self.bday.split("-")[2])

        self.pyDate = datetime(self.byear, self.bmth, self.dday)
     # birthday needs to come in YYYY-MM-DD format
    
    

    def get_age(self):
        today = datetime.today()
        years = today.year - self.pyDate.year
        if today.month < self.pyDate.month:
            years -= 1
        #yrs = divmod(date_diff,12)
       # years, months = hours, remainder = divmod(date_diff, 365)
        return  years
        #pass

    def get_sign(self, bday):


        #print bmth
        print "Birthday is: :", bday

        if self.bmth < 2: 
            if self.dday < 22:
                results = ZODIAC[10]
            else:
                results = ZODIAC[11]
        elif self.bmth < 3: 
            if self.dday < 20:
                results = ZODIAC[11]
            else:
                results = ZODIAC[12]
        elif self.bmth < 4: 
            if self.dday < 21:
                results = ZODIAC[11]
            else:
                results = ZODIAC[1]
        elif self.bmth < 5: 
            if self.dday < 22:
                results = ZODIAC[1]
            else:
                results = ZODIAC[2]
        elif self.bmth < 6: 
            if self.dday < 21:
                results = ZODIAC[2]
            else:
                results = ZODIAC[3]
        elif self.bmth < 7: 
            if self.dday < 22:
                results = ZODIAC[3]
            else:
                results = ZODIAC[4]
        elif self.bmth < 8: 
            if self.dday < 23:
                results = ZODIAC[4]
            else:
                results = ZODIAC[5]
        elif self.bmth < 9: 
            if self.dday < 24:
                results = ZODIAC[5]
            else:
                results = ZODIAC[6]
        elif self.bmth < 10: 
            if self.dday < 24:
                results = ZODIAC[6]
            else:
                results = ZODIAC[7]
        elif self.bmth < 11: 
            if self.dday < 24:
                results = ZODIAC[7]
            else:
                results = ZODIAC[8]
        elif self.bmth < 12: 
            if self.dday < 22:
                results = ZODIAC[8]
            else:
                results = ZODIAC[9]
        elif self.bmth < 13: 
            if self.dday < 22:
                results = ZODIAC[9]
            else:
                results = ZODIAC[10]
        else:
            results = "The Zodiac Sign Nazi says, 'NO SIGN FOR YOU!!'"

        return results

                

if __name__ == '__main__':
    event = Event("Test Event One", datetime.now(), '23:30')
    print event.eventdate
    print event.eventname
    print event.eventtime
    birth = Birthday('2001-05-31')
    #birth.bday = '2001-01-31'

    zodiac = birth.get_sign(birth.bday)
    age = birth.get_age()
    print "She is", age, "years old!"
    print "Sign is:", zodiac
    recurevnt = RecurringEvent("Test Event One", '2014-07-30', '23:30', 'last_bus_day_of_cal_month')
    print recurevnt.next_event()



