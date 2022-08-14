from asyncio import run

import GoogleCalendarClient
import RedCapClient
from SchedulerBot import SchedulerBot
from config import calendarID
from config import api_url, api_key

if __name__ == '__main__':
    # Initialize the Scheduler Bot Object with api credentials
    scheduler = SchedulerBot(calendarID, api_url, api_key)
    SchedulerBot.start(scheduler)
