
import GoogleCalendarClient
import RedCapClient
from SchedulerBot import SchedulerBot
from config import calendarID
from config import api_url, api_key

if __name__ == '__main__':

    # Run program until user exits
    repeat_flag = True
    while repeat_flag:

        # Initialize the Scheduler Bot Object with api credentials
        scheduler = SchedulerBot(calendarID, api_url, api_key)

        # run program
        SchedulerBot.start(scheduler)

        # Prompts and logic for user input to determine exit or rerun
        usr_input = int(input("\n~~~~~Choose from the options below~~~~~\n(0) Exit\n(1) Rerun Program\n"))
        while usr_input != 0:
            if usr_input != 1:
                print(f"\nCommand Not Found, please enter a valid number. (0/1)\n")
                usr_input = int(input("\n~~~~~Choose from the options below~~~~~\n(0) Exit\n(1) Rerun Program\n"))
            elif usr_input == 1:
                break
        if usr_input == 0:
            print(f"\n~~~Peace~~~")
            repeat_flag = False





