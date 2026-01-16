from abc import ABC, abstractmethod

CURRENT_YEAR = 2025


class User(ABC):
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year

    def years_on_platform(self):
        return CURRENT_YEAR - self.join_year

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} | {self.role()} | {self.years_on_platform()} years on platform"


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"


customer = Customer("Alice", 2020)
vendor = Vendor("Bob", 2018)

print(customer)
print(vendor)
