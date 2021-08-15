import json
from collections import OrderedDict
import datetime as dt

# tasks today
def ldall(action_type, current_date, current_week_day):
    if action_type == 'ldall':

        all_events = []
        data = json.load(open('time_recall_data.json'))

        for week_day in data[0]["scheduled"][0]:
            if week_day == current_week_day:
                for event in data[0]["scheduled"][0][week_day]:
                    all_events.append(event)
        for event in range(len(data[0]["singular"])):
            if str(current_date) == data[0]["singular"][event]['date']:
                all_events.append(data[0]["singular"][event])
        all_events = sort_events(all_events)
        for event in all_events:
            display_event(event)


# tasks within an hour
def now(action_type, current_time, current_date, current_week_day):
    if action_type == 'now':

        print("Current time:", current_time, '\n')
        all_events = []
        data = json.load(open('time_recall_data.json'))

        for week_day in data[0]["scheduled"][0]:
            if week_day == current_week_day:
                for event in data[0]["scheduled"][0][week_day]:
                    all_events.append(event)
        for event in range(len(data[0]["singular"])):
            if current_date == data[0]["singular"][event]['date']:
                all_events.append(data[0]["singular"][event])
        all_events = sort_events(all_events)
        for event in all_events:
            if abs(time_to_secs(str(current_time)) - time_to_secs(event['time']) < 3600):
                display_event(event)
        if not all_events:
            print("No events.")


def load_db(action_type):
    if action_type == 'lddb':
        data = json.load(open('time_recall_data.json'), object_pairs_hook=OrderedDict)
        print(json.dumps(data, indent=4))


def time_to_secs(time):
    time = time.split(':')
    time = int(time[0])*3600 + int(time[1])*60
    return time


def sort_events(events_array):
    array_to_sort = []
    for event in events_array:
        array_to_sort.append([event, time_to_secs(event['time'])])
    array_to_sort.sort(key=lambda k: k[1])
    for event in range(len(array_to_sort)):
        array_to_sort[event] = array_to_sort[event][0]
    return array_to_sort


def compare_dates(current_date, date):
    date = date.split("-")
    date = dt.date(int(date[0]), int(date[1]), int(date[2]))
    if current_date == date:
        return False
    if current_date > date:
        return True
    elif current_date > date:
        return False


def display_event(event):
    print("Event:", event['event'], '\n',
          "Time:", event['time'], '\n',
          "Notes:", event['notes'], '\n',
          "Special notes:", event['special'] if 'special' in event else '', '\n')


def delete_outdated(current_date):
    data = json.load(open('time_recall_data.json', 'rw+'))
    for event in range(len(data[0]["singular"])):
        if compare_dates(current_date, data[0]["singular"][event]['date']):
            print(data[0]["singular"][event]["location"])