import os
from calculator_logic.calculator import Calculator


class ConsoleCalculator:
    def __init__(self, parser):
        self.__calculator = Calculator()
        self.__parser = parser

    @property
    def parser(self):
        return self.__parser

    @parser.setter
    def parser(self, parser):
        self.__parser = parser

    def show_calculator(self):
        print(self.__calculator.memory_number)
        try:
            operation, number = self.__parser.parse()
            self.__calculator.memory_number = self.__calculator.calculate(self.__calculator.memory_number,
                                                                          number, operation)
            os.system("cls")
        except SystemExit:
            os._exit(0)
        except Exception as e:
            os.system("cls")
            print(str(e))
        finally:
            self.show_calculator()
