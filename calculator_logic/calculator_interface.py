from abc import ABC, abstractmethod


class CalculatorInterface(ABC):
    """ Interface for calculator. """
    @property
    @abstractmethod
    def memory_number(self):
        pass

    @abstractmethod
    def sum(self, first, second):
        pass

    @abstractmethod
    def subtract(self, first, second):
        pass

    @abstractmethod
    def multiply(self, first, second):
        pass

    @abstractmethod
    def divide(self, first, second):
        pass

    @abstractmethod
    def calculate(self, first, second, operation):
        pass
