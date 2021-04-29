import unittest


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        self.assertEqual(False, False)

    def test_something2(self):
        self.assertEqual(True, False)

    def test_something3(self):
        self.assertEqual(False, False)

    def test_something4(self):
        self.assertEqual(1, 2)



if __name__ == '__main__':
    unittest.main()
