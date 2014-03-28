# gtcal.utils
# Utility functions for calendar app
#
# Author:  Benjamin Bengfort <bb830@georgetown.edu>
# Created: Thu Mar 27 21:34:59 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: utils.py [] bb830@georgetown.edu $

"""
Utility functions for calendar app
"""

##########################################################################
## Imports
##########################################################################

import os
import json

from events import Event
from datetime import datetime

##########################################################################
## File path helper functions
##########################################################################

def makepath(path=None):
    """
    Returns the absolute path of the URI passed in, ensuring that the path
    exists at the given location and that there will be no conflicts in
    creating or editing the file there, e.g. it will make all the
    directories associated with the path.
    """
    path = path or "test.txt"
    path = os.path.expanduser(path)
    path = os.path.expandvars(path)
    path = os.path.abspath(path)

    if not os.path.exists(path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    return path

##########################################################################
## Time and Date helper functions
##########################################################################

def get_dtkey(dt):
    """
    Returns a tuple with the year and day of the year (counting from Jan 1)
    and this data structure is enough to identify a unique day, which is
    used as a key in our storage format.
    """
    return dt.year, dt.timetuple().tm_yday

##########################################################################
## JSON Encoder and Decoder classes
##########################################################################

class CalendarEncoder(json.JSONEncoder):
    """
    Custom encoder that handles datetimes.
    """

    JSON_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(self.JSON_FORMAT)
        elif isinstance(obj, Event):
            return {
                "type": obj.__class__.__name__,
                "name": obj.name,
                "start": obj.start,
                "end": obj.end,
                "notes": obj.notes,
                "location": obj.location
            }
        elif hasattr(obj, 'next'):
            return list(obj)
        else:
            return super(CalendarEncoder, self).default(obj)

class CalendarDecoder(json.JSONDecoder):
    """
    Custom encoder that handles datetimes.
    """

    JSON_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    def decode(self, s):
        try:
            return datetime.strptime(s, self.JSON_FORMAT)
        except ValueError:
            return super(CalendarDecoder, self).decode(s)
