def LevelOneRules():
    return """🔹 Level 1 Rules:
- The computer will choose a random **1-digit number** (0-9).
- You have **10 tries** to guess the number.
- No hints will be given. Just guess until you get it right!
"""

def LevelTwoRules():
    return """🔹 Level 2 Rules:
- The computer will choose a random **2-digit number** (10-99).
- You have **10 tries** to guess the number.
- Clues:
  - **Pico**: A correct digit is in the wrong position.
  - **Fermi**: A correct digit is in the right position.
  - **Bagels**: No digits are correct.
"""

def LevelThreeRules():
    return """🔹 Level 3 Rules:
- The computer will choose a random **3-digit number** (100-999).
- You have **10 tries** to guess the number.
- Clues:
  - **Pico**: A correct digit is in the wrong position.
  - **Fermi**: A correct digit is in the right position.
  - **Bagels**: No digits are correct.
- This level is harder because numbers are longer!
"""

if __name__ == "__main__":
    print(LevelOneRules())
    print(LevelTwoRules())
    print(LevelThreeRules())
