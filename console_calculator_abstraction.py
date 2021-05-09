from abc import ABC
from calculator_logic.calculator import Calculator


class ConsoleCalculatorAbstraction(ABC):
    """The CalculatorAbstraction defines the interface for the "control" part of the two class hierarchies."""
    def __init__(self, input_obj):
        self.__input = input_obj
        self.__calculator = Calculator()

    @property
    def input_obj(self):
        return self.__input

    @property
    def calculator(self):
        return self.__calculator

    def show_calculator(self):
        pass
