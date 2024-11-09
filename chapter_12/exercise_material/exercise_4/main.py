import json
from user import User

def load_users(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return {user_id: User(**user_info) for user_id, user_info in data.items()}
    except FileNotFoundError:
        return {}

def save_users(filename, users):
    with open(filename, 'w') as file:
        json.dump({user_id: user.__dict__ for user_id, user in users.items()}, file)

def authenticate(users):
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")
    if user_id in users and users[user_id].pin == pin:
        return users[user_id]
    else:
        print("Invalid User ID or PIN.")
        return None

def atm_menu(user):
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Transfer\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            user.check_balance()
        
        elif choice == '2':
            account = input("Withdraw from (checking/savings): ").lower()
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(account, amount)
        
        elif choice == '3':
            from_account = input("Transfer from (checking/savings): ").lower()
            to_account = 'checking' if from_account == 'savings' else 'savings'
            amount = float(input("Enter amount to transfer: "))
            user.transfer(from_account, to_account, amount)
        
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        
        else:
            print("Invalid option. Please try again.")

def main():
    users = load_users('chapter_12/exercise_material/exercise_4/users.json')
    
    user = authenticate(users)
    if user:
        atm_menu(user)
    
    save_users('users.json', users)

if __name__ == "__main__":
    main()
