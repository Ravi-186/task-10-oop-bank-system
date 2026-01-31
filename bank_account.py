"""
TASK 10: Object-Oriented Programming (OOP)
Simulating basic bank operations using OOP concepts
"""

# ---------------- BASE CLASS ----------------
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulation (private attribute)

    # Getter method
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}")
        else:
            print("❌ Insufficient balance")

    # Display account details
    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.__balance}")


# ---------------- CHILD CLASS (INHERITANCE) ----------------
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.04):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Method overriding (Polymorphism)
    def display_details(self):
        super().display_details()
        print(f"Interest Rate: {self.interest_rate * 100}%")


# ---------------- MULTIPLE OBJECTS & OPERATIONS ----------------
account1 = BankAccount("Ravi Tej", 5000)
account2 = SavingsAccount("Anjali", 10000)

print("\n--- Bank Account ---")
account1.display_details()
account1.deposit(2000)
account1.withdraw(3000)

print("\n--- Savings Account ---")
account2.display_details()
account2.deposit(5000)
account2.withdraw(2000)
