import unittest
from complex_calculation import ComplexNumber, AddSub, Multiplication, Division


class MyTestCase(unittest.TestCase):
    
    def test_case_1(self):
        c1 = ComplexNumber(3, 4)
        self.assertEqual(3, c1.get_real())
        self.assertEqual(4, c1.get_imaginary())
        self.assertEqual('3 + 4i', c1.complex_representation())

    def test_case_2(self):
        c1 = ComplexNumber(0, 1)
        self.assertEqual(0, c1.get_real())
        self.assertEqual(1, c1.get_imaginary())
        self.assertEqual('1i', c1.complex_representation())

    def test_case_3(self):
        c1 = ComplexNumber(0, 0)
        self.assertEqual(0, c1.get_real())
        self.assertEqual(0, c1.get_imaginary())
        self.assertEqual('0', c1.complex_representation())

    def test_case_5(self):
        c1 = ComplexNumber(-1, -1)
        self.assertEqual(-1, c1.get_real())
        self.assertEqual(-1, c1.get_imaginary())
        self.assertEqual('-1 - 1i', c1.complex_representation())

    def test_case_6(self):
        c1 = ComplexNumber(-2.2, 0.3)
        self.assertEqual(-2.2, c1.get_real())
        self.assertEqual(0.3, c1.get_imaginary())
        self.assertEqual('-2.2 + 0.3i', c1.complex_representation())

    def test_case_7(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 1)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 2)
        self.assertTrue(add.get_imaginary() == 3)
        self.assertTrue(add.get_represention() == '2 + 3i')

    def test_case_8(self):
        c1 = ComplexNumber(0, 0)
        c2 = ComplexNumber(0, 0)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 0)
        self.assertTrue(add.get_imaginary() == 0)
        self.assertTrue(add.get_represention() == '0')

    def test_case_9(self):
        c1 = ComplexNumber(-1, -2)
        c2 = ComplexNumber(1, 1)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 0)
        self.assertTrue(add.get_imaginary() == -1)
        self.assertTrue(add.get_represention() == '-i')


if __name__ == '__main__':
    unittest.main()

















