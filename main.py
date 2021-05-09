import os
from console_calculator import ConsoleCalculator
from calculator_type import CalculatorType
from digit_input import DigitInput
from complex_input import ComplexInput


if __name__ == '__main__':
    print("Choose your calculator:")
    print("1) Digit calculator\n2) Complex calculator")
    try:
        calc_type = int(input())
        os.system("cls")
        if CalculatorType.DIGIT == calc_type:
            ConsoleCalculator(DigitInput()).show_calculator()
        elif CalculatorType.COMPLEX == calc_type:
            ConsoleCalculator(ComplexInput()).show_calculator()
        else:
            raise Exception("Calculator type does not exist!")
    except Exception as e:
        print(str(e))
