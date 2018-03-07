from math import sqrt, exp, cos, sin

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        det = (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / det,
            (self.imaginary * other.real - self.real * other.imaginary) / det
        )

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, - self.imaginary)

    def exp(self):
        
        c = round(cos(self.imaginary), 15)
        s = round(sin(self.imaginary), 15)
        expa = exp(self.real)

        return ComplexNumber(expa * c, expa * s)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        return "{} + j{}".format(self.real, self.imaginary)
