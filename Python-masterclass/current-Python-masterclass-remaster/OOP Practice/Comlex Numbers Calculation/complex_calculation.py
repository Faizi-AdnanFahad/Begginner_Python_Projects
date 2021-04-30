
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
                if self.ima == -1:
                    self.display = f'-i'
        elif self.ima == 0:
            if self.real > 0:
                self.display = f'{self.real}'
            elif self.ima < 0:
                self.display = f'-{abs(self.real)}'

        return self.display


class AddSub(ComplexNumber):

    def __init__(self, firstC, secondC):
        real = firstC.get_real() + secondC.get_real()
        img = firstC.get_imaginary() + secondC.get_imaginary()
        super().__init__(real=real, ima=img)

    def get_real(self):
        return super().get_real()

    def get_imaginary(self):
        return super().get_imaginary()

    def get_represention(self):
        return super().complex_representation()



class Multiplication:

    def __init__(self):
        pass


class Division:

    def __init__(self):
        pass

