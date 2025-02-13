import random
import sys


def main():
    money = 10000
    while True:
        bet = getbet()
        if 0 >= bet >= 10000:
            print("error in bet")
        elif bet == ".quit":
            sys.exit(".quitted")
        else:
            while True:
                pass
        pass


def getbet():

    bet = int(input(f"Place your bet or .quit to exit the game\n>>>"))
    return bet


if __name__ == "__main__":
    main()