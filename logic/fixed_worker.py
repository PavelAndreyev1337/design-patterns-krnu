from .worker import Worker


class FixedWorker(Worker):
    """Worker with hourly pay fixed pay."""
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name)
        self.__fixed_salary = fixed_salary
        self.__monthly_salary = 0
        self.calculate_salary()
 
    @property
    def monthly_salary(self):
        return self.__monthly_salary

    def calculate_salary(self):
        self.__monthly_salary = self.__fixed_salary
        return self.__monthly_salary
