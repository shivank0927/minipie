import sys
from text import text

def main():
    prompt = input("Enter a Word") 
    if prompt == "":
        sys.exit("error")
    bitmap = text() # patterns
    for line in bitmap.splitlines():
        for i, bit in enumerate(line): # iterating over the line and each bit to replace message
            if bit == ' ':
                print(" ", end='')
            else:
                print(prompt[i % len(prompt)], end='') # entering char from the prompt replacing bits.
        print() 

if __name__ == "__main__":
    main() 