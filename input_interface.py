from abc import ABC, abstractmethod


class InputInterface(ABC):
    """The Input defines the interface for all implementation classes."""
    @abstractmethod
    def parse(self):
        pass
