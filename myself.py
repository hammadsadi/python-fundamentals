import datetime

day = datetime.datetime.today().strftime("%A")

if day == "Friday":
    print("Jumma Mubarak! May Allah bless you with mercy, blessings, and peace.")
else:
    print(f"Today is {day} Continue your regular worship and keep doing good deeds.")