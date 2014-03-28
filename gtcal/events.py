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

    def __init__(self):
        pass

    def get_age(self):
        pass
