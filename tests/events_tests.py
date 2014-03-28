# tests.events_tests
# Testing for the events of the gtcal
#
# Author:   Benjamin Bengfort <bb830@georgetown.edu>
# Created:  Thu Mar 27 22:41:13 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: events_tests.py [] bb830@georgetown.edu $

"""
Testing for the events of the gtcal
"""

##########################################################################
## Imports
##########################################################################

import unittest
from gtcal.events import *
from datetime import datetime, timedelta

##########################################################################
## Imports
##########################################################################

class EventTests(unittest.TestCase):

    def test_event_string(self):
        """
        Check that an event prints nicely
        """
        event = Event(
            name  = "Software Engineering for Data",
            start = datetime(2014, 3, 28, 18, 00),
            end   = datetime(2014, 3, 28, 21, 00),
            location = "640 Massachusetts Ave; Washington D.C.",
            notes = "Second course of Data Analytics certificate"
        )

        self.assertTrue(str(event))

    def test_event_duration(self):
        """
        Test the duration method of an event
        """
        event = Event(
            name  = "Software Engineering for Data",
            start = datetime(2014, 3, 28, 18, 00),
            end   = datetime(2014, 3, 28, 21, 00),
            location = "640 Massachusetts Ave; Washington D.C.",
            notes = "Second course of Data Analytics certificate"
        )

        # Test hours
        self.assertEqual(event.duration(), "3.00 hours")

        # Test days
        event.end = datetime(2014, 3, 30, 21, 00)
        self.assertEqual(event.duration(), "2 days")

        # Test minutes
        event.end = datetime(2014, 3, 28, 18, 30)
        self.assertEqual(event.duration(), "30 minutes")

class RecurringEventTests(unittest.TestCase):

    def test_all_events(self):
        """
        Check that the recurring events can come up with recurrence
        """
        event = RecurringEvent(
            name     = "Software Engineering for Data",
            start    = datetime(2014, 3, 28, 18, 00),
            end      = datetime(2014, 3, 28, 21, 00),
            occurs   = 4,
            interval = 7,
            location = "640 Massachusetts Ave; Washington D.C.",
            notes    = "Second course of Data Analytics certificate"
        )
        self.assertEqual(len(list(event.all_events())), event.occurences)

    def test_next_event_middle(self):
        """
        Test that the next event is calculated
        """
        yesterday = datetime.today() - timedelta(days=1)
        event = RecurringEvent(
            name     = "Software Engineering for Data",
            start    = yesterday,
            end      = yesterday + timedelta(seconds=3600),
            occurs   = 3,
            interval = 1,
            location = "640 Massachusetts Ave; Washington D.C.",
            notes    = "Second course of Data Analytics certificate"
        )

        self.assertIsNotNone(event.next_event())
        self.assertGreater(event.next_event().start, yesterday)

    def test_next_event_none(self):
        """
        Test that next event returns None when exhausted
        """
        yesterday = datetime.today() - timedelta(days=5)
        event = RecurringEvent(
            name     = "Software Engineering for Data",
            start    = yesterday,
            end      = yesterday + timedelta(seconds=3600),
            occurs   = 3,
            interval = 1,
            location = "640 Massachusetts Ave; Washington D.C.",
            notes    = "Second course of Data Analytics certificate"
        )

        self.assertIsNone(event.next_event())

class BirthdayTests(unittest.TestCase):

    def test_get_age(self):
        """
        Check birthday can calculate age
        """
        bday  = Birthday("Ben", datetime(1984, 04, 07))
        today = datetime.today()

        age   = (today - bday.start).days / 365
        self.assertEqual(bday.get_age(), age)

    def test_next_event(self):
        """
        Ensure that the next event is this year (e.g. coming up)
        """
        today = datetime.today()
        bday  = Birthday("Joe", datetime(1973, today.month, today.day) + timedelta(days=2))
        nbday = bday.next_event()

        self.assertEqual(today.year, nbday.start.year)

    def test_next_year_event(self):
        """
        Ensure that the next event is next year (e.g. already passed)
        """
        today = datetime.today()
        bday  = Birthday("Anne", datetime(1992, today.month, today.day) - timedelta(days=2))
        nbday = bday.next_event()

        self.assertEqual(today.year+1, nbday.start.year)

    def test_all_events(self):
        """
        Ensure length of all events is same as age
        """
        bday = Birthday("Barb", datetime(1983, 10, 21))
        print list(bday.all_events())
        self.assertEqual(len(list(bday.all_events())), bday.get_age()+1)
