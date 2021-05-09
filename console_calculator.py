import os
from calculator_logic.calculator import Calculator
from copy import deepcopy


class ConsoleCalculator:
    def __init__(self, calculator, type=float):
        self.__calculator = calculator
        self.__type = type

    def set_type(self, type):
        self.__type = type

    def show_calculator(self):
        print(self.__calculator.memory_number)
        operation = input()
        if operation == "exit":
            exit()
        try:
            number = self.__type(input())
            self.__calculator.memory_number = self.__calculator.calculate(self.__calculator.memory_number,
                                                                          number, operation)
            os.system("cls")
        except Exception as e:
            os.system("cls")
            print(str(e))
        finally:
            self.show_calculator()

    def clone(self):
        return deepcopy(self)
