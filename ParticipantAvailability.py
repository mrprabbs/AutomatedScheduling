class ParticipantAvailability:
    """
     Class representing an avaialbe session for the participant
    """
    def __init__(self, webscreen_id, timezone, start, end):
        """
        Constructs object to represent 1 hour long available session for participant
        @param webscreen_id: int
            id to represent participant, same id as in REDCap
        @param timezone: pytz.Timezone
            timezone in which participant is located
        @param start: Datetime
            start of session for which participant is available
        @param end: Datetime
            end of session for which participant is available
        """
        self.webscreen_id = webscreen_id
        self.timezone = timezone
        self.start = start
        self.end = end

    def getWebscreenId(self):
        return self.webscreen_id

    def getTimezone(self):
        return self.timezone

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def setTimezone(self, timezone):
        self.timezone = timezone

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def __str__(self):
        return f"WebscreenID: {self.webscreen_id}\nTimezone: {self.timezone}\nStart: {self.start}\nEnd: {self.end}"
