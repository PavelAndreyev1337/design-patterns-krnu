from console_calculator import ConsoleCalculator
from calculator_logic.calculator_factory import CalculatorFactory


class ConsoleCalculatorFactory:
    __digit_calculator = None
    __complex_calculator = None

    @classmethod
    def initialize(cls):
        cls.__digit_calculator = ConsoleCalculator(CalculatorFactory.create())
        cls.__complex_calculator = ConsoleCalculator(
            CalculatorFactory.create(), complex)

    @classmethod
    def create_digit_calculator(cls):
        return cls.__digit_calculator.clone()

    @classmethod
    def create_complex_calculator(cls):
        return cls.__complex_calculator.clone()
