from func import list_sum, division
import unittest


class TestFunc(unittest.TestCase):

    def setUp(self) -> None:
        print("Hi")

    def tearDown(self) -> None:
        print("Bye\n")

    def test_case_1(self):
        print("T1")
        input_list = list_sum([1, 2, 3])
        expected = [1, 3, 6]
        self.assertEqual(input_list, expected)

    def test_case_2(self):
        print("T2")
        self.assertEqual(5, 5)

    def test_case_3(self):
        print("T3")
        input_list = list_sum([1, 2])
        expected = [1, 3]
        self.assertEqual(input_list, expected)

    def test_case_4(self):
        print("T4")
        self.assertRaises(AssertionError, division, 1, 0)

    def test_case_5(self):
        print("T5")
        with self.assertRaises(AssertionError):
            division(1, 0)


if __name__ == '__main__':
    unittest.main()

