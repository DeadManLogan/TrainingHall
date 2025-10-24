from functools import wraps
from datetime import datetime

def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} executed at {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Execution completed.")
        return result
    return wrapper


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @log_transaction
    def deposit(self, amount):
        self.balance += amount

    @log_transaction
    def withdraw(self, amount):
        self.balance -= amount

b = BankAccount(owner="Banker")
print(b.balance)
b.deposit(10)
print(b.balance)
b.withdraw(2)
print(b.balance)
