# -*- coding: utf-8 -*-
import caldav
import os
from caldav.elements import dav
from datetime import datetime, timedelta, time
today  = datetime.combine(datetime.today(), time(0,0))
# Caldav url
# Works on both Win or Linux
username = os.environ.get('_siNextcloudUser')
password = os.environ.get('_siNextcloudPW')

url = "https://" + username + ":" + password + "@next.social-robot.info/nc/remote.php/dav"

#vcal = """BEGIN:VCALENDAR
#VERSION:2.0
#PRODID:-//Example Corp.//CalDAV Client//EN
#BEGIN:VEVENT
#UID:1234567890
#DTSTAMP:20100510T182145Z
#DTSTART:20100512T170000Z
#DTEND:20100512T180000Z
#SUMMARY:This is an event
#END:VEVENT
#END:VCALENDAR
#"""

# example event object
#<VCALENDAR| [<VERSION{}2.0>, <CALSCALE{}GREGORIAN>, 
#             <PRODID{}-//Sabre//Sabre VObject 4.1.6//EN>, 
#             <VEVENT| [<UID{}e8e55e25-1d7c-4bc5-a115-29480d076a30>, 
#                       <DTSTART{}2020-02-17 09:30:00+00:00>, 
#                       <DTEND{}2020-02-17 10:50:00+00:00>, 
#                       <CREATED{}2020-02-16 19:53:30+00:00>, 
#                       <DTSTAMP{}2020-02-16 19:54:08+00:00>, 
#                       <LAST-MODIFIED{}2020-02-16 19:54:08+00:00>, 
#                       <SEQUENCE{}2>, 
#                       <SUMMARY{}Testtermin>]>]>

# open connection to calendar
client = caldav.DAVClient(url)
principal = client.principal()
# get all available calendars (for this user)
calendars = principal.calendars()

# check the calendar events and parse results..

if len(calendars) > 0:
  calendar = calendars[0]
  events = calendar.date_search(today, datetime.combine(today, time(23,59,59,59))) #Events am heutigen Tag

  if len(events) == 0:
    print("No events today!")
  else:
    print("Total {num_events} events:".format(num_events=len(events)))

    for event in events:
      event.load()
      e = event.instance.vevent
      if e.dtstart.value.strftime("%H:%M") == "00:00":
        # Überprüfung von ganztägigen Events
        eventTime = e.dtstart.value.strftime("%D")
        print("{eventTime} {eventSummary}".format(eventTime=eventTime, eventSummary=e.summary.value))
      else:
        # This is a "normal" event
        eventTime = e.dtstart.value.strftime("%H:%M")
        print("{eventTime} {eventSummary})".format(eventTime=eventTime, eventSummary=e.summary.value))

  eventsWeekly = calendar.date_search(start=datetime(2021, 1, 11),
                                      end=datetime(2021, 1, 17))  # Bisher Hardcode für die Woche

  if len(eventsWeekly)== 0:
    print("No events this week")
    #Hier kann man das Hinzufügen erstellen
    #addAppointmentNextWeek()
  else:
    print("Number of events this week: {numberEvents}".format(numberEvents = len(eventsWeekly)))
    for eventW in eventsWeekly:
      eventW.load()
      eW = eventW.instance.vevent
      # Überprüfung von ganztägigen Events
      if eW.dtstart.value.strftime("%H:%M") == "00:00":
        eventTime = eW.dtstart.value.strftime("%D") # Änderen der Startzeit als das Datums
        print("{eventTime} {eventSummary} ".format(eventTime=eventTime, eventSummary=eW.summary.value))
      else:
        eventTime = eW.dtstart.value.strftime("%H:%M")
        print("{eventTime} {eventSummary})".format(eventTime=eventTime, eventSummary=eW.summary.value))

#def addAppointmentNextWeek():
 # if(len(eventsWeekly)==0):
#    my_event = calendar.save_event("""BEGIN:VCALENDAR
#    VERSION:2.0
#    PRODID:-//Example Corp.//CalDAV Client//EN
#    BEGIN:VEVENT
#    UID:20200516T060000Z-123401@example.com
#    DTSTAMP:20210116T060000Z
#    DTSTART:20210117T060000Z
#    DTEND:20201017T230000Z
#    RRULE:FREQ=YEARLY
#    SUMMARY:Do the needful
#    END:VEVENT
#    END:VCALENDAR
#    """)
#  return my_event
