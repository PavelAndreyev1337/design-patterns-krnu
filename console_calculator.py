import os
from calculator_logic.calculator import Calculator


class ConsoleCalculator:
    def __init__(self):
        self.__calculator = Calculator()

    @staticmethod
    def check_float(potential_number):
        try:
            float(potential_number)
            return True
        except ValueError:
            return False

    def show_calculator(self):
        print(self.__calculator.memory_number)
        operation = input()
        if operation == "exit":
            exit()
        try:
            input_value = input()
            if self.check_float(input_value):
                number = float(input_value)
            else:
                number = complex(input_value)
            self.__calculator.memory_number = self.__calculator.calculate(self.__calculator.memory_number,
                                                                          number, operation)
            os.system("cls")
        except Exception as e:
            os.system("cls")
            print(str(e))
        finally:
            self.show_calculator()
