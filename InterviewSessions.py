class InterviewSessions:
    """
    Class representing a compatible interview sessions

    Attributes
    ----------
    event: Event
        Google Calendar Event that has information about the interviewer and their availability
    participant: ParticipantAvailability
        Object that has information about the participant and their availability
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
    def __init__(self, event, participant, interviewer_name, interviewer_email, participant_start, participant_end):
        """
        Constructs InterviewSessions Object for easy access to certain attributes

        Parameters
        ----------
        @param event: Event
            Google Calendar Event that has information about the interviewer and their availability
        @param participant: ParticipantAvailability
            Object that has information about the participant and their availability
        @param interviewer_name: str
            Name of available interviewer
        @param interviewer_email: str
            Email of available interviewer
        @param participant_start: Datetime
            Start time of participant availability, since it is compatible with the interviewer, this is when the
            scheduled interview will start
        @param participant_end: Datetime
        End time of participant availability, since it is compatible with the interviewer, this is when the
        scheduled interview will end
        """

        self.event = event
        self.participant = participant
        self.interviewer_name = interviewer_name
        self.interviewer_email = interviewer_email
        self.participant_start = participant_start
        self.participant_end = participant_end
