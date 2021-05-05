
from abc import ABC, abstractmethod


class Worker(ABC):
    """Abstract class for worker."""
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    @abstractmethod
    def monthly_salary(self):
        pass
    
    @abstractmethod
    def calculate_salary(self):
        pass

    def __lt__(self, other):
        if self.monthly_salary > other.monthly_salary:
            return True
        elif self.monthly_salary == other.monthly_salary:
            return True if min(self.name[0], other.name[0]) == self.name[0] else False

    def __repr__(self):
        return f"Id: {self.id} Name: {self.name} Monthly salary: {self.monthly_salary}"
