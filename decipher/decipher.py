Symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def decipher(text):
    text = text.upper() 
    for key in range(1, 27): 
        decrypted = []
        for i in text:
            if i == " ":
                decrypted.append(" ")
            elif i in Symbols:
                position = Symbols.index(i)
                new_position = (position + key) % 26  # wrap around
                decrypted.append(Symbols[new_position])
            else:
                decrypted.append(i)

        print(f"Key #{key}: {''.join(decrypted)}")  # each key 

def main():
    try:
        while True:
            text = input("Enter the encrypted caesar cipher to crack\n>>> ")
            decipher(text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
