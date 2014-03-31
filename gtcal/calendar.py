#!/usr/bin/python
# gitcal.calendar
# Calendar class and disk functionality
#
# Author: Chad Leonard
# Created: 20140330
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: calendar.py [] @georgetown.edu $

"""
Calendar class and disk functionality
"""

##########################################################################
## Imports
##########################################################################
from events import Event
#from datetime import datetime
import datetime
import csv

##########################################################################
## Main Calendar App
##########################################################################

class Calendar(object):
    """
    A calender holds and manages events, saving and loading them to disk.
    """

    def __init__(self, calname):
        checkin_date = datetime.datetime.now()
        self.calname = calname


    
    def load(self, calname):
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    def save(self, csvfile):
        csvfile.close()

    def calopen(self, calname):
        with open(calname+'.csv', 'wb') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
        return csvfile

    def add_event(self, Event):
        csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    def remove_event(self):
        pass

    def update_event(self):
        pass

    def todays_agenda(self):
        pass

    def order_agenda(self):
        pass

if __name__ == '__main__':
    cal = Calendar("CalendarOne")
    print cal.calname
    csvfile = cal.calopen(cal.calname)
    event = Event("Cal Test Event", '2013-03-30', "13:30")
    cal.add_event(event)
    cal.save(csvfile)


