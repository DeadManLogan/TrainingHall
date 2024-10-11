class User:
    def __init__(self, user_id, pin, checking_balance=0, savings_balance=0):
        self.user_id = user_id
        self.pin = pin
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def check_balance(self):
        print(f"Checking Account Balance: ${self.checking_balance}")
        print(f"Savings Account Balance: ${self.savings_balance}")
    
    def withdraw(self, account_type, amount):
        if account_type == 'checking':
            if self.checking_balance >= amount:
                self.checking_balance -= amount
                print(f"Withdrawn ${amount} from Checking Account. New balance: ${self.checking_balance}")
            else:
                print("Insufficient funds in Checking Account.")
        elif account_type == 'savings':
            if self.savings_balance >= amount:
                self.savings_balance -= amount
                print(f"Withdrawn ${amount} from Savings Account. New balance: ${self.savings_balance}")
            else:
                print("Insufficient funds in Savings Account.")
    
    def transfer(self, from_account, to_account, amount):
        if from_account == 'checking' and self.checking_balance >= amount:
            self.checking_balance -= amount
            self.savings_balance += amount
            print(f"Transferred ${amount} from Checking to Savings. New Checking balance: ${self.checking_balance}, Savings balance: ${self.savings_balance}")
        elif from_account == 'savings' and self.savings_balance >= amount:
            self.savings_balance -= amount
            self.checking_balance += amount
            print(f"Transferred ${amount} from Savings to Checking. New Checking balance: ${self.checking_balance}, Savings balance: ${self.savings_balance}")
        else:
            print("Insufficient funds for transfer.")
        
            
