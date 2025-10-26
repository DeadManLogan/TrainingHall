from functools import wraps
from datetime import datetime
import time

def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} executed at {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Execution completed.")
        return result
    return wrapper

def time_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Transaction took {end - start:.2f} seconds.")
        return result
    return wrapper

def validate_transaction(func):
    @wraps(func)
    def wrapper(self, amount, *args, **kwargs):
        if func.__name__ == "withdraw":
            if self.balance - amount < 0:
                raise ValueError("Cannot proceed with transaction. New balance will be negative.")
            elif amount < 0:
                raise ValueError("Cannot withdraw negative amount.")
        elif func.__name__ == "deposit":
            if amount < 0:
                raise ValueError("Cannot deposit negative amount.")
        return func(self, amount, *args, **kwargs)
    return wrapper


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
   
    @time_transaction
    @validate_transaction
    @log_transaction
    def deposit(self, amount):
        self.balance += amount

    @time_transaction
    @validate_transaction
    @log_transaction
    def withdraw(self, amount):
        self.balance -= amount

b = BankAccount(owner="Banker")
print(b.balance)
b.deposit(10)
print(b.balance)
b.withdraw(2)
print(b.balance)
b.withdraw(12)
print(b.balance)
