from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"{self.name} is an Admin user."


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"{self.name} is a Guest user."


admin_user = Admin("rohit", 2019)
guest_user = Guest("kohli", 2022)

print(admin_user.get_role())
print(admin_user.account_age())
print(admin_user)

print()

print(guest_user.get_role())
print(guest_user.account_age())
print(guest_user)
