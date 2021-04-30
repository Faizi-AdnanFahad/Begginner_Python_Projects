class OnlineSchool:

    def __init__(self):
        self.participant_list = []

    def getParticipants(self, course):
        result = []
        for participant in self.participant_list:
            for registrations in participant.getRegistrations():
                if registrations.getTitle() == course:
                    result.append(participant)

        return result

    def addParticipant(self, participantObj):
        if len(self.participant_list) < 100:
            self.participant_list.append(participantObj)

