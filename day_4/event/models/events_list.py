from models.event import Event
import datetime 

event1 = Event(datetime.date(2022, 11, 28), 'Company Party', 30, False, 'R15', 'New product launch')
event2 = Event(datetime.date(2022, 12, 2), 'Birthday Party', 25, False, 'R06', 'Birthday party for Ron! presents optional.')
event3 = Event(datetime.date(2022, 12, 8), 'Pancake Day', 20, True, 'R01', 'Pancakes for everyone! bring your own fruit...')
event4 = Event(datetime.date(2022, 12, 15), 'Retirement Party', 15, False, 'R10', 'Retirement party for Jen, remember to sign her card!')

events = [event1, event2, event3, event4]

def get_event(event_index):
    return events[event_index]

def add_event(new_event):
    events.append(new_event)