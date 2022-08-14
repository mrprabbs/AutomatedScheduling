from __future__ import print_function

from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
import pytz

utc = pytz.UTC
cst = pytz.timezone('US/Central')

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events']


def setup_client(calendar_id):
    """
    Static method to initialize Calendar with the calendar id utilising the gcsa python wrapper

    Parameters
    ---------
    calendar_id: str
            Identification code for specific calendar that has interviewer availability
    """
    #     """Shows basic usage of the Google Calendar API.
    #     Prints the start and name of the next 10 events on the user's calendar.
    #     """
    #     # The file token.json stores the user's access and refresh tokens, and is
    #     # created automatically when the authorization flow completes for the first
    #     # time.
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #     return GoogleCalendar(calendar=calendar_id, credentials=creds)
    #
    # #     # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'client_secret.json', SCOPES, redirect_uri='localhost/users/auth/google_oauth2/callback')
    #
    #         creds = flow.run_local_server(port=3000)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())

    gc = GoogleCalendar(calendar=calendar_id, credentials_path="credentials.json")
    return gc


class GoogleCalendarClient:
    """
    Client class to interact with Google Calendar API
    """
    def __init__(self, calendar_id):
        """
        construct Calendar Object using gcsa python wrapper

        Parameters
        ----------
            calendar_id: str
                Identification code for specific calendar that has interviewer availability
        """
        self.calendar = setup_client(calendar_id)

    def scheduleEvent(self, event, participant, interviewer_name, interviewer_email, participant_start, participant_end):
        """
        Function to schedule interview event on Google Calendar with specific details

        Parameters
        ----------
        event: Event
            Google Calendar Event that has information about the interviwer and their availability
        participant: ParticipantAvailability
            Object that has information about the participant and their availabiilty
        interviewer_name: str
            Name of available interviewer
        interviewer_email: str
            Email of available interviewer
        participant_start: Datetime
            Start time of participant availability, since it is compatible with the interviewer, this is when the
             scheduled interview will start
        participant_end: Datetime
            End time of participant availability, since it is compatible with the interviewer, this is when the
            scheduled interview will end
        """
        # print("\nSCHEDULING GOOGLE CALENDAR EVENT\n")

        print(f"\nEVENT SCHEDULED - {interviewer_name}\nStart: {participant_start}\tEnd: {participant_end}\nattendees: {interviewer_email}")
        event = Event(summary=f"SCHEDULED - {interviewer_name}", start=participant_start, end=participant_end, attendees=interviewer_email)

        # self.calendar.add_event(event)


        pass