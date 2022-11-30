# AutomatedScheduling

Python Script that pulls interviwer availability from Google Calendar and patient availability from REDCap to find and schedule compatible sessions. 

REDCap patient availability is in %Y-%m-%dgen_avail_%a___%H%M format. Value is either 0 or 1 in REDCap report. 

Interviwer availability is determined by presence of string "Participant" in google calendar event. 



Must create config.py - REDCap and GoogleCalendar API Credentials
