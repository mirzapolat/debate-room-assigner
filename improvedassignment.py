import csv
import random

from assignments import make_top_rooms, make_proam_rooms, make_random_rooms, make_fcfs_rooms

class Participant:
    def __init__(self, name, languages, level, is_speaker, has_priority, team_name):
        self.name = name
        self.language = languages           # ENG, GER
        self.level = level                  # BEGINNER, ADVANCED, DONTKNOW
        self.is_speaker = is_speaker        # True, False
        self.has_priority = has_priority    # True, False
        self.team_name = team_name

class Room:
    def __init__(self, name, chair, mode):
        self.name = name
        self.chair = chair          # Chair Judge of the room
        self.positions = []
        self.mode = mode            # TOP, BOTTOM, PROAM, ALL

# Loads all participants from a csv file
def load_participants(filename):
    participants = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header row
        for row in reader:
            if len(row) == 6:
                participant = Participant(*row)
                participants.append(participant)
    return participants

def make_rooms(participants, mode):
    rooms = [];
    if mode == "TOP":
        rooms = make_top_rooms(participants)
    if mode == "PROAM":
        rooms = make_proam_rooms(participants)
    if mode == "RANDOM":
        rooms = make_random_rooms(participants)
    if mode == "FCFS":
        rooms = make_fcfs_rooms(participants)
    return rooms

def save_rooms(rooms, filename):
    print("Saving rooms to " + filename)

def main():
    participants = load_participants(input("Participants CSV File:              "))
    amout_of_rooms = int(input("Amount of rooms:                    "))
    rooms = make_rooms(participants, input("Mode (TOP, PROAM, RANDOM, FCFS):    "))
    save_rooms(rooms, input("Output CSV File:                    "))
    print("... Completed!")

if __name__ == "__main__":
    main()