import os
from calculator_logic.calculator import Calculator


class DigitConsoleCalculator:
    def __init__(self, calculator):
        self.__calculator = calculator

    def show_calculator(self):
        print(self.__calculator.memory_number)
        operation = input()
        if operation == "exit":
            exit()
        try:
            number = float(input())
            self.__calculator.memory_number = self.__calculator.calculate(self.__calculator.memory_number,
                                                                          number, operation)
            os.system("cls")
        except Exception as e:
            os.system("cls")
            print(str(e))
        finally:
            self.show_calculator()
