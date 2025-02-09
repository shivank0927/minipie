import datetime
import sys
import random
import math
number = int(input(f"Enter to check for paradox (Maximum: 100)"))

if number >  100:
    sys.exit("fuck you")

def birthdays(number):
    birthdays = []
    for i in range(number):    
        year = datetime.date(2000, 1, 1)
        day = datetime.timedelta(random.randint(0, 364))
        birthday = year + day
        birthdays.append(birthday)
    return birthdays

def match(birthdays):
    if len(birthdays) == len(set(birthdays)): # since sets eliminate multiple instances, if both are equals means there's no match
        return "NOT FOUND"
    # tricky loop to check birthday with every other birthday!

    for i, birthx in enumerate(birthdays):
        for j, birthy in enumerate(birthdays[i + 1:]): # starts iteration from second element [1]
            if i == j:
                return birthx

print(match(birthdays(number)))
simulations = 0
for i in range(100_000):
    print(i, "simulations run...")
    birthday = birthdays(number)
    if match(birthday) != None:
        simulations += 1

print(round(simulations / 100000 * 100, 2))