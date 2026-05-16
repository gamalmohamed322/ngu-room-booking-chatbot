AVAILABLE_ROOMS = {
    "study_room": [
        "Library Study Room 1",
        "Library Study Room 2",
        "Library Study Room 3"
    ],
    "meeting_room": [
        "Meeting Room A",
        "Meeting Room B"
    ],
    "lab_room": [
        "CS Lab 1",
        "CS Lab 2",
        "Engineering Lab"
    ],
    "club_activity_room": [
        "Student Activity Room",
        "Club Meeting Room"
    ]
}


def get_all_rooms():
    rooms = []

    for room_type, room_names in AVAILABLE_ROOMS.items():
        for room_name in room_names:
            rooms.append({
                "room_type": room_type,
                "room_name": room_name
            })

    return rooms


def is_valid_room(room_name):
    all_rooms = get_all_rooms()

    for room in all_rooms:
        if room["room_name"].lower() == room_name.lower():
            return True

    return False
