import datetime


def is_conflict(s1, e1, s2, e2):
    "takes start and end times of two events and determines if they overlap"
    if s1 == s2 or e1 == e2: 
        return True
    return (s1 < e2) and (e1 > s2)



event1_st = int(input("event 1 start time: ").replace(":", ""))
event1_et = int(input("event 1 end time: ").replace(":", ""))
event2_st = int(input("event 2 start time: ").replace(":", ""))
event2_et = int(input("event 2 end time: ").replace(":", ""))
print(is_conflict(event1_st, event1_et, event2_st, event2_et))
