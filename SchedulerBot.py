import datetime
import json
import pdb

import pytz

from ParticipantAvailability import ParticipantAvailability
from GoogleCalendarClient import GoogleCalendarClient
from InterviewSessions import InterviewSessions
from RedCapClient import RedCapClient
from utils import weekday_converter, timezone_converter, interviewer_email_converter
from pytz import timezone
import pandas as pd
import calendar


cst = pytz.timezone('US/Central')


def getAvailableParticipantSessions(number_of_weeks):
    """
    Function to determine all available 1-hour sessions for patient in the REDCap project that needs to have an
    interview scheduled

    Parameters
    ----------
    @param data: JSON
        REDCap project report (general availability)

    @return:
        final_participant_availability: list[ParticipantAvailability]
            list of all available 1-hour sessions for each patient for the next 7 days
    """
    # csv_file = '/study/bewell/raw-data/redcap/bewell__base.csv'

    csv_file = 'bewell__base.csv'
    data = pd.read_csv(csv_file)
    participant_availability = []
    session = []
    today = datetime.datetime.today()
    data = data.set_index(data['webscreen_id'])

    # for participant in data.iterrows():
    # print(f"type: {type(participant)}\tparticipant: {participant}")

    # prompt user until user inputs valid participant webscreen id
    participant = None
    while participant is None:
        try:
            participant_webscreen_id = int(input("Enter webscreen id of participant you would like to schedule: \n"))
            participant = data.loc[participant_webscreen_id]
        except (KeyError):
            print(f"Invalid Participant Webscreen ID, please try again")

    for key, val in participant.items():
        if "webscreen_id" in key:
            webscreen_id = val
        if "gen_avail_time_zone" in key and isinstance(val, str):
            participant_timezone = timezone(timezone_converter[val])

    participant = dict(participant)
    ga_values = list(participant.values())
    ga_keys = list(participant.keys())

    # for all times, check if patient is available during that time
    for i in range(len(ga_keys)):
        if "time_zone" not in ga_keys[i] and "gen_avail" in str(ga_keys[i]) and "gen_avail" in ga_keys[i] and "gen_avail" in ga_keys[i+1] and "gen_avail" in ga_keys[i + 2]:

            # if patient is available for 3 consecutive 30 minute time blocks, add session to participant availability
            count = int(ga_values[i]) + int(ga_values[i + 1]) + int(ga_values[i + 2])
            # print(count)
            if count == 3:
                session.append(ga_keys[i])
                session.append(ga_keys[i + 1])
                session.append(ga_keys[i + 2])
                # add copy of session to
                participant_availability.append(session.copy())
                session.clear()

        final_participant_availability = []

    for start, middle, end in participant_availability:

        # print(f"\n\nstart: {start}\nmidele: {middle}\nend: {end}\n\n")

        start_day_num = weekday_converter[start[10:13]]
        end_day_num = weekday_converter[end[10:13]]
        origin_day = today.day + (7 * number_of_weeks)

        # print(f"Origin_day: {origin_day}\nstart_day_num: {start_day_num}\nend_day_num: {end_day_num}\ntoday.weekday(): {today.weekday()}")

        if today.weekday() < start_day_num:
            start_day = start_day_num - today.weekday()
            start_day = start_day + origin_day
        elif today.weekday() > start_day_num:
            start_day = (7 - today.weekday() + start_day_num)
            start_day = start_day + origin_day
        else:
            start_day = origin_day

        if today.weekday() < end_day_num:
            end_day = end_day_num - today.weekday()
            end_day = end_day + origin_day
        elif today.weekday() > end_day_num:
            end_day = (7 - today.weekday() + end_day_num)
            end_day = end_day + origin_day
        else:
            end_day = origin_day

        # print(f"\n\nOrigin_day: {origin_day}\nstart_day: {start_day}\nend_day: {end_day}")

        start_year_month_day = str(datetime.datetime.utcnow())[0:7] + str("-" + str(start_day))
        end_year_month_day = str(datetime.datetime.utcnow())[0:7] + str("-" + str(end_day))

        # print(f"\n\nstart_year_month_day: {start_year_month_day}\nend_year_month_day: {end_year_month_day}")

        str_start_year = start_year_month_day[0:4]
        str_start_month = start_year_month_day[5:7]

        str_end_year = end_year_month_day[0:4]
        str_end_month = end_year_month_day[5:7]

        days_in_month = int(calendar.monthrange(int(str_start_year), int(str_start_month))[1])

        # print(f"\n\ndays_in_month: {days_in_month}")

        if int(start_day) > days_in_month:
            str_start_month = str(int(str_start_month) + 1)
            # str_start_day = (start_day_num - today.weekday()) - (days_in_month - origin_day)
            str_start_day = start_day - days_in_month
            start_year_month_day = f"{str_start_year}-{str_start_month}-{str_start_day}"

        if int(end_day) > days_in_month:
            str_end_month = str(int(str_end_month) + 1)
            # str_end_day = (end_day_num - today.weekday()) - (days_in_month - origin_day)
            str_end_day = end_day - days_in_month
            end_year_month_day = f"{str_end_year}-{str_end_month}-{str_end_day}"

        # print(f"\n\nstart_day: {start_day}\tdays_in_month: {days_in_month}\nstart_day_num: {start_day_num}\ttoday.weekday(): {today.weekday()}")
        # print(f"\n\nstart_year_month_day: {start_year_month_day}\tend_year_month_day: {end_year_month_day}")

        start_datetime = participant_timezone.localize(
            datetime.datetime.strptime(f"{start_year_month_day}{start}", "%Y-%m-%dgen_avail_%a___%H%M"))
        end_datetime = participant_timezone.localize(
            datetime.datetime.strptime(f"{end_year_month_day}{end}", "%Y-%m-%dgen_avail_%a___%H%M"))

        # print(
        # f"start_datetime.tzinfo: {start_datetime.tzinfo}\tstart_datetime: {start_datetime}\tend_datetime.tzinfo: {end_datetime.tzinfo}\tend_datetime: {end_datetime}\n")

        start_datetime = start_datetime.astimezone(pytz.utc)
        end_datetime = end_datetime.astimezone(pytz.utc)

        # print(
        #     f"start_datetime.tzinfo: {start_datetime.tzinfo}\tstart_datetime: {start_datetime}\tend_datetime.tzinfo: {end_datetime.tzinfo}\tend_datetime: {end_datetime}\n")

        participant = ParticipantAvailability(webscreen_id, participant_timezone, start_datetime, end_datetime)

        # print(participant.__str__())
        # print(f"{participant}\n")

        final_participant_availability.append(participant)

        # print(f"final_participant_availability: {final_participant_availability}")

    return final_participant_availability


def getAvailableInterviewSessions(self, participant_availability):
    """
    Function to determine compatible sessions between patients and interviewers in calendar
    @param self:
        self.Calendar: GoogleCalendar
    @param participant_availability: list[ParticipantAvailability]
    @return:
        interview_sessions: list[InterviewSessions]
    """
    print('\t\t\t\t\t~~~~Finding compatible sessions~~~~\n\n')
    if not self.calendar.get_events():
        print('No upcoming events found.')
        return
    compatible_session_count = 0
    # iterate through all sessions where patient is available
    for participant in participant_availability:
        # print(self.calendar)
        for event in self.calendar.get_events(participant.start, order_by='startTime', single_events=True):
            try:
                if isinstance(event.summary, str) and "participant" in event.summary.lower():
                    event_start = event.start + datetime.timedelta(minutes=15)
                    event_end = event.end

                    # print(f"Event Summary: {event.summary}")
                    # print(
                    #     f"Participant Start: {participant.getStart()}\tParticipant End: {participant.getEnd()}\nInterviwer Start: {event_start}\tInterviwer End:{event_end}\n")

                    if participant.getStart() >= event_start and participant.getEnd() <= event_end:
                        compatible_session_count += 1
                        # print(f"\nparticipant.getStart(): {participant.getStart()}\nevent_start: {event_start}\nparticipant.getEnd(): {participant.getEnd()}\nevent_end: {event_end}")

                        print("\n\n~~~~~~~~~~~~~~~~~~~~POSSIBLE "
                              "INTERVIEW TIME DETAILS~~~~~~~~~~~~~~~~~~~~\n")
                        print(f"WebscreenID: {participant.webscreen_id}\n\n\t\t\t~~~~~~~~~~Google Calendar Event~~~~~~~~~~\n\n{event.summary}\n\nStart: {event.start.astimezone(cst).strftime('%Y-%m-%d %I:%M%p')}\t\t\t\tEnd: {event.end.astimezone(cst).strftime('%Y-%m-%d %I:%M%p')}")

                        # print(f"\n\t\t\t\t~~~~~~~~~~UTC TIMEZONE~~~~~~~~~~\n")
                        # print(
                        #     f"Participant Start: {participant.getStart()}\tParticipant End: {participant.getEnd()}\nInterviwer Start: {event_start}\tInterviwer End:{event_end}\n")
                        # print(
                        #     f"Interview Session Interval\nStart:  {participant.getStart()}\tEnd: {participant.getEnd()}\n")

                        print(f"\n\t\t\t\t~~~~~~~~~~CST TIMEZONE~~~~~~~~~~\n")
                        print(
                            f"Participant Availability\nStart: {participant.getStart().astimezone(cst).strftime('%I:%M%p')}\t\tEnd: {participant.getEnd().astimezone(cst).strftime('%I:%M%p')}\n\nInterviwer Availability\nStart: {event_start.astimezone(cst).strftime('%I:%M %p')}\t\tEnd: {event_end.astimezone(cst).strftime('%I:%M%p')}\n")
                        print(
                            f"Compatible Interview Session Interval\nStart:  {participant.getStart().astimezone(cst).strftime('%I:%M%p')}\t\tEnd: {participant.getEnd().astimezone(cst).strftime('%I:%M%p')}\n")

                        print(f"\n\t\t\t\t~~~~~~~~~~{str(participant.getTimezone())} TIMEZONE~~~~~~~~~~\n")
                        print(
                            f"Participant Availability\nStart: {participant.getStart().astimezone(participant.getTimezone()).strftime('%I:%M%p')}\t\tEnd: {participant.getEnd().astimezone(participant.getTimezone()).strftime('%I:%M%p')}\n\nInterviewer Availability\nStart: {event_start.astimezone(participant.getTimezone()).strftime('%I:%M%p')}\t\tEnd:{event_end.astimezone(participant.getTimezone()).strftime('%I:%M%p')}\n")
                        print(
                            f"Compatible Interview Session Interval\nStart:  {participant.getStart().astimezone(participant.getTimezone()).strftime('%I:%M%p')}\t\tEnd: {participant.getEnd().astimezone(participant.getTimezone()).strftime('%I:%M%p')}\n")

                        # interviewer_name = event.summary.split()[0]
                        #
                        # interviewer_email = interviewer_email_converter[interviewer_name]
                        # participant_start = participant.getStart().astimezone(cst)
                        # participant_end = participant.getEnd().astimezone(cst)
                        #
                        # interview_session = InterviewSessions(event, participant, interviewer_name, interviewer_email,
                        #                                       participant_start, participant_end)
                        # interview_sessions.append(interview_session)

            except (TypeError, AttributeError) as error:
                # print(error)
                break
    if compatible_session_count == 0:
        print('\t\t\t\t\t~~~~NO compatible sessions found :( ~~~~\n\n')
    # print(interview_sessions)

    return

    # return interview_sessions


#
# def uploadToREDCap(self):
#     # export scheduledInterview record data from REDCap
#     data = self.exportInterviewRecord()
#     # update scheduledInterview record
#
#     # for key, val in data.items():
#     #     if "webscreen_id" in key:
#     #         print(val)
#         # print(f"Key: {key}\nVal: {val}")
#     # import scheduledInterview record into REDCap

class SchedulerBot(GoogleCalendarClient, RedCapClient):
    """
    A class that utilizes the inherited methods from Google Calendar and REDCap client classes to find
    compatible schedules between the study participants on REDCap and the interviewers on Google Calendar
    ...

    Methods
    -------
    start()
        Finds and schedule compatible sessions on REDCap and Google Calendar
    Parameters
    ----------
    GoogleCalendarClient : GoogleCalendarClient
        Client with methods to interact with the Google Calendar API
    RedCapClient : RedCapClient
        Client with methods to interact with teh REDCap API

    """

    def __init__(self, calendar_id, api_url, api_key):
        """
        Constructs the REDCap and Google Calendar Client Classes

        @param calendar_id: str
                Identification code for specific calendar that has interviewer availability
        @param api_url: str
                url for REDCap API that is required to access that API
        @param api_key: str
                key for REDCAP API that is required to access that API

        """

        RedCapClient.__init__(self, api_url, api_key)
        GoogleCalendarClient.__init__(self, calendar_id)

    def start(self):
        """
        Finds and schedule compatible sessions on REDCap and Google Calendar
        """
        # User determines how many weeks ahead they would like to find compatible schedules for the specific participant
        number_of_weeks = int(input("Which week would you like to see schedules for.\n0: this weeek\n1: next week\n2: "
                                    "2 weeks from now\netc.\n"))

        # Determine all available 1-hour sessions for patient in the REDCap project
        participant_availability = getAvailableParticipantSessions(number_of_weeks)

        # get compatible interview sessions based on participant_availability
        interview_sessions = getAvailableInterviewSessions(self, participant_availability)

        # schedule google calendar event for all

        # for session in interview_sessions:
        #     # print(
        #     #     "Event Start: {session.event.start}\tEvent End: {session.event.end}\nParticipant: {session.participant}\n")
        #     self.scheduleEvent(session.event, session.participant, session.interviewer_name, session.interviewer_email,
        #                        session.participant_start, session.participant_end)

        # uploadToREDCap(self)
