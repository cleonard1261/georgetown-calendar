# gtcal.calendar
# Calendar class and disk functionality
#
# Author:  Benjamin Bengfort <bb830@georgetown.edu>
# Created:
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: calendar.py [] bb830@georgetown.edu $

"""
Calendar class and disk functionality
"""

##########################################################################
## Imports
##########################################################################

import os
import csv

from utils import *
from events import Event
from datetime import datetime
from collections import defaultdict

##########################################################################
## Module constants
##########################################################################

EVENT_FIELDS = ("name", "start", "end", "notes", "location")
CSV_DATETIME = "%Y-%m-%d %H:%M:%S" # e.g. "2014-03-28 09:00:00"

##########################################################################
## Main Calendar App
##########################################################################

class Calendar(object):
    """
    A calender holds and manages events, saving and loading them to disk.
    """

    def __init__(self, path=None):
        self.storage  = defaultdict(lambda: defaultdict(list))
        self.location = path

        if self.location:
            self.load()

    def load(self, path=None):
        """
        Load from the internal storage location or to a new location that
        is specified by this method. Note that load checks if the path
        exists, otherwise it does nothing, refusing to raise an exception.
        """
        # Get the path and check if it exists
        path = path or self.location
        if not os.path.exists(path): return

        # Open the path for reading
        with open(path, 'r') as data:

            # The data is in CSV format with headers, so create a CSV reader
            reader = csv.DictReader(data)

            # Each event is a row in the reader, go through all and load
            for row in reader:
                # Convert datetimes for start and end
                row['start'] = datetime.strptime(row['start'], CSV_DATETIME)
                row['end'] = datetime.strptime(row['end'], CSV_DATETIME)

                # Add the event with the fields in the row
                self.add_event(**row)

    def save(self, path=None):
        """
        Save the calendar from internal storage location or to a new
        location that is specified by this method.
        """
        # Get the path
        path = path or self.location

        # Open the file for writing
        with open(path, 'w') as data:

            # Create a writer that knows how to write Events
            writer = csv.DictWriter(data, fieldnames=EVENT_FIELDS)
            writer.writeheader()    # Write the header fields

            # Iterate through each year in our storage
            for year in self.storage:
                # Iterate through each day per year
                for day in self.storage[year]:
                    # Iterate through each event per day
                    for event in self.storage[year][day]:
                        # Create a dictionary from the event
                        row = dict(zip(EVENT_FIELDS, map(lambda f: getattr(event, f), EVENT_FIELDS)))
                        # Write the Dictionary as a CSV row
                        writer.writerow(row)

    def add_event(self, **kwargs):
        """
        Adds an event by creating the event with the arbitrary list of
        arguments that is passed into this method, then stores it according
        to the year and the day in our internal storage.
        """
        event = Event(**kwargs)                         # Create event
        year_key, day_key = get_dtkey(event.start)      # Get the year, day
        self.storage[year_key][day_key].append(event)   # Store the event
        return event

    def todays_agenda(self):
        """
        Creates a nice print out of the agenda for today
        """
        today     = datetime.today()          # What day is today?
        year, day = get_dtkey(today)          # Get the keys of our storage
        events    = self.storage[year][day]   # Get the events out of storage

        # Check if we have anything
        if not events:
            return "No events scheduled for today!"

        # Otherwise, start creating agenda
        output = []

        # Create a nice agenda header
        output.append("Agenda for %s:" % today.strftime("%B %d, %Y"))
        output.append("    You have %i events" % len(events))
        output.append("=" * len(output[0]))
        output.append("") # This will create a blank line

        for event in events:
            output.append(event.pprint(date_format="%I:%M %p"))
            output.append("-" * len(output[0]))
            output.append("") # This will create a blank line

        return "\n".join(output)

    def __len__(self):
        numevents = 0
        for year in self.storage:
            for day in self.storage[year]:
                numevents += len(self.storage[year][day])
        return numevents

    def __str__(self):
        output = str(self.__class__.__name__)
        if self.location:
            output += " at %s" % self.location
        output += " with %i events" % (len(self))
        return output
