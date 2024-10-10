import csv

class Attendee:
    def __init__(self, name, company, country, email):
        self.name = name
        self.company = company
        self.country = country
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Company: {self.company}, Country: {self.country}, Email: {self.email}"
    
class Conference:
    def __init__(self):
        self.file = "chapter_12/exercise_material/exercise_3/attendee_list.csv"
        self.fields = ["Name", "Company", "Country", "Email"]
        self.attendees = []
        self.load_attendees()

    def load_attendees(self):
        with open(self.file) as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                attendee = Attendee(row[0], row[1], row[2], row[3])
                self.attendees.append(attendee)

    def add_attendee(self, name, company, country, email):
        new_attendee = Attendee(name, company, country, email)
        self.attendees.append(new_attendee)
        self.save_attendees()

    def save_attendees(self):
        with open(self.file, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            for attendee in self.attendees:
                writer.writerow({'Name': attendee.name, 'Company': attendee.company, 'Country': attendee.country, 'Email': attendee.email})

    def display_info(self, name):
        for attendee in self.attendees:
            if attendee.name == name:
                print(attendee)

    def delete_attendee(self, name):
        self.attendees = [attendee for attendee in self.attendees if attendee.name != name]
        self.save_attendees()

    def list_all(self):
        for attendee in self.attendees:
            print(f"Name: {attendee.name}, Email: {attendee.email}")

    def list_by_country(self, country):
        for attendee in self.attendees:
            if attendee.country == country:
                print(f"Name: {attendee.name}, Email: {attendee.email}")