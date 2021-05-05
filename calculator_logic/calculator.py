from .calculator_interface import CalculatorInterface


class Calculator(CalculatorInterface):
    """ Realization for calculator interface. """
    def __init__(self):
        self.__memory_number = 0

    @property
    def memory_number(self):
        return self.__memory_number

    @memory_number.setter
    def memory_number(self, memory_number):
        self.__memory_number = memory_number

    def sum(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        if second == 0:
            raise ZeroDivisionError()
        return first / second

    def calculate(self, first, second, operation):
        if operation == "+":
            return self.sum(first, second)
        elif operation == "-":
            return self.subtract(first, second)
        elif operation == "*":
            return self.multiply(first, second)
        elif operation == "/":
            return self.divide(first, second)
        else:
            raise Exception("No such operation!")
