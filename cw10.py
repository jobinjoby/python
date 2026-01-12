from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, join_year):
        self._name = name
        self._join_year = join_year

    def years_on_platform(self):
        current_year = 2025
        return current_year - self._join_year

    @abstractmethod
    def role(self):
        pass

    def display_info(self):
        print(
            f"Name: {self._name} | "
            f"Role: {self.role()} | "
            f"Years on Platform: {self.years_on_platform()}"
        )


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"

customer1 = Customer("sachin", 2020)
vendor1 = Vendor("dhoni", 2018)

customer1.display_info()
vendor1.display_info()
