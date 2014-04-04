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

from datetime import datetime
#import datetime
import csv
import os

##########################################################################
## Global Variables
##########################################################################



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

    def save(self, csvfile):
        csvfile.close()

    def add_event(self, event, calname):
		 with open(calname+'.csv', 'a') as csvfile:
			 self.csvwriter = csv.writer(csvfile, dialect='excel', delimiter='|')
			 self.csvwriter.writerow([event.eventdate]+[event.eventname]+[event.eventtime])
		 return csvfile

    def remove_event(self, eventdate, eventname, calname):
        file_dir = '/Users/chadleonard/venv/calendar_app/georgetown_calendar/gtcal/'
        file_name = file_dir+calname+'.csv'
        output_file = file_dir+calname+'Temp.csv'
        input_file = open(file_name, 'r')
        with open(output_file, 'wb') as csvfile:
			self.csvwriter = csv.writer(csvfile, dialect='excel', delimiter='|')
			reader = csv.reader(input_file, delimiter='|', quoting=csv.QUOTE_NONE)
			for row in reader:
				if event.eventdate in [row][0]:
				   if event.eventtime in [row][0]:
				      continue
				   else:
				       self.csvwriter.writerow([row][0])
				else:
				    self.csvwriter.writerow([row][0])
        input_file.close()
        csvfile.close()	
        cmd = 'mv ' + output_file+' '+file_name		
        os.system(cmd)
				
				

        # see below for ideas on reading in csv file and writing to a temp file.
        # http://stackoverflow.com/questions/7588934/deleting-columns-in-a-csv-with-python
        # see jointest.py for os.system commads to rm the old file

    def update_event(self,eventdate, eventname, eventtime, calname):
        file_dir = '/Users/chadleonard/venv/calendar_app/georgetown_calendar/gtcal/'
        file_name = file_dir+calname+'.csv'
        output_file = file_dir+calname+'Temp.csv'        
        input_file = open(file_name, 'r')
        with open(output_file, 'wb') as csvfile:
			self.csvwriter = csv.writer(csvfile, dialect='excel', delimiter='|')
			reader = csv.reader(input_file, delimiter='|', quoting=csv.QUOTE_NONE)
			for row in reader:
				if eventdate in [row][0]:
				   if eventtime in [row][0]:
				      self.csvwriter.writerow([eventdate]+[eventname]+[eventtime])
				   else:
				       self.csvwriter.writerow([row][0])
				else:
				    self.csvwriter.writerow([row][0])
        input_file.close()
        csvfile.close()	
        cmd = 'mv ' + output_file+' '+file_name		
        os.system(cmd)


    def todays_agenda(self, eventdate, calname):
        file_dir = '/Users/chadleonard/venv/calendar_app/georgetown_calendar/gtcal/'
        file_name = file_dir+calname+'.csv'    
        input_file = open(file_name, 'r')
        reader = csv.reader(input_file, delimiter='|', quoting=csv.QUOTE_NONE)
        agenda = []
        for row in reader:
			if eventdate in [row][0]:
				agenda.append([row][0])
			else:
				continue
        input_file.close()
        return agenda

    def order_agenda(self):
        pass

if __name__ == '__main__':
    from events import Event
    cal = Calendar("CalendarOne")
    print cal.calname
    #csvfile = cal.calopen(cal.calname)

    event = Event("Cal Test Event", '2013-03-30', "13:30")
    event1 = Event("Cal Test Event One", '2014-04-02', "11:30")
    event2 = Event("Cal Test Event Two", '2014-04-02', "14:30")
    print event1.eventname
    csvfile = cal.add_event(event, cal.calname)
    cal.save(csvfile)
    csvfile = cal.add_event(event1, cal.calname)
    cal.save(csvfile)
    csvfile = cal.add_event(event2, cal.calname)
    cal.save(csvfile)
    cal.remove_event(event1.eventdate, event1.eventname, cal.calname)
    cal.update_event(event2.eventdate, "Cal Prod Event Two", event2.eventtime, cal.calname)
    agenda = cal.todays_agenda(event2.eventdate, cal.calname)
    for i in agenda:
        print i[0]+',', i[1]+',',i[2]



