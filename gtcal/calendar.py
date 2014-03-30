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

    def __init__(self, eventname, eventdate, eventtime):
        checkin_date = datetime.datetime.now()
        event = Event(eventname, eventdate, eventtime)
        print event.eventdate
        print event.eventname
        print event.eventtime

    
    def load(self):
        pass

    def save(self):
        pass

    def add_event(self):
        pass

    def remove_event(self):
        pass

    def update_event(self):
        pass

    def todays_agenda(self):
        pass

    def order_agenda(self):
        pass

if __name__ == '__main__':
    cal = Calendar("Cal Test Event", '2013-03-30', "13:30")
    


