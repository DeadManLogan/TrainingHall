import json

class User:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

class ATM:
    def __init__(self):
        print("Wecome to ATM")
        name = input("Enter you username: ")
        pin = input("Enter your pin: ")
        self.user = User(name, pin)
        self.load_users()
        self.authenticate()
        while self.auth == False:
            name = input("Enter you username: ")
            pin = input("Enter your pin: ")
            self.user = User(name, pin)
            self.authenticate()

    def load_users(self):
        with open("chapter_12/exercise_material/exercise_4/users.json", 'r') as file:
            users = json.load(file)
        self.users = users

    def get_users(self):
        return self.users
    
    def authenticate(self):
        for user in self.users:
            if self.user.name == user["name"]:
                if self.user.pin == user["pin"]:
                    print("You have authenticated successfully!!")
                    self.auth = True
                else:
                    self.auth = False
                    print("Wrong credentials.")
            
