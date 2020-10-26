# OBED ABABIO
from tabulate import tabulate
from event import list_to_string
from event import Event


class Meeting(Event):
    "event types that involve other contacts"

    def __init__(self, Title, Date, Start, End, Invitees):
        Event.__init__(self, Title, Date, Start, End)
        self.event_contacts = Invitees

    def __str__(self):
        "prints meeting within grid"

        contacts = "Participants: " + list_to_string(self.event_contacts)
        name = self.event_name + "\n"
        date = "Date: " + self.event_date + "\n"
        time_range = "Time: " + self.start_time + " - " + self.end_time + "\n"
        text = [name + date + time_range + contacts]
        output = tabulate([text], tablefmt="grid")
        return output

    def __lt__(self, other):
        if self.event_date == other.event_date:
            return self.start_time < self.end_time
        else:
            return self.event_date < other.event_date
        
