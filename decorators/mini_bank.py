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

def limit_large_transactions(max_amount):
    def decorator(func):
        @wraps(func)
        def wrapper(self, amount, *args, **kwargs):
            if amount > max_amount:
                raise ValueError("You overcame the maximum transaction amount. Try with smaller amount.")
            return func(self, amount, *args, **kwargs)
        return wrapper
    return decorator


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
   
    @limit_large_transactions(10000)
    @time_transaction
    @validate_transaction
    @log_transaction
    def deposit(self, amount):
        self.balance += amount

    @limit_large_transactions(10000)
    @time_transaction
    @validate_transaction
    @log_transaction
    def withdraw(self, amount):
        self.balance -= amount

b = BankAccount(owner="Banker")
print(b.balance)
b.deposit(15000)
print(b.balance)
b.withdraw(20000)
print(b.balance)
