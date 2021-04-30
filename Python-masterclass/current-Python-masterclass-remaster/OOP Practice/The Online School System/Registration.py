class Registration:

    def __init__(self, course, instructorObj=None):
        self.course = course
        self.instructor = instructorObj
        self.grade_list = ['F', 'Failing']
        self.mark = 0
        self.grade_letter = 0

    @classmethod
    def constructor2(cls, course, instructorObj):
        return cls(course=course, instructorObj=instructorObj)

    def getTitle(self):
        return self.course

    def getMarks(self):
        return self.mark

    def get_grade_list(self):
        return self.grade_list

    def getInstructor(self):
        return self.instructor

    def getGradeReport(self):
        if 90 <= self.mark <= 100:
            self.grade_list[0] = 'A+'
            self.grade_list[1] = 'Exceptional'
            self.grade_letter = 9
        elif 80 <= self.mark <= 90:
            self.grade_list[0] = 'A'
            self.grade_list[1] = 'Excellent'
            self.grade_letter = 8
        elif 70 <= self.mark <= 80:
            self.grade_list[0] = 'B'
            self.grade_list[1] = 'Good'
            self.grade_letter = 7
        elif 60 <= self.mark <= 70:
            self.grade_list[0] = 'C'
            self.grade_list[1] = 'Competent'
            self.grade_letter = 6
        elif 50 <= self.mark <= 60:
            self.grade_list[0] = 'D'
            self.grade_list[1] = 'Passing'
            self.grade_letter = 5
        else:
            self.grade_list[0] = 'F'
            self.grade_list[1] = 'Failing'
            self.grade_letter = 0

        return self.grade_list

    def getInformation(self):
        if self.instructor is None:
            result = f"{self.course} has not yet been assigned an instructor"
        else:
            result = f"{self.course}, taught by {self.instructor.getName()}, is completed with raw marks {self.mark}" \
                     f" ({self.grade_list[0]} ) {self.grade_list[1]})"
        return result

    def setInstructor(self, instructor):
        self.instructor = instructor

    def setMarks(self, newMark):
        self.mark = newMark

    def setGradeLetter(self, newLetter):
        self.grade_letter = newLetter
