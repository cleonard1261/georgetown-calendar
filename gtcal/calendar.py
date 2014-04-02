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
import dateutil
#from events import Event
#from datetime import datetime
import datetime
import csv
#from events import *

##########################################################################
## Main Calendar App
##########################################################################

class Calendar(object):
    """
    A calender holds and manages events, saving and loading them to disk.
    """

    def __init__(self, calname):
        checkin_date = datetime.now()
        self.calname = calname


    
    def load(self, calname):
        pass

    def save(self, csvfile):
        csvfile.close()

    def calopen(self, calname):
        with open(calname+'.csv', 'wb') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
        return csvfile

    def add_event(self, Event):
        pass

    def remove_event(self):
        file_name = 'C:\Temp\my_file.csv'
        output_file = 'C:\Temp\new_file.csv'
        csv_file = open(file_name, 'r')
        ## note that the index of the year column is excluded
        column_indices = [0,1,3,4]
        with open(output_file, 'w') as fh:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
               tmp_row = []
               for col_inx in column_indices:
                   tmp_row.append(row[col_inx])
               fh.write(','.join(tmp_row))
        # see below for ideas on reading in csv file and writing to a temp file.
        # http://stackoverflow.com/questions/7588934/deleting-columns-in-a-csv-with-python
        # see jointest.py for os.system commads to rm the old file

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


