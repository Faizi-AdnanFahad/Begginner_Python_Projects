import unittest
from complex_calculation import ComplexNumber, AddSub, Multiplication, Division, Conjugate


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

    def test_case_4(self):
        c1 = ComplexNumber(-1, -1)
        self.assertEqual(-1, c1.get_real())
        self.assertEqual(-1, c1.get_imaginary())
        self.assertEqual('-1 - 1i', c1.complex_representation())

    def test_case_5(self):
        c1 = ComplexNumber(-2.2, 0.3)
        self.assertEqual(-2.2, c1.get_real())
        self.assertEqual(0.3, c1.get_imaginary())
        self.assertEqual('-2.2 + 0.3i', c1.complex_representation())

    def test_case_6(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 1)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 2)
        self.assertTrue(add.get_imaginary() == 3)
        self.assertTrue(add.get_representation() == '2 + 3i')

    def test_case_7(self):
        c1 = ComplexNumber(0, 0)
        c2 = ComplexNumber(0, 0)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 0)
        self.assertTrue(add.get_imaginary() == 0)
        self.assertTrue(add.get_representation() == '0')

    def test_case_8(self):
        c1 = ComplexNumber(-1, -2)
        c2 = ComplexNumber(1, 1)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 0)
        self.assertTrue(add.get_imaginary() == -1)
        self.assertTrue(add.get_representation() == '-1i')

    def test_case_9(self):
        c1 = ComplexNumber(0.2, -2.9)
        c2 = ComplexNumber(1, 1)
        add = AddSub(c1, c2)
        self.assertTrue(add.get_real() == 1.2)
        self.assertTrue(add.get_imaginary() == -1.9)
        self.assertTrue(add.get_representation() == '1.2 - 1.9i')

    def test_case_10(self):
        conj = Conjugate(2, 3)
        self.assertTrue(conj.get_real() == 2)
        self.assertTrue(conj.get_imaginary() == -3)
        self.assertTrue(conj.get_representation() == '2 - 3i')

    def test_case_11(self):
        conj = Conjugate(-2, 3)
        self.assertTrue(conj.get_real() == -2)
        self.assertTrue(conj.get_imaginary() == -3)
        self.assertTrue(conj.get_representation() == '-2 - 3i')

    def test_case_12(self):
        conj = Conjugate(2, -3)
        self.assertTrue(conj.get_real() == 2)
        self.assertTrue(conj.get_imaginary() == 3)
        self.assertTrue(conj.get_representation() == '2 + 3i')

    def test_case_13(self):
        conj = Conjugate(-2, -3)
        self.assertTrue(conj.get_real() == -2)
        self.assertTrue(conj.get_imaginary() == 3)
        self.assertTrue(conj.get_representation() == '-2 + 3i')

    def test_case_14(self):
        conj = Conjugate(0, 3)
        self.assertTrue(conj.get_real() == 0)
        self.assertTrue(conj.get_imaginary() == -3)
        self.assertTrue(conj.get_representation() == '-3i')

    def test_case_15(self):
        conj = Conjugate(0, -3)
        self.assertTrue(conj.get_real() == 0)
        self.assertTrue(conj.get_imaginary() == 3)
        self.assertTrue(conj.get_representation() == '3i')

    def test_case_16(self):
        conj = Conjugate(2, 0)
        self.assertTrue(conj.get_real() == 2)
        self.assertTrue(conj.get_imaginary() == 0)
        self.assertTrue(conj.get_representation() == '2')

    def test_case_17(self):
        conj = Conjugate(0, 0)
        self.assertTrue(conj.get_real() == 0)
        self.assertTrue(conj.get_imaginary() == 0)
        self.assertTrue(conj.get_representation() == '0')

    def test_case_18(self):
        conj = Conjugate(3, 1)
        self.assertTrue(conj.get_real() == 3)
        self.assertTrue(conj.get_imaginary() == -1)
        self.assertTrue(conj.get_representation() == '3 - 1i')

    def test_case_19(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 1)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == -1)
        self.assertTrue(m.get_imaginary() == 3)
        self.assertTrue(m.get_representation() == '-1 + 3i')

    def test_case_20(self):
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(1, 1)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == 0)
        self.assertTrue(m.get_imaginary() == 2)
        self.assertTrue(m.get_representation() == '2i')

    def test_case_21(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 1)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == -1)
        self.assertTrue(m.get_imaginary() == 3)
        self.assertTrue(m.get_representation() == '-1 + 3i')

    def test_case_22(self):
        c1 = ComplexNumber(0, 2)
        c2 = ComplexNumber(1, 1)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == -2)
        self.assertTrue(m.get_imaginary() == 2)
        self.assertTrue(m.get_representation() == '-2 + 2i')

    def test_case_23(self):
        c1 = ComplexNumber(0, 0)
        c2 = ComplexNumber(1, 1)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == 0)
        self.assertTrue(m.get_imaginary() == 0)
        self.assertTrue(m.get_representation() == '0')

    def test_case_24(self):
        c1 = ComplexNumber(0, 0)
        c2 = ComplexNumber(0, 0)
        m = Multiplication(c1, c2)
        m.multiply()
        self.assertTrue(m.get_real() == 0)
        self.assertTrue(m.get_imaginary() == 0)
        self.assertTrue(m.get_representation() == '0')

    # DIVISION
    def test_case_25(self):
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(2, 1)
        d = Division(c1, c2)
        d.divide()
        self.assertTrue(d.get_real() == 0.60, 0.1)
        self.assertTrue(d.get_imaginary() == 0.20, 0.1)
        self.assertTrue(d.get_representation() == '0.6 + 0.2i')

    def test_case_26(self):
        c1 = ComplexNumber(0.1, 1)
        c2 = ComplexNumber(2, -0.4)
        d = Division(c1, c2)
        d.divide()
        self.assertTrue(d.get_real() == -0.05, 0.1)
        self.assertTrue(d.get_imaginary() == 0.49, 0.1)
        self.assertTrue(d.get_representation() == '-0.05 + 0.49i')

    def test_case_27(self):
        c1 = ComplexNumber(2, 1)
        c2 = ComplexNumber(2, -1)
        d = Division(c1, c2)
        d.divide()
        self.assertTrue(d.get_real() == 0.60, 0.1)
        self.assertTrue(d.get_imaginary() == 0.80, 0.1)
        self.assertTrue(d.get_representation() == '0.6 + 0.8i')

    def test_case_28(self):
        c1 = ComplexNumber(0, 1)
        c2 = ComplexNumber(2, 0)
        d = Division(c1, c2)
        d.divide()
        self.assertTrue(d.get_real() == 0.00, 0.1)
        self.assertTrue(d.get_imaginary() == 0.50, 0.1)
        self.assertTrue(d.get_representation() == '0.5i')

    def test_case_29(self):
        c1 = ComplexNumber(6, 2)
        c2 = ComplexNumber(0, 0)
        d = Division(c1, c2)
        d.divide()
        self.assertRaises(ZeroDivisionError)
        self.assertRaises(ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()
