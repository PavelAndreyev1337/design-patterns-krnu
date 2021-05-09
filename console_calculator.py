import os
from console_calculator_abstraction import ConsoleCalculatorAbstraction


class ConsoleCalculator(ConsoleCalculatorAbstraction):
    def show_calculator(self):
        print(self.calculator.memory_number)
        operation = input()
        if operation == "exit":
            exit()
        try:
            self.calculator.memory_number = self.calculator.calculate(self.calculator.memory_number,
                                                                      self.input_obj.parse(), operation)
            os.system("cls")
        except Exception as e:
            os.system("cls")
            print(str(e))
        finally:
            self.show_calculator()
