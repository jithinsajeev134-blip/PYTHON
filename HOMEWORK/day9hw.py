# Base class Account
class Account:
    def __init__(self, name: str, balance: float):
        self._name = name        # protected attribute
        self._balance = balance  # protected attribute

    def __add__(self, other):
        # Add balances of two accounts
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented

    def display_details(self):
        return f"Account Holder: {self._name}, Balance: {self._balance:.2f}"


# SavingsAccount subclass
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05  # 5% interest


# CurrentAccount subclass
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02  # 2% interest


# Main program
if __name__ == "__main__":
    # Create accounts
    savings = SavingsAccount("Ravi", 10000.0)
    current = CurrentAccount("Anjali", 15000.0)

    # Display details
    print("=== Account Details ===")
    print(f"Name: {savings._name}, Balance: {savings._balance:.2f}, Interest: {savings.calculate_interest():.2f}")
    print(f"Name: {current._name}, Balance: {current._balance:.2f}, Interest: {current.calculate_interest():.2f}")

    # Total balance using + operator
    total_balance = savings + current
    print("\n=== Total Balance ===")
    print(f"Combined Balance of {savings._name} and {current._name}: {total_balance:.2f}")