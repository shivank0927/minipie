import random
import time

D1 = 'o\n'
D2 = 'oo\n'
D3 = 'ooo\n'
D4 = 'oooo\n'
D5 = 'ooooo\n'
D6 = 'oooooo\n'

faces = [D1, D2, D3, D4, D5, D6]


REWARD = 4
PENALTY = -1

def main():
    while True:

        random.shuffle(faces)

        one = random.choice(faces)
        two = random.choice(faces)
        three = random.choice(faces)
        four = random.choice(faces)
        five = random.choice(faces)
        six = random.choice(faces)

        
        
        print(one, two, three, four, five, six, sep="")

        time.sleep(1)

if __name__ == "__main__":
    main()
