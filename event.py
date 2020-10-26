# OBED ABABIO
from tabulate import tabulate

def list_to_string(arr):
    ret = ""
    for i in range(len(arr)):
        if i == 0:
            ret = ret + str(arr[i])
        else:
            ret = ret + ", "+ str(arr[i])
    return ret

class Event:
    "contains detials of each scheduled event"

    def __init__(self, Title, Date, Start, End):
        self.event_name = Title
        self.event_date = Date
        self.start_time = Start
        self.end_time = End
    
    def __str__(self):

        "prints event wihtin grid"
        
        name = self.event_name + "\n"
        date = "Date: " + self.event_date + "\n"
        time_range = "Time: " + self.start_time + " - " + self.end_time
        text = [name + date + time_range]
        output = tabulate([text], tablefmt="grid")
        return output

    
    def __lt__(self, other):
        if self.event_date == other.event_date:
            return self.start_time < self.end_time
        else:
            return self.event_date < other.event_date
        




