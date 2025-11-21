from abc import ABC, abstractmethod

CURRENT_YEAR = 2025

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        """Concrete method to calculate account age"""
        return CURRENT_YEAR - self.account_year

    @abstractmethod
    def get_role(self):
        """Abstract method that must be implemented by subclasses"""
        pass
class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name}, Account Age: {self.account_age()} years"

if __name__ == "__main__":
    admin1 = Admin("Alice", 2019)
    guest1 = Guest("Bob", 2023)

    
    print(admin1.get_role())   
    print(guest1.get_role())   

    print(admin1.account_age())  
    print(guest1.account_age())  

    print(admin1)  
    print(guest1)  