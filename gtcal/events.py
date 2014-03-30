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

from datetime import datetime
from datetime import timedelta


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

    def __init__(self):
        pass

    def __str__(self):
        pass

class RecurringEvent(Event):
    """
    Event that repeats for a fixed amount of time.
    """

    def __init__(self):
        pass

    def next_event(self):
        pass

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
                print ZODIAC[10]
            else:
                print ZODIAC[11]
        elif self.bmth < 3: 
            if self.dday < 20:
                print ZODIAC[11]
            else:
                print ZODIAC[12]
        elif self.bmth < 4: 
            if self.dday < 21:
                print ZODIAC[11]
            else:
                print ZODIAC[1]
        elif self.bmth < 5: 
            if self.dday < 22:
                print ZODIAC[1]
            else:
                print ZODIAC[2]
        elif self.bmth < 6: 
            if self.dday < 21:
                print ZODIAC[2]
            else:
                print ZODIAC[3]
        elif self.bmth < 7: 
            if self.dday < 22:
                print ZODIAC[3]
            else:
                print ZODIAC[4]
        elif self.bmth < 8: 
            if self.dday < 23:
                print ZODIAC[4]
            else:
                print ZODIAC[5]
        elif self.bmth < 9: 
            if self.dday < 24:
                print ZODIAC[5]
            else:
                print ZODIAC[6]
        elif self.bmth < 10: 
            if self.dday < 24:
                print ZODIAC[6]
            else:
                print ZODIAC[7]
        elif self.bmth < 11: 
            if self.dday < 24:
                print ZODIAC[7]
            else:
                print ZODIAC[8]
        elif self.bmth < 12: 
            if self.dday < 22:
                print ZODIAC[8]
            else:
                print ZODIAC[9]
        elif self.bmth < 13: 
            if self.dday < 22:
                print ZODIAC[9]
            else:
                print ZODIAC[10]
        else:
            print "The Zodiac Sign Nazi says, 'NO SIGN FOR YOU!!'"

                

if __name__ == '__main__':
    #event = Event("Data Class", datetime.now(), datetime.now(),None, None)
    birth = Birthday('2001-05-31')
    #birth.bday = '2001-01-31'

    birth.get_sign(birth.bday)
    age = birth.get_age()
    print "She is", age, "years old!"



