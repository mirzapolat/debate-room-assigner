import random
from improvedassignment import Room, Participant

def make_top_rooms(participants):
    return []

def make_proam_rooms(participants):
    return []

def make_random_rooms(participants, amount_of_rooms):
    random.shuffle(participants)
    rooms = []

    priority_speaker_eng = [p for p in participants if p.language == 'ENG' and p.is_speaker == True and p.is_priority == True]
    normal_speaker_eng = [p for p in participants if p.language == 'ENG' and p.is_speaker == True and p.is_priority == False]

    priority_speaker_ger = [p for p in participants if p.language == 'GER' and p.is_speaker == True and p.is_priority == True]
    normal_speaker_ger = [p for p in participants if p.language == 'GER' and p.is_speaker == True and p.is_priority == False]

    priority_judge_eng = [p for p in participants if p.language == 'ENG' and p.is_speaker == False and p.is_priority == True]
    normal_judge_eng = [p for p in participants if p.language == 'ENG' and p.is_speaker == False and p.is_priority == False]

    for r in range (1, amount_of_rooms + 1):
        if r % 2 == 1:  # English Room first
            if (sum(1 for p in participants if p.language == 'ENG' and p.is_speaker == True) >= 8): # At least 8 speakers
                list = []
                for p in participants:
                    if p.language == 'ENG' and p.is_speaker == True:
                        list.append(p)
                rooms.append(Room("Room " + str(r), str(r), "RANDOM", list))



    return []

def make_fcfs_rooms(participants):
    return []