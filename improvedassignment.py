import csv

from assignmodes import make_top_rooms, make_proam_rooms, make_random_rooms, make_fcfs_rooms

class Participant:
    def __init__(self, name, languages, level, is_speaker, has_priority, team_name):
        self.name = name
        self.language = languages           # ENG, GER
        self.level = level                  # BEGINNER, ADVANCED, DONTKNOW
        self.is_speaker = is_speaker        # True, False
        self.has_priority = has_priority    # True, False
        self.team_name = team_name

class Room:
    def __init__(self, name, chair, mode, positions):
        self.name = name
        self.chair = chair          # Chair Judge of the room
        self.positions = positions  # List of participants in the room
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

def make_rooms(participants, mode, amount_of_rooms):
    rooms = [];
    if mode == "TOP":
        rooms = make_top_rooms(participants, amount_of_rooms)
    if mode == "PROAM":
        rooms = make_proam_rooms(participants, amount_of_rooms)
    if mode == "RANDOM":
        rooms = make_random_rooms(participants, amount_of_rooms)
    if mode == "FCFS":
        rooms = make_fcfs_rooms(participants, amount_of_rooms)
    return rooms

def save_rooms(rooms, filename):
    print("Saving rooms to " + filename)

def main():
    participants = load_participants(input("Participants File: "))
    while len(participants) == 0 or participants == None:    # Check if participants are loaded
        print("<!> No participants found in file")
        participants = load_participants(input("Participants File: "))

    amout_of_rooms = int(input("Amount of rooms: "))
    while amout_of_rooms < 1:   # Check if amount of rooms is greater than 0
        print("<!> Amount of rooms must be greater than 0")
        amout_of_rooms = int(input("Amount of rooms: "))

    roommode = input("Mode (TOP, PROAM, RANDOM, FCFS): ")
    while roommode not in ["TOP", "PROAM", "RANDOM", "FCFS"]:   # Check if mode is valid
        print("<!> Mode must be TOP, PROAM, RANDOM or FCFS")
        roommode = input("Mode: ")

    rooms = make_rooms(participants, roommode, amout_of_rooms)

    save_rooms(rooms, input("Output File: "))
    print("... Completed!")

if __name__ == "__main__":
    main()