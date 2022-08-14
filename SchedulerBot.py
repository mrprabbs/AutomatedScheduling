import datetime

import pytz

from ParticipantAvailability import ParticipantAvailability
from GoogleCalendarClient import GoogleCalendarClient
from InterviewSessions import InterviewSessions
from RedCapClient import RedCapClient
from utils import weekday_converter, timezone_converter, interviewer_email_converter
from pytz import timezone

cst = pytz.timezone('US/Central')


def getAvailableParticipantSessions(data):
    """
    Function to determine all available 1-hour sessions for all patients in the REDCap project that need to have an
    interview scheduled


    Parameters
    ----------
    @param data: REDCap project report (general availability)


    @return:
        final_participant_availability: list[ParticipantAvailability]
            list of all available 1-hour sessions for each patient for the next 7 days
    """
    # print(f"data: {data}\ntype: {type(data)}")
    today = datetime.datetime.today()
    count = 0
    participant_availability = []
    session = []
    for participant in data:
        for key, val in participant.items():
            if "webscreen_id" in key:
                webscreen_id = val
            if "gen_avail_time_zone" in key:
                participant_timezone = timezone(timezone_converter[val])
        ga_values = list(participant.values())
        ga_keys = list(participant.keys())
        # for all times, check if patient is available during that time
        for i in range(5, len(ga_values) - 3):
            # if patient is available for 3 consecutive 30 minute time blocks, add session to participant availability
            count = int(ga_values[i]) + int(ga_values[i + 1]) + int(ga_values[i + 2])
            # print(count)
            if count == 3:
                session.append(ga_keys[i])
                session.append(ga_keys[i + 1])
                session.append(ga_keys[i + 2])
                participant_availability.append(session.copy())
                session.clear()
        # print(participant_availability)
        final_participant_availability = []
        for start, middle, end in participant_availability:

            # print(f"start: {start}\tend: {end}\n")
            start_day = weekday_converter[start[10:13]]
            end_day = weekday_converter[end[10:13]]
            # print(f"start_day: {start_day}\tend_day: {end_day}\n")

            if today.weekday() < start_day:
                start_day = start_day - today.weekday()
                start_day = start_day + today.day
            elif today.weekday() > start_day:
                start_day = (7 - today.weekday() + start_day)
                start_day = start_day + today.day
            else:
                start_day = today.day

            if today.weekday() < end_day:
                end_day = end_day - today.weekday()
                end_day = end_day + today.day
            elif today.weekday() > end_day:
                end_day = (7 - today.weekday() + end_day)
                end_day = end_day + today.day
            else:
                end_day = today.day

            # print(f"start_day: {start_day}\tend_day: {end_day}\n")
            start_year_month_day = str(datetime.datetime.utcnow())[0:7] + str("-" + str(start_day))
            end_year_month_day = str(datetime.datetime.utcnow())[0:7] + str("-" + str(end_day))
            # print(f"start_year_month_day: {start_year_month_day}\tend_year_month_day: {end_year_month_day}\n")

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
    print('\t\t\t\t\t~~~~Getting compatible sessions~~~~\n\n\n')
    if not self.calendar.get_events():
        print('No upcoming events found.')
        return
    interview_sessions = []
    # iterate through all sessions where patient is available
    for participant in participant_availability:
        for event in self.calendar:
            try:
                if "Participant" in event.summary:
                    event_start = event.start + datetime.timedelta(minutes=30)
                    event_end = event.end
                    # print(f"Event Summary: {event.summary}")
                    # print(
                    #     f"Participant Start: {participant.getStart()}\tParticipant End: {participant.getEnd()}\nInterviwer Start: {event_start}\tInterviwer End:{event_end}\n")
                    if participant.getStart() >= event_start and participant.getEnd() <= event_end:
                        print("~~~~~~~~~~~~~~~~~~~~INTERVIEW TIME DETAILS~~~~~~~~~~~~~~~~~~~~\n")
                        print(f"WebscreenID: {participant.webscreen_id}\t\tGoogle Calendar Event: {event}\n")

                        print(f"\n\t\t\t\t~~~~~~~~~~UTC TIMEZONE~~~~~~~~~~\n")
                        print(
                            f"Participant Start: {participant.getStart()}\tParticipant End: {participant.getEnd()}\nInterviwer Start: {event_start}\tInterviwer End:{event_end}\n")
                        print(
                            f"Interview Session Interval\nStart:  {participant.getStart()}\tEnd: {participant.getEnd()}\n")

                        print(f"\n\t\t\t\t~~~~~~~~~~CST TIMEZONE~~~~~~~~~~\n")
                        print(
                            f"Participant Start: {participant.getStart().astimezone(cst)}\tParticipant End: {participant.getEnd().astimezone(cst)}\nInterviwer Start: {event_start.astimezone(cst)}\tInterviwer End:{event_end.astimezone(cst)}\n")
                        print(
                            f"Interview Session Interval\nStart:  {participant.getStart().astimezone(cst)}\tEnd: {participant.getEnd().astimezone(cst)}\n")

                        print(f"\n\t\t\t\t~~~~~~~~~~{str(participant.getTimezone())} TIMEZONE~~~~~~~~~~\n")
                        print(
                            f"Participant Start: {participant.getStart().astimezone(participant.getTimezone())}\tParticipant End: {participant.getEnd().astimezone(participant.getTimezone())}\nInterviewer Start: {event_start.astimezone(participant.getTimezone())}\tInterviwer End:{event_end.astimezone(participant.getTimezone())}\n")
                        print(
                            f"Interview Session Interval\nStart:  {participant.getStart().astimezone(participant.getTimezone())}\tEnd: {participant.getEnd().astimezone(participant.getTimezone())}\n")
                        interviewer_name = event.summary.split()[0]
                        interviewer_email = interviewer_email_converter[interviewer_name]
                        participant_start = participant.getStart().astimezone(cst)
                        participant_end = participant.getEnd().astimezone(cst)

                        interview_session = InterviewSessions(event, participant, interviewer_name, interviewer_email,
                                                              participant_start, participant_end)
                        interview_sessions.append(interview_session)
            except TypeError as error:
                # print(error)
                break

    # print(interview_sessions)
    return interview_sessions


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
        # # get (start, end) datetime tuples

        participant_availability = getAvailableParticipantSessions(self.getGeneralAvailability())

        # # get available interview sessions based on participant_availability

        interview_sessions = getAvailableInterviewSessions(self, participant_availability)

        # schedule google calendar event for all

        for session in interview_sessions:
            # print(
            #     "Event Start: {session.event.start}\tEvent End: {session.event.end}\nParticipant: {session.participant}\n")
            self.scheduleEvent(session.event, session.participant, session.interviewer_name, session.interviewer_email,
                               session.participant_start, session.participant_end)

        # uploadToREDCap(self)
