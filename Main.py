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