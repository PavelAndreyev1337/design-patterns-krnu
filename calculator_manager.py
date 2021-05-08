import os
from calculator_type import CalculatorType
from digit_console_calculator import DigitConsoleCalculator
from complex_console_calculator import ComplexConsoleCalculator
from calculator_logic.calculator_factory import CalculatorFactory


class CalculatorManager:
    """The Singleton class."""
    __instance = None

    @staticmethod
    def get_instance():
        if CalculatorManager.__instance == None:
            CalculatorManager()
        return CalculatorManager.__instance

    def __init__(self):
        if CalculatorManager.__instance != None:
            raise Exception("Calculator manager is singleton!")
        else:
            CalculatorManager.__instance = self

    def show_menu(self):
        print("Choose your calculator:")
        print("1) Digit calculator\n2) Complex calculator\n3) Exit")
        try:
            calc_type = int(input())
            os.system("cls")
            if CalculatorType.DIGIT == calc_type:
                DigitConsoleCalculator(
                    CalculatorFactory.create()).show_calculator()
            elif CalculatorType.COMPLEX == calc_type:
                ComplexConsoleCalculator(
                    CalculatorFactory.create()).show_calculator()
            else:
                exit()
        except Exception as e:
            print(str(e))
            os.system("cls")
            self.show_menu()
