import datetime
import sys
import random

def birthdays(number):
    """Generate a list of random birthdays within the year 2000."""
    birthday_list = []
    for _ in range(number):    
        year = datetime.date(2000, 1, 1)
        day = datetime.timedelta(days=random.randint(0, 364)) 
        birthday = year + day  # random birthdays
        birthday_list.append(birthday)
    return birthday_list

def match(birthday_list):
    """Check if any birthday appears more than once in the list."""
    if len(birthday_list) == len(set(birthday_list)): 
        return None
    
    for i, birthx in enumerate(birthday_list):
        for birthy in birthday_list[i + 1:]:  # starts iteration from next element
            if birthx == birthy:
                return birthx

def main():
    """Run the birthday paradox simulation."""
    while True:
        number = int(input("Enter Number of dates you want to generate for simulation of Birthday Paradox. MAX: 100\n> "))
        if 0 < number < 100:
            break
    
    print()
    try:
        count = int(input("Enter The Number of simulations you want to perform, LIMIT: 500,000\n> "))
        simulations = 0
        
        for i in range(count):  # running simulations
            print(f"{i} simulations run.....\n")
            birthday_list = birthdays(number)
            if match(birthday_list) is not None:
                simulations += 1
        
        probability = round((simulations / count) * 100, 2)
        sys.exit(f"In {count} simulations and {number} birthday dates, the probability of 2 people having the same birthday is {probability}%")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()