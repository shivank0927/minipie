import random
import sys

print("""In this traditional Japanese dice game, two dice are rolled in a bamboo\n
cup by the dealer sitting on the floor. The player must guess if the\n
dice total to an even (cho) or odd (han) number.\n""")

def main():
    money = 10000
    rounds = 5 

    while True:
        if money < 0:
            sys.exit("You're broke")
        bet = getbet()
        
        if bet <= 0 or bet > 10000:
            print("error in bet! bet must be between 1 - 10000.")
            continue 

        counter = 0 

        while counter < rounds:
            computer = roll()
            print("Rolling......\n")
            response = input("cho (even) OR  han (odd)?\n>>> ").strip().lower()

            if response not in ["cho", "han"]:
                print("Enter a correct choice (cho or han)!")
                continue  

            if (is_even(computer) and response == "cho") or (not is_even(computer) and response == "han"):
                money += bet
                print(f"YOU WON THE ROUND! TOTAL MONEY: {money}")
            else:
                money -= bet
                print(f"YOU LOSE! The number was {computer}. TOTAL MONEY: {money}")
            counter += 1

        ask = input("Type .quit to exit, or press Enter to continue: ").strip().lower()
        if ask == ".quit":
            sys.exit("Thanks for playing!")

def getbet():
    while True:
        bet = input("Place your bet (1-10,000) or type .quit to exit: ").strip()
        if bet.lower() == ".quit":
            sys.exit("Thanks for playing!")
        if bet.isdigit():
            return int(bet)
        print("Invalid input! Please enter a valid number.")

def roll():
    return random.randint(1, 6) + random.randint(1, 6)

def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    main()
