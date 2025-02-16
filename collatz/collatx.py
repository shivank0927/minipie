def collatz(number):
    while number != 1:
        print(number, end=", ")
        if number % 2 == 0:
            number = number // 2 # collatz sequence logic
        else:
            number = (number * 3) + 1
    print(number) 

def main():
    try:
        number = int(input("E\enter a number to start the Collatz sequence: "))
        if number <= 0:
            print("enter a positive number.")
            return
        collatz(number)
    except ValueError:
        print("error!.")

if __name__ == "__main__":
    main()
