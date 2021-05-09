from abc import ABC, abstractmethod


class ParserInterface(ABC):
    """The ParserInterface is interface declares common  operations."""

    @abstractmethod
    def parse(self):
        pass
