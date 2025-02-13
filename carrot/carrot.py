import random

print("Carrot in a Box - A Bluffing Game")
print("Two players, one box has a carrot. Decide to swap or not!\n")

p1 = input("Player 1, enter name: ")
p2 = input("Player 2, enter name: ")
print(f"{p1} has the RED box. {p2} has the GOLD box.")

print(f"{p1}, you will look inside your box while {p2} will not be looking at your box")
input("Press enter when ready...")

carrot = random.choice([True, False])

if carrot:
    print("You see a carrot inside your box!")
else:
    print("Your box is empty.")

input("Press Enter to continue...")
print("\n" * 100)  # clear scrren!
print(f"Now both players are allowed to look their boxes")
input("Press Enter to continue...")

print(f"{p2}, do you want to swap boxes? YES/NO")
while True:
    swap = input(">>> ").strip().upper()
    if swap in ("YES", "NO"):
        break
    print("enter YES or NO.")

if swap == "YES":
    carrot = not carrot  # swapp

input("Press Enter to reveal the winner...")
print()

if carrot:
    print(f"{p1} wins! The carrot was in their box.")
else:
    print(f"{p2} wins! The carrot was in their box.")

print("Thanks for playing!")

