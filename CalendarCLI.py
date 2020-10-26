# OBED ABABIO
import sys
from event import Event
from meeting import Meeting
from calendar import Calendar
from event import list_to_string

if __name__ == "__main__":
    cal = Calendar()

    while(1):
        command = input("Enter command\nview, contacts, create, delete, load, save, quit\n")

        if command == "create":
            Invitees = []
            Title = input("Title?\n")
            Date = input("Date? (YYYY-MM-DD)\n")
            Start = input("Start time? (HH:MM in 24-hour format)\n")
            End = input("End time? (HH:MM in 24-hour format)\n")
            choice = input("Invite others? \"yes\" or \"no\"\n")

            if choice == "yes":
                while(True):
                    name = input("\"<Contact name>\" or \"done\" \n")
                    if name == "done":
                        break
                    if name not in Invitees:
                        Invitees.append(name)
                new_event = Meeting(Title, Date, Start, End, Invitees)
            else:
                new_event = Event(Title, Date, Start, End)
            
            conflict_list = cal.check_conflict(new_event)
            # CHECK IF WE ONLY PRINT FIRST CONFLICT ALL LIST OF ALL CONFLICTS!!!
            if len(conflict_list) > 0:
                print("Cannot add this event because it conflicts with this event...\n")
                print(conflict_list[0])
            else:
                cal.add_event_to_cal(new_event)

        
        if command == "view":
            choice = input("\"all\" or \"<contact name>\"\n")
            events = cal.display_events(choice)
            for event in events:
                print(event)

        if command == "contacts":
            contacts = cal.display_contacts()
            for person in contacts:
                print(person)

        if command == "delete":
            event_number = input(
                "Which event?\nEnter an index 1..n to identify the event from the sorted list\n")
            event = cal.delete_event(int(event_number))
            print("Deleted this event...")
            print(event)
        
        if command == "save":
            cal.save_calendar()
            print("Saved to calendar.csv")
        
        if command == "load":
            cal.load_events()
            print("Loaded from calendar.csv")

        if command == "quit":
            sys.exit(0)
    


