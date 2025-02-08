import random
from messages import LevelOneRules, LevelTwoRules, LevelThreeRules

def hint(user, computer):
    if user == computer:
        return "Correct!"
    
    for i in range(len(computer)):
        if user[i] == computer[i]:
            return "Fermi!"
        elif user[i] in computer:
            return "Pico!"
        else:
            return "Bagels!"
        
def game(level, digits):
    computer = str(random.randint(10**(digits - 1), 10**digits - 1))
    count = 1
    tries = 10
    
    if level == 1:
        print(LevelOneRules())
    elif level == 2:
        print(LevelTwoRules())
    elif level == 3:
        print(LevelThreeRules())
    else:
        print("Are you retarded")

    while count <= tries:
        user = input(f"Guess #{count}:  ")

        if user == computer:
            print(f"Congratulatiions, You guessed the number in {count} tries 🎊")
            return
        
        print(hint(user, computer))
        count += 1
        print(f"You have {tries - count + 1} tries left!\n")

    print(f"You lost! The correct number was {computer}. Better luck next time!")

def main():
    try:
        difficulty = int(input("Choose difficulty level:\n1. Level 1\n2. Level 2\n3. Level 3\nYour choice: "))
        
        if difficulty == 1:
            game(level=1, digits=1)
        elif difficulty == 2:
            game(level=2, digits=2)
        elif difficulty == 3:
            game(level=3, digits=2)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    except ValueError:
        print("Invalid input! Please enter a number 1, 2, or 3.")

if __name__ == "__main__":
    main()