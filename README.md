Давайте создадим простой калькулятор комплексных чисел на языке программирования Python с использованием архитектурных паттернов и принципов SOLID. Для логирования мы будем использовать библиотеку logging. В процессе разработки, давайте создадим три основных компонента: комплексное число, калькулятор и логгер.

ComplexNumber.py - Класс для представления комплексных чисел.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"

Calculator.py - Класс для выполнения операций сложения, умножения и деления.

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


Logger.py - Класс для логирования операций калькулятора.

import logging

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ComplexCalculator")

    def log(self, message):
        self.logger.info(message)




Main.py - Основной файл для демонстрации работы калькулятора.

from ComplexNumber import ComplexNumber
from Calculator import Calculator
from Logger import Logger

# Создаем комплексные числа
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)

# Создаем калькулятор и логгер
calculator = Calculator()
logger = Logger()

# Сложение
result_add = calculator.add(num1, num2)
logger.log(f"Сложение: {num1} + {num2} = {result_add}")

# Умножение
result_multiply = calculator.multiply(num1, num2)
logger.log(f"Умножение: {num1} * {num2} = {result_multiply}")

# Деление
result_divide = calculator.divide(num1, num2)
logger.log(f"Деление: {num1} / {num2} = {result_divide}")


Для запуска приложения вам нужно установить Python (если еще не установлен) и выполнить Main.py. У вас также должны быть файлы ComplexNumber.py, Calculator.py и Logger.py в том же каталоге. Запуск производится стандартным способом для Python-скриптов:

python Main.py
