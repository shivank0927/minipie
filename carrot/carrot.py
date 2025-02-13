import sys
import random

print("""Welcome, It's a two player game enter your names\n
      Rules:\n""")
def main():
        p1 = input("Enter your name, player 1\n>>>").title().strip()
        p2 = input("Enter your name, player 2\n>>>").title().strip()

        print("""There are two boxes, one is gold and the other is lead\n
              choose one box out of the two, the person who gets to choose will\n
              be random. Good luck!""")
        
        while True:
            
            choose = random.randint(1, 2)
            while True:
                if choose == 1:
                    print(f"{p1} gets the chance to choose\nType which box do you wanna choose\n")
                    box = input()
                    if box == "gold":
                            pass
                    elif box == "lead":
                            pass
                    else:
                            print("Incorrect choice")

                    



