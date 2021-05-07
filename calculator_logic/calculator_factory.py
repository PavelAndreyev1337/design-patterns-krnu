from .calculator import Calculator


class CalculatorFactory:
    """Class declares the factory method. """
    @staticmethod
    def create():
        return Calculator()
