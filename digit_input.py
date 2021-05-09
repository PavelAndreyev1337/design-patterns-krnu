from input_interface import InputInterface


class DigitInput(InputInterface):
    def parse(self):
        return float(input())
