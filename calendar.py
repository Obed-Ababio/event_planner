# OBED ABABIO
import csv
from event import Event
from contact import Contact
from meeting import Meeting


class Calendar:
    "main object for event scheduling"

    def __init__(self):
        self.event_list   = []
        self.contacts = []
    
    def add_invitees_to_contacts(self, event):
        "adds attendees of an event to the contacts list"

        if isinstance(event, Meeting):
            old_contact_list = []
            for contact in self.contacts:
                old_contact_list.append(contact.person_name)
            for name in event.event_contacts:
                if name not in old_contact_list:
                    new_contact = Contact(name)
                    self.contacts.append(new_contact)

    def add_event_to_cal(self, event):
        "adds an event passed as an argument to the calendar"

        self.event_list.append(event)
        self.event_list.sort()
        self.add_invitees_to_contacts(event)

    
    @staticmethod
    def is_conflict(s1, e1, s2, e2):
        "takes start and end times of two events and determines if they overlap"

        return (s1 < e2) and (e1 > s2)

    def check_conflict(self, new_event):
        "checks event passed as argument against events to prevent conflict"
        """Returns conflicting event(s) in list. Returns none otherwise"""

        conflicts = []
        str1 = str(new_event.start_time.split(":")[0] + new_event.start_time.split(":")[1])
        str2 = str(new_event.end_time.split(":")[0]   + new_event.end_time.split(":")[1])
        new_event_st = int(str1)
        new_event_et = int(str2)
        for old_event in self.event_list:
            if old_event.event_date == new_event.event_date:
                str1 = str(old_event.start_time.split(":")[0] + old_event.start_time.split(":")[1])
                str2 = str(old_event.end_time.split(":")[0]   + old_event.end_time.split(":")[1])
                old_event_st = int(str1)
                old_event_et = int(str2)
                if self.is_conflict(new_event_st, new_event_et, old_event_st, old_event_et):
                    conflicts.append(old_event)
        return conflicts
    
    def display_contacts(self):
        "displays all event attendees in sorted order"
        
        contacts = []
        for contact in self.contacts:
            if contact.person_name not in contacts:
                contacts.append(contact.person_name)
        contacts = sorted(contacts)
        return contacts
    
    def delete_event(self, index):
        "deletes event within calendar at index"

        if index < len(self.event_list):
            event = self.event_list[index - 1]
            del self.event_list[index - 1]
            return event
    
    def display_events(self, name):
        "returns a list of all events in calendar or events attended by name"

        if name == "all":
            return self.event_list
        else:
            event_list = []
            for event in self.event_list:
                if isinstance(event, Meeting) and name in event.event_contacts:
                    event_list.append(event)
            return event_list  

    def save_calendar(self):
        "saves all events into a calendar.csv file"

        rows = []
        for event in self.event_list:
            event_info = []
            event_info.append(event.event_name)
            event_info.append(event.event_date)
            event_info.append(event.start_time)
            event_info.append(event.end_time)
            if isinstance(event, Meeting):
                for person in event.event_contacts:
                    event_info.append(person)
            rows.append(event_info)
        
        filename = "calendar.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)

    def purge(self):
        self.event_list = []
        self.contacts = []

    def load_events(self):
        "loads events from a csv file to calendar"

        self.purge()
        filename = "calendar.csv"
        event_fields = 4

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                name = row[0]
                date = row[1]
                start = row[2][:5]
                end = row[3][:5]
                participants = list(row[4:])
                if len(row) > event_fields:
                    new_event = Meeting(name, date, start, end, participants)
                else:
                    new_event = Event(name, date, start, end)
                self.add_event_to_cal(new_event)





            





