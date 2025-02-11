import sys

Symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encrypted(text, key):
    encrypt = []  
    for i in text:
        if i == " ":
            encrypt.append(" ")  
        elif i in Symbols:
            position = Symbols.index(i) # catches the positiion of the text 
            position = position - key  
            encrypt.append(Symbols[position])
        else:
            encrypt.append(i)  
    return "".join(encrypt)

def decrypted(text, key):
    decrypt = []  
    for i in text:
        if i == " ":
            decrypt.append(" ")  
        elif i in Symbols:
            position = Symbols.index(i)
            position = position + key  
            decrypt.append(Symbols[position])
        else:
            decrypt.append(i)
    return "".join(decrypt)

def main():
    try:
        while True:
            
            text = input("Enter a text. Enter X to exit\n>>> ").upper() # prompt
            if text == "X":
                sys.exit(".")
            key = int(input("Enter a key\n>>> "))
            response = input("Press (E) to encrypt or (D) to decrypt\n>>> ").lower()

            if response == 'e':
                print("Encrypted text:", encrypted(text, key))
            elif response == 'd':
                print("Decrypted text:", decrypted(text, key))
            else:
                print("please enter 'E' or 'D'.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
