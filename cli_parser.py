from parser_interface import ParserInterface


class CLIParser(ParserInterface):
    """Concrete strategy implementation."""

    def parse(self):
        operation = input()
        if operation == "exit":
            raise SystemExit()
        str_number = input()
        try:
            return (operation, float(str_number))
        except ValueError:
            return (operation, complex(str_number))
