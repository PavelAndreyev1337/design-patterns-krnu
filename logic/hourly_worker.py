from .worker import Worker


class HourlyWorker(Worker):
    """Hourly wage worker."""

    def __init__(self, id, name, hourly_rate):
        super().__init__(id, name)
        self.__hourly_rate = hourly_rate
        self.__monthly_salary = 0
        self.calculate_salary()
    
    @property
    def monthly_salary(self):
        return self.__monthly_salary

    def calculate_salary(self):
        self.__monthly_salary = 5 * 4 * 8 * self.__hourly_rate
        return 5 * 4 * 8 * self.__hourly_rate
