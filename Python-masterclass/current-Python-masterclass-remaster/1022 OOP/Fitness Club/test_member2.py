import unittest
from member import Member, Facility, Trainer


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        alan = Member.constructor3(85, 175)
        mark = Member.constructor3(101, 181)

        self.assertEqual(85, alan.getWeight(), 0.1)
        self.assertEqual(101, mark.getWeight(), 0.1)
        self.assertEqual(175, alan.getHeight(), 0.1)
        self.assertEqual(181, mark.getHeight(), 0.1)

        self.assertEqual("Overweight (27.8)", alan.getBMIReport())
        self.assertEqual("Obese (30.8)", mark.getBMIReport())
        self.assertEqual("Normal (23.5)", alan.getBMIReport())
        self.assertEqual("Obese (30.8)", mark.getBMIReport())

    def test_case2(self):
        suyeon = Member.constructor2(12345, 's', 100)
        yuna = Member.constructor2(12346, 'b', 200)
        jihye = Member('jihye', 12348, 'g', 300)
        self.assertFalse(suyeon == yuna)
        self.assertFalse(suyeon == jihye)
        self.assertFalse(yuna == jihye)

    def test_case3(self):
        alan = Member.constructor3(85, 175)
        mark = Member.constructor3(101, 181)

        self.assertEqual(85, alan.getWeight(), 0.1)
        self.assertEqual(101, mark.getWeight(), 0.1)
        self.assertEqual(175, alan.getHeight(), 0.1)
        self.assertEqual(181, mark.getHeight(), 0.1)

        self.assertEqual("Overweight (27.8)", alan.getBMIReport())
        self.assertEqual("Obese (30.8)", mark.getBMIReport())

        self.assertFalse(mark == alan)
        mark = alan
        self.assertTrue(mark == alan)

        alan.set(-13)
        self.assertEqual("Normal (23.5)", alan.getBMIReport())
        self.assertEqual("Normal (23.5)", mark.getBMIReport())


def test_case4(self):
    alan = Member()
    mark = Member()
    oldAlan = alan
    oldMark = mark

    self.assertTrue(alan == oldAlan)
    self.assertTrue(mark == oldMark)

    tom = alan
    alan = mark
    mark = tom

    self.assertTrue(alan == oldMark)
    self.assertTrue(mark == oldAlan)


def test_case5(self):
    alan = Member("Alan")
    mark = Member("Mark")
    tom = Member("Tom")
    self.assertTrue(alan.getTrainer() is None)
    self.assertTrue(mark.getTrainer() is None)
    self.assertFalse(tom.getTrainer() is not None)

    jared = Trainer("Jared")
    jon = Trainer("Jon")

    alan.registerTrainer(jared)
    mark.registerTrainer(jon)
    self.assertTrue(alan.getTrainer() != None and alan.getTrainer() == jared)
    self.assertTrue(mark.getTrainer() == jon)

    self.assertTrue(tom.getTrainer() == None)

    tom.referTrainer(mark)
    self.assertTrue(tom.getTrainer() != None and tom.getTrainer() == jon)

    tom.referTrainer(alan)
    self.assertTrue(tom.getTrainer() != None and tom.getTrainer() == jared)

    alan.swapTrainer(mark)
    self.assertTrue(alan.getTrainer() != None and alan.getTrainer() == jon)
    self.assertTrue(mark.getTrainer() != None and mark.getTrainer() == jared)

    self.assertTrue(alan.getTrainer() != None and alan.getTrainer() == jared)
    self.assertTrue(mark.getTrainer() != None and mark.getTrainer() == jon)

    gym = Facility("Gym", 1, 2)
    spa = Facility("Spa", 2, 2)
    tennis = Facility("Tennis", 3, 2)

    alan.registerFacility(gym)
    alan.registerFacility(spa)
    alan.registerFacility(tennis)

    self.assertEqual(12, alan.getPaymentDue(), 0.1)


if __name__ == '__main__':
    unittest.main()
