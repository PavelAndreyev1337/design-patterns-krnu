from input_interface import InputInterface


class ComplexInput(InputInterface):
    def parse(self):
        return complex(input())
