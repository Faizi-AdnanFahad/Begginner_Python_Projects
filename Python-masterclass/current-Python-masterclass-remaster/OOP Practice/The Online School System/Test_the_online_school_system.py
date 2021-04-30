import unittest
from Instructor import Instructor
from Registration import Registration
from Participant import Participant
from OnlineSchool import OnlineSchool


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        i = Instructor("Jackie", 70130, "jackie@eecs.yorku.ca")
        name = i.getName()
        ext = i.getPhoneExtension()
        contact = i.getEmail()
        info = i.getInformation()

        self.assertEqual("Jackie", name)
        self.assertEqual(70130, ext)
        self.assertEqual("jackie@eecs.yorku.ca", contact)
        self.assertEqual("Jackie has campus phone extension 70130 and contact email jackie@eecs.yorku.ca", info)

        i.setName("Jonathan")
        i.setPhoneExtension(70139)
        i.setEmail("jonathan@yorku.ca")

        self.assertEqual("Jonathan", i.getName())
        self.assertEqual(70139, i.getPhoneExtension())
        self.assertEqual("jonathan@yorku.ca", i.getEmail())
        self.assertEqual("Jonathan has campus phone extension 70139 and contact email jonathan@yorku.ca",
                         i.getInformation())

    def test_case_2(self):
        r = Registration("Software Design")
        t = r.getTitle()
        m = r.getMarks()
        i = r.getInstructor()
        gr = r.getGradeReport()
        info = r.getInformation()

        self.assertEqual("Software Design", t)
        self.assertEqual(0, m)
        self.assertTrue(i is None)
        self.assertTrue(gr.length == 2 and gr[0].equals("F") and gr[1].equals("Failing"))
        self.assertEqual("Software Design has not yet been assigned an instructor", info)

        jackie = Instructor("Jackie", 70130, "jackie@eecs.yorku.ca")
        r.setInstructor(jackie)

        self.assertEqual("Software Design", r.getTitle())
        self.assertEqual(0, r.getMarks())
        self.assertTrue(r.getInstructor() is not None
                        and r.getInstructor() == jackie  # reference aliasing #
                        # Q. Can you visualize this chain of method calls? #
                        and r.getInstructor().getName().equals("Jackie")
                        and r.getInstructor().getPhoneExtension() == 70130
                        and r.getInstructor().getEmail().equals("jackie@eecs.yorku.ca"))
        self.assertTrue(r.getGradeReport().length == 2)
        self.assertEqual(r.getGradeReport()[0], "F")
        self.assertEqual(r.getGradeReport()[1], "Failing")
        self.assertEqual("Software Design, taught by Jackie, is completed with raw marks 0 (F ) Failing)",
                         r.getInformation())

        r.setMarks(61)

        self.assertEqual(61, r.getMarks())
        self.assertTrue(r.getGradeReport().length == 2
                        and r.getGradeReport()[0].equals("C")
                        and r.getGradeReport()[1].equals("Competent"))
        self.assertEqual("Software Design, taught by Jackie, is completed with raw marks 61 (C ) Competent)",
                         r.getInformation())

        jim = Instructor("Jim Davies", 70139, "jim@yorku.ca")
        r.setInstructor(jim)

        self.assertTrue(r.getInstructor() is not None
                        and r.getInstructor() != jackie
                        and r.getInstructor() == jim)
        self.assertEqual("Software Design, taught by Jim Davies, is completed with raw marks 61 (C ) Competent)",
                         r.getInformation())

    def test_case_3(self):
        r = Registration("Data Structures", Instructor("J. Gibbons", 76283, "jeremy@yorku.ca"))
        r.setMarks(73)

        self.assertEqual("Data Structures", r.getTitle())
        self.assertEqual(73, r.getMarks())
        self.assertTrue(r.getInstructor().getName().equals("J. Gibbons")
                        and r.getInstructor().getPhoneExtension() == 76283
                        and r.getInstructor().getEmail().equals("jeremy@yorku.ca")
                        and r.getInstructor().getInformation().equals(
            "J. Gibbons has campus phone extension 76283 and contact email jeremy@yorku.ca"))
        self.assertTrue(r.getGradeReport().length == 2
                        and r.getGradeReport()[0].equals("B")
                        and r.getGradeReport()[1].equals("Good"))
        self.assertEqual("Data Structures, taught by J. Gibbons, is completed with raw marks 73 (B ) Good)",
                         r.getInformation())

    def test_case_4(self):
        alan = Instructor("A. Wassyng", 70130, "jackie@eecs.yorku.ca")
        mark = Instructor("M. Lawford", 70139, "jonathan@yorku.ca")

        suyeon = Participant("S. Y. Lee")
        suyeonRegistrations = suyeon.getRegistrations()
        report = suyeon.getGPAReport()

        # empty list of registrations to begin with #
        self.assertTrue(suyeonRegistrations.length == 0)
        # GPA undefined over an empty list of registrations #
        self.assertEqual("No GPA available yet for S. Y. Lee", report)
        # non-registered courses have default marks -1 #
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == -1)
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == -1)
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)

        r1 = Registration("Intro. to OOP", alan)
        # add two registrations for suyeon
        # Hints:
        # 	- Are the two `addRegistration` calls denote the same method?
        #	- Or an overloaded method (i.e., methods with the same name but distinct input parameter types)?
        #
        suyeon.addRegistration(r1)
        suyeon.addRegistration("Heavy Metal Music")
        ############/ make a test and check what happens if you don't call getRegistration
        self.assertTrue(suyeon.getRegistrations().length == 2
                        and suyeon.getRegistrations()[0] == r1
                        and suyeon.getRegistrations()[1].getTitle().equals("Heavy Metal Music")
                        and suyeon.getRegistrations()[1].getInstructor() == None)
        self.assertTrue(suyeon.getRegistrations()[0].getMarks() == 0)
        self.assertTrue(suyeon.getRegistrations()[1].getMarks() == 0)
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == 0)  # now a registered course #
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == 0)  # now a registered course #
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)  # still a non-registered course #

        suyeon.getRegistrations()[1].setInstructor(mark)

        self.assertTrue(suyeon.getRegistrations()[1].getInstructor() == mark)

        #
        # Notice the format of GPA report:
        #  - GPA value is displayed with 1 digit after the decimal point.
        # 	- The comma-separated list of `GradePo(LetterGrade)` is surrounded by curly braces.
        # 	- There is a space after each comma and after the colon.
        #
        self.assertEqual("S. Y. Lee's GPA of {0 (F), 0 (F)}: 0.0", suyeon.getGPAReport())

        suyeon.updateMarks("Intro. to OOP", 61)
        suyeon.updateMarks("Heavy Metal Music", 79)
        # non-existing course -> do nothing #
        suyeon.updateMarks("Psychology I", 89)
        self.assertTrue(suyeon.getRegistrations()[0].getMarks() == 61)  # Grade: C) GP: 6  #
        self.assertTrue(suyeon.getRegistrations()[1].getMarks() == 79)  # Grade: B) GP: 7 #
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == 61)
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == 79)
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)
        # GPA = sum of GPs divided by number of courses #
        self.assertEqual("S. Y. Lee's GPA of {6 (C), 7 (B)}: 6.5", suyeon.getGPAReport())

        yuna = Participant("Y. Lee")
        yuna.addRegistration(Registration("Heavy Metal Music", mark))
        yuna.addRegistration(Registration("Intro. to OOP", alan))
        # Q. Can you understand the two occurrences of anonymous objects below? #
        yuna.addRegistration(Registration(
            "Psychology I",
            Instructor("Tom", 70141, "tom@yorku.ca")))
        yuna.updateMarks("Heavy Metal Music", 85)
        yuna.updateMarks("Intro. to OOP", 58)
        yuna.updateMarks("Psychology I", 66)

        self.assertTrue(yuna.getRegistrations()[0].getMarks() == 85)  # Grade: A) GP: 8  #
        self.assertTrue(yuna.getRegistrations()[1].getMarks() == 58)  # Grade: D) GP: 5 #
        self.assertTrue(yuna.getRegistrations()[2].getMarks() == 66)  # Grade: C) GP: 6 #
        self.assertTrue(yuna.marksOf("Heavy Metal Music") == 85)
        self.assertTrue(yuna.marksOf("Intro. to OOP") == 58)
        self.assertTrue(yuna.marksOf("Psychology I") == 66)
        self.assertEqual("Y. Lee's GPA of {8 (A), 5 (D), 6 (C)}: 6.3", yuna.getGPAReport())

        self.assertEqual(suyeon.getRegistrations()[0].getTitle(), yuna.getRegistrations()[1].getTitle())
        self.assertTrue(suyeon.getRegistrations()[0] != yuna.getRegistrations()[1])
        self.assertEqual(suyeon.getRegistrations()[1].getTitle(), yuna.getRegistrations()[0].getTitle())
        self.assertTrue(suyeon.getRegistrations()[1] != yuna.getRegistrations()[0])

        suyeon.clearRegistrations()
        yuna.clearRegistrations()

        self.assertTrue(suyeon.getRegistrations().length == 0
                        and yuna.getRegistrations().length == 0)
        self.assertTrue(suyeon.getGPAReport().equals("No GPA available yet for S. Y. Lee")
                        and yuna.getGPAReport().equals("No GPA available yet for Y. Lee"))
        courses = ["Intro. to OOP", "Heavy Metal Music", "Psychology I", "Software Design"]

        for i in range(len(courses)):
            self.assertTrue(suyeon.marksOf(courses[i])) == -1
            self.assertTrue(yuna.marksOf(courses[i])) == -1

        # Next semester, students may choose to re-take some courses. #
        suyeon.addRegistration("Heavy Metal Music")
        suyeon.updateMarks("Heavy Metal Music", 99)

        self.assertTrue(suyeon.getRegistrations().length == 1)
        self.assertEqual("S. Y. Lee's GPA of {9 (A+)}: 9.0", suyeon.getGPAReport())
        self.assertEqual("Heavy Metal Music has not yet been assigned an instructor",
                         suyeon.getRegistrations()[0].getInformation())

    def test_case_5(self):
        heeyeon = Participant("H. Y. Kang")
        r1 = Registration("EECS2001")
        r2 = Registration("EECS2011")
        r3 = Registration("EECS2021")
        r4 = Registration("EECS2031")
        r5 = Registration("EECS1090")
        lost_of_r = [r1, r2, r3, r4, r5]

        # Q. Without the loop below,
        # how many lines of assertions need to be written explicitly?
        #
        for i in range(len(lost_of_r)):
            heeyeon.addRegistration(lost_of_r[i])
        self.assertTrue(heeyeon.getRegistrations().length == i + 1)
        self.assertTrue(heeyeon.getRegistrations()[i] == lost_of_r[i])

        # Maximum number of registrations allowed is 5.
        # Adding beyond the maximum capacity will have no effect.
        #
        heeyeon.addRegistration(Registration("ECON1000"))
        heeyeon.addRegistration(Registration("ECON1010"))

        self.assertTrue(heeyeon.getRegistrations().length == 5)
        self.assertTrue(heeyeon.getRegistrations()[0] == r1)
        self.assertTrue(heeyeon.getRegistrations()[1] == r2)
        self.assertTrue(heeyeon.getRegistrations()[2] == r3)
        self.assertTrue(heeyeon.getRegistrations()[3] == r4)
        self.assertTrue(heeyeon.getRegistrations()[4] == r5)

    def test_case_6(self):
        school = OnlineSchool()
        # courses not existing (yet) #
        list1 = school.getParticipants("Intro. to OOP")
        list2 = school.getParticipants("Heavy Metal Music")
        list3 = school.getParticipants("Chamber Music")

        self.assertTrue(list1.length == 0 and list2.length == 0 and list3.length == 0)

        alan = Participant("A. Wassyng")
        mark = Participant("M. Lawford")
        tom = Participant("T. Maibaum")
        school.addParticipant(alan)
        school.addParticipant(mark)
        school.addParticipant(tom)
        tom.addRegistration("Heavy Metal Music")
        tom.addRegistration("Chamber Music")
        tom.addRegistration("Intro. to OOP")
        alan.addRegistration("Intro. to OOP")
        mark.addRegistration("Heavy Metal Music")
        mark.addRegistration("Intro. to OOP")

        #
        #
        # Order in which participants appear in the returned array of `getParticipants` should be
        # the same as how they appear in the school's list of participants (e.g., alan, mark, tom).
        #
        #

        list1 = school.getParticipants("Intro. to OOP")
        list2 = school.getParticipants("Heavy Metal Music")
        list3 = school.getParticipants("Chamber Music")

        self.assertTrue(list1.length == 3
                        and list1[0] == alan
                        and list1[1] == mark
                        and list1[2] == tom)
        self.assertTrue(list2.length == 2
                        and list2[0] == mark
                        and list2[1] == tom)
        self.assertTrue(list3.length == 1
                        and list3[0] == tom)

        # non-existing course #
        self.assertTrue(school.getParticipants("How to Make Fish and Chips").length == 0)

    def test_case_7(self):
        alan = Instructor("A. Wassyng", 70130, "jackie@eecs.yorku.ca")
        mark = Instructor("M. Lawford", 70139, "jonathan@yorku.ca")

        suyeon = Participant("S. Y. Lee")
        #
        # Length of the returned array from `getRegistrations` corresponds to
        # the number of registrations added by the so far.
        # See the instructions PDF regarding the max number of registrations that can be added.
        #
        suyeonRegistrations = suyeon.getRegistrations()
        report = suyeon.getGPAReport()

        # empty list of registrations to begin with #
        self.assertTrue(suyeonRegistrations.length == 0)
        # GPA undefined over an empty list of registrations #
        self.assertEqual("No GPA available yet for S. Y. Lee", report)
        # non-registered courses have default marks -1 #
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == -1)
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == -1)
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)

        r1 = Registration("Intro. to OOP", alan)
        # add two registrations for suyeon
        # Hints:
        # 	- Are the two `addRegistration` calls denote the same method?
        #	- Or an overloaded method (i.e., methods with the same name but distinct input parameter types)?
        #
        suyeon.addRegistration(r1)
        suyeon.addRegistration("Heavy Metal Music")
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == 0)  # now a registered course #
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == 0)  # now a registered course #
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)  # still a non-registered course #

        suyeon.getRegistrations()[1].setInstructor(mark)

        self.assertTrue(suyeon.getRegistrations()[1].getInstructor() == mark)

        #
        # Notice the format of GPA report:
        #  - GPA value is displayed with 1 digit after the decimal point.
        # 	- The comma-separated list of `GradePo(LetterGrade)` is surrounded by curly braces.
        # 	- There is a space after each comma and after the colon.
        #
        self.assertEqual("S. Y. Lee's GPA of {0 (F), 0 (F)}: 0.0", suyeon.getGPAReport())

        suyeon.updateMarks("Intro. to OOP", 61)
        suyeon.updateMarks("Heavy Metal Music", 79)
        # non-existing course -> do nothing #
        suyeon.updateMarks("Psychology I", 89)
        self.assertTrue(suyeon.getRegistrations()[0].getMarks() == 61)  # Grade: C) GP: 6  #
        self.assertTrue(suyeon.getRegistrations()[1].getMarks() == 79)  # Grade: B) GP: 7 #
        self.assertTrue(suyeon.marksOf("Intro. to OOP") == 61)
        self.assertTrue(suyeon.marksOf("Heavy Metal Music") == 79)
        self.assertTrue(suyeon.marksOf("Psychology I") == -1)
        # GPA = sum of GPs divided by number of courses #
        self.assertEqual("S. Y. Lee's GPA of {6 (C), 7 (B)}: 6.5", suyeon.getGPAReport())

        yuna = Participant("Y. Lee")
        yuna.addRegistration(Registration("Heavy Metal Music", mark))
        yuna.addRegistration(Registration("Intro. to OOP", alan))
        # Q. Can you understand the two occurrences of anonymous objects below? #
        yuna.addRegistration(Registration(
            "Psychology I",
            Instructor("Tom", 70141, "tom@yorku.ca")))
        yuna.updateMarks("Heavy Metal Music", 85)
        yuna.updateMarks("Intro. to OOP", 58)
        yuna.updateMarks("Psychology I", 66)

        self.assertTrue(yuna.getRegistrations()[0].getMarks() == 85)  # Grade: A) GP: 8  #
        self.assertTrue(yuna.getRegistrations()[1].getMarks() == 58)  # Grade: D) GP: 5 #
        self.assertTrue(yuna.getRegistrations()[2].getMarks() == 66)  # Grade: C) GP: 6 #
        self.assertTrue(yuna.marksOf("Heavy Metal Music") == 85)
        self.assertTrue(yuna.marksOf("Intro. to OOP") == 58)
        self.assertTrue(yuna.marksOf("Psychology I") == 66)
        self.assertEqual("Y. Lee's GPA of {8 (A), 5 (D), 6 (C)}: 6.3", yuna.getGPAReport())

        # Suyeon and Yuna are classmates of two courses,
        # but the objects are distinct.
        #
        self.assertEqual(suyeon.getRegistrations()[0].getTitle(), yuna.getRegistrations()[1].getTitle())
        self.assertTrue(suyeon.getRegistrations()[0] != yuna.getRegistrations()[1])
        self.assertEqual(suyeon.getRegistrations()[1].getTitle(), yuna.getRegistrations()[0].getTitle())
        self.assertTrue(suyeon.getRegistrations()[1] != yuna.getRegistrations()[0])

        # At the end of the semester, clear registrations of students. #
        suyeon.clearRegistrations()
        yuna.clearRegistrations()

        self.assertTrue(suyeon.getRegistrations().length == 0
                        and yuna.getRegistrations().length == 0)
        self.assertTrue(suyeon.getGPAReport().equals("No GPA available yet for S. Y. Lee")
                        and yuna.getGPAReport().equals("No GPA available yet for Y. Lee"))
        courses = ["Intro. to OOP", "Heavy Metal Music", "Psychology I", "Software Design"]
        # Q. Without the loop below,
        # how many lines of assertions need to be written explicitly?
        #
        for i in range(len(courses)):
            self.assertTrue(suyeon.marksOf(courses[i]) == -1)
            self.assertTrue(yuna.marksOf(courses[i]) == -1)

        # Next semester, students may choose to re-take some courses. #
        suyeon.addRegistration("Heavy Metal Music")
        suyeon.updateMarks("Heavy Metal Music", 99)

        self.assertTrue(suyeon.getRegistrations().length == 1)
        self.assertEqual("S. Y. Lee's GPA of {9 (A+)}: 9.0", suyeon.getGPAReport())
        self.assertEqual("Heavy Metal Music has not yet been assigned an instructor",
                         suyeon.getRegistrations()[0].getInformation())


if __name__ == '__main__':
    unittest.main()
