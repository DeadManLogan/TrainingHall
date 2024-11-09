from conference import Attendee, Conference

def main():
    manager = Conference()
    # manager.add_attendee("Blade", "Midnight Suns", "Earth-616", "error")
    # manager.display_info("Blade")
    # manager.delete_attendee("Blade")
    manager.list_by_country("UK")
    # manager.list_all()

if __name__ == "__main__":
    main()