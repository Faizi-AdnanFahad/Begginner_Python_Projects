import unittest
from member import Member


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        member1 = Member()
        member2 = Member()
        self.assertTrue(member1 != member2)

    def test_case2(self):
        suyeon = Member.constructor2(12345, 's', 100)
        yuna = Member.constructor2(12346, 'b', 200)
        jihye = Member('jihye', 12348, 'g', 300)
        self.assertFalse(suyeon == yuna)
        self.assertFalse(suyeon == jihye)
        self.assertFalse(yuna == jihye)

    def test_case3(self):
        self.alan = Member.constructor3(85, 175)
        self.mark = Member.constructor3(101, 181)

        self.assertEqual(85, self.alan.getWeight(), 0.1)
        self.assertEqual(101, self.mark.getWeight(), 0.1)
        self.assertEqual(175, self.alan.getHeight(), 0.1)
        self.assertEqual(181, self.mark.getHeight(), 0.1)

        self.assertEqual("Overweight (27.8)", self.alan.getBMIReport())
        self.assertEqual("Obese (30.8)", self.mark.getBMIReport())
        self.alan.set_weight(-13)
        self.mark.set_weight(-13)
        self.assertEqual("Normal (23.5)", self.alan.getBMIReport())
        self.assertEqual("Overweight (26.9)", self.mark.getBMIReport())

    # def setUp(self) -> None:
    #     self.alan = Member.constructor3(85, 175)
    #     self.mark = Member.constructor3(101, 181)

    def test_case4(self):
        self.alan = Member.constructor3(85, 175)
        self.mark = Member.constructor3(101, 181)
        self.assertEqual(85, self.alan.getWeight(), 0.1)
        self.assertEqual(101, self.mark.getWeight(), 0.1)
        self.assertEqual(175, self.alan.getHeight(), 0.1)
        self.assertEqual(181, self.mark.getHeight(), 0.1)

        self.assertEqual("Overweight (27.8)", self.alan.getBMIReport())
        self.assertEqual("Obese (30.8)", self.mark.getBMIReport())
        self.alan.set_weight(-13)
        self.mark.set_weight(-13)
        self.assertEqual("Normal (23.5)", self.alan.getBMIReport())
        self.assertEqual("Overweight (26.9)", self.mark.getBMIReport())

    def test_case5(self):
        self.alan = Member.constructor3(85, 175)
        self.mark = Member.constructor3(101, 181)

        self.assertEqual(85, self.alan.getWeight(), 0.1)
        self.assertEqual(101, self.mark.getWeight(), 0.1)
        self.assertEqual(175, self.alan.getHeight(), 0.1)
        self.assertEqual(181, self.mark.getHeight(), 0.1)

        self.alan.set_weight(5)
        self.mark.set_weight(-3)
        self.assertEqual(90, self.alan.getWeight(), 0.1)
        self.assertEqual(98, self.mark.getWeight(), 0.1)

        self.assertEqual("Overweight (29.4)", self.alan.getBMIReport())
        self.assertEqual("Obese (29.9)", self.mark.getBMIReport())


if __name__ == '__main__':
    unittest.main()




























