#Day of the Week
#Given a number 0-6, prints the corresponding day of the week


day_key = {
    "0": "Sunday",
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday"
}

day = str(input("Day (0-6)? "))

print(day_key[day])
