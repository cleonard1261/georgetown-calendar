# gtcal.events
# Events class hierarchy
#
# Author:  Benjamin Bengfort <bb830@georgetown.edu>
# Created:
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: events.py [] bb830@georgetown.edu $

"""
Events class hierarchy
"""

##########################################################################
## Imports
##########################################################################

from datetime import datetime, timedelta

##########################################################################
## Module Constants
##########################################################################

## Format dates and times as strings
SHORT_DATE    = "%m/%d/%Y"
LONG_DATE     = "%B %d, %Y"
TIME_FORMAT   = "%I:%M %p"
LONG_DATETIME = "%B %d, %Y at %I:%M %p"

##########################################################################
## Event Classes
##########################################################################

class Event(object):
    """
    Base event class that contains all properties and behavior of events.
    """

    def __init__(self, name, start, end, notes=None, location=None):
        self.name  = name
        self.start = start
        self.end   = end
        self.notes = notes
        self.location = location

    def duration(self):
        """
        Calculates how long the event will be in hours.
        """
        delta = self.end - self.start # This returns a time delta object

        # If event is in days, return days
        if delta.days > 0:
            return "%i days" % delta.days

        # Attempt to report delta in meaningful time unit
        if delta.seconds >= 3600:
            hours = delta.seconds / 3600.0
            return "%0.2f hours" % hours
        else:
            minutes = delta.seconds / 60
            return "%i minutes" % minutes

    def pprint(self, date_format=LONG_DATETIME, verbosity=3):
        """
        Pretty print the event, with a format for start and end dates as
        well as with a verbosity that indicates how much to print.
        """
        if verbosity == 0:
            # Simplest, shortest representation
            return "%s on %s" % (self.name, self.start.strftime(date_format))

        output = []
        if verbosity > 0:
            output = []
            output.append(self.name)
            output.append("from %s to %s" % (self.start.strftime(date_format), self.end.strftime(date_format)))

        if verbosity > 1:
            output.append("(%s)" % self.duration())
            if self.location:
                output.append("at %s" % self.location)

        if verbosity > 2:
            if self.notes:
                output.append("")
                output.append("Notes:")
                output.append(self.notes)

        return "\n".join(output)

    def __str__(self):
        return self.pprint(verbosity=0)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.pprint(verbosity=0))

class RecurringEvent(Event):
    """
    Event that repeats for a fixed amount of time.
    """

    def __init__(self, name, start, end, occurs=1, interval=1, notes=None, location=None):

        super(RecurringEvent, self).__init__(name, start, end, notes, location)
        # Interval is in days, e.g. 2 is every other day and 7 is every week
        self.interval   = interval
        self.occurences = occurs

    def all_events(self):
        """
        Returns a list of normal events for all events
        """
        for idx in xrange(0, self.occurences):
            days  = timedelta(days=self.interval*idx)
            start = self.start + days
            end   = self.end + days
            event = Event(self.name, start, end, self.notes, self.location)
            yield event

    def next_event(self):
        """
        Returns the next upcoming event date (doesn't care about past
        events)
        """
        today = datetime.now()
        for event in self.all_events():
            if event.start > today:
                return event
        return None

class Birthday(RecurringEvent):
    """
    An anniversary for someone's birthday, recurring every year
    """

    def __init__(self, person, birthday):
        super(Birthday, self).__init__(
            name     = "%s's Birthday" % person,
            start    = birthday,
            end      = birthday + timedelta(days=1),
            occurs   = 100,
            interval = 365,
        )

    def get_age(self):
        """
        Returns the age of the person
        """
        today = datetime.today()
        delta = today - self.start
        return delta.days / 365

    def all_events(self):
        """
        Returns a generator of all birthdays
        """
        # parameters
        today = datetime.today()
        month = self.start.month
        day   = self.start.day
        bday  = datetime(self.start.year, month, day)

        # while loop
        while bday < today:
            yield Event(
                name  = self.name,
                start = bday,
                end   = bday + timedelta(days=1),
            )

            bday = datetime(bday.year+1, month, day)

    def next_event(self):
        """
        No need to iterate, just replace years here.
        """
        today = datetime.today()
        bday  = datetime(today.year, self.start.month, self.start.day)
        if bday < today:
            bday = bday.replace(year=today.year+1)

        return Event(
            name  = self.name,
            start = bday,
            end   = bday + timedelta(days=1),
        )

