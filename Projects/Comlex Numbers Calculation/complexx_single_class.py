
class ComplexNumber:

    def __init__(self, real, ima):
        self.real = real
        self.ima = ima
        self.display = ''

    def get_real(self):
        return self.real

    def get_imaginary(self):
        return self.ima

    def complex_representation(self):
        if self.real != 0 and self.ima != 0:
            if self.real > 0 and self.ima > 0:
                self.display = f'{self.real} + {self.ima}i'
            elif self.real > 0 and self.ima < 0:
                self.display = f'{self.real} - {abs(self.ima)}i'
            elif self.real < 0 and self.ima > 0:
                self.display = f'-{abs(self.real)} + {self.ima}i'
            if self.real < 0 and self.ima < 0:
                self.display = f'-{abs(self.real)} - {abs(self.ima)}i'
        elif self.real == 0 and self.ima == 0:
            self.display = '0'
        elif self.real == 0:
            if self.ima > 0:
                self.display = f'{self.ima}i'
            elif self.ima < 0:
                self.display = f'-{abs(self.ima)}i'
        elif self.ima == 0:
            if self.real > 0:
                self.display = f'{self.real}'
            elif self.ima < 0:
                self.display = f'-{abs(self.real)}'

        return self.display


class AddSub(ComplexNumber):

    def __init__(self, firstC, secondC):
        self.real = firstC.get_real() + secondC.get_real()
        self.img = firstC.get_imaginary() + secondC.get_imaginary()
        super().__init__(real=self.real, ima=self.img)

    def get_real(self):
        return super().get_real()

    def get_imaginary(self):
        return super().get_imaginary()

    def get_representation(self):
        return super().complex_representation()


class Conjugate(ComplexNumber):

    def __init__(self, a, b):  # a + bi
        negative_b = b * (-1)
        super().__init__(real=a, ima=negative_b)

    def get_real(self):
        return super().get_real()

    def get_imaginary(self):
        return super().get_imaginary()

    def get_representation(self):
        return super().complex_representation()


class Multiplication:

    def __init__(self, complex1, complex2):
        self.a = complex1.get_real()
        self.b = complex1.get_imaginary()
        self.c = complex2.get_real()
        self.d = complex2.get_imaginary()

    def multiply(self):
        real = ((self.a * self.c) - (self.b * self.d))
        ima = ((self.a * self.d) + (self.b * self.c))
        self.com = ComplexNumber(real=real, ima=ima)

    def get_real(self):
        return self.com.get_real()

    def get_imaginary(self):
        return self.com.get_imaginary()

    def get_representation(self):
        return self.com.complex_representation()


class Division:

    def __init__(self, c1, c2):
        self.a = c1.get_real()
        self.b = c1.get_imaginary()
        # if c2.get_real() != 0 and c2.get_imaginary != 0:
        self.c = c2.get_real()
        self.d = -(c2.get_imaginary())
        # else:
        #     raise AssertionError("You can't divide by zero")

    def divide(self):
        try:
            real = round(((self.a * self.c) - (self.b * self.d)) / ((self.c ** 2) + (self.d ** 2)), 2)
            ima = round(((self.a * self.d) + (self.b * self.c)) / ((self.c ** 2) + (self.d ** 2)), 2)
            self.div = ComplexNumber(real=real, ima=ima)
        except ZeroDivisionError:
            print("You can't divide by zero")

    def get_real(self):
        return self.div.get_real()

    def get_imaginary(self):
        return self.div.get_imaginary()

    def get_representation(self):
        return self.div.complex_representation()
