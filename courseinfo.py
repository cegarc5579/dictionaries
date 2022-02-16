courseroom = {
    "CS101": 3004,
    "CS102": 4501,
    "CS103": 6755,
    "NT110": 1244,
    "CM241": 1411,
}
coursename = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee",
}
coursetime = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m.",
}


user_input = input("Enter Course Number: ")

if user_input in courseroom.keys():
    print(
        "Room #:",
        courseroom[user_input],
        "Instructor Name:",
        coursename[user_input],
        "Course Time:",
        coursetime[user_input],
    )
else:
    print("Information not found.")
