import os
from calculator_type import CalculatorType
from console_calculator_factory import ConsoleCalculatorFactory


class CalculatorManager:
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        print("Choose your calculator:")
        print("1) Digit calculator\n2) Complex calculator\n3) Exit")
        try:
            calc_type = int(input())
            os.system("cls")
            ConsoleCalculatorFactory.initialize()
            if CalculatorType.DIGIT == calc_type:
                ConsoleCalculatorFactory.create_digit_calculator().show_calculator()
            elif CalculatorType.COMPLEX == calc_type:
                ConsoleCalculatorFactory.create_complex_calculator().show_calculator()
            else:
                exit()
        except Exception as e:
            print(str(e))
            os.system("cls")
            self.show_menu()
