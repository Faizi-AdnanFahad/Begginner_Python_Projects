from Registration import Registration


class Participant:

    def __init__(self, studentName):
        self.studentName = studentName
        self.registrationsList = []

    def getRegistrations(self):
        return self.registrationsList

    def getGPAReport(self):
        seq = '{'
        total = 0
        for registrations in self.getRegistrations():
            total += registrations.grade_letter
            if self.getRegistrations().index(registrations) < len(self.registrationsList) - 1:
                seq += f"{registrations.grade_letter} ({registrations.get_grade_list()[0]}), "
            elif self.getRegistrations().index(registrations) == len(self.registrationsList) - 1:
                seq += f"{registrations.grade_letter} ({registrations.get_grade_list()[0]})"
        seq += "}"

        if len(self.registrationsList) == 0:
            result = f"No GPA available yet for {self.studentName}"
        else:
            result = f"{self.studentName}'s GPA of {seq}: {total / len(self.getRegistrations()):.1f}"

        return result

    def marksOf(self, course):
        result = -1
        for registrations in self.registrationsList:
            if registrations.getTitle() == course:
                result = registrations.getMarks()
        return result

    def addRegistration(self, registration):
        if len(self.registrationsList) < 5:
            if type(registration) == Registration:
                self.registrationsList.append(registration)
            elif type(registration) == str:
                r = Registration(registration)
                self.registrationsList.append(r)

    def updateMarks(self, course, newMark):
        for registrations in self.registrationsList:
            if registrations.getTitle() == course:
                registrations.setMarks(newMark)
                registrations.getGradeReport()
                break

    def clearRegistrations(self):
        self.registrationsList.clear()
