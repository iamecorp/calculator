from ComplexNumber import ComplexNumber

class Calculator:
    @staticmethod
    def add(a, b):
        return ComplexNumber(a.real + b.real, a.imaginary + b.imaginary)

    @staticmethod
    def multiply(a, b):
        real_part = a.real * b.real - a.imaginary * b.imaginary
        imaginary_part = a.real * b.imaginary + a.imaginary * b.real
        return ComplexNumber(real_part, imaginary_part)

    @staticmethod
    def divide(a, b):
        denominator = b.real**2 + b.imaginary**2
        real_part = (a.real * b.real + a.imaginary * b.imaginary) / denominator
        imaginary_part = (a.imaginary * b.real - a.real * b.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)
