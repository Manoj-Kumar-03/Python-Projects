import random

logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

stages = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

word_list = [
    "python", "computer", "keyboard", "monitor", "program",
    "network", "internet", "science", "diamond", "elephant",
    "giraffe", "mountain", "adventure", "treasure", "airplane",
    "hospital", "umbrella", "sandwich", "chocolate", "pineapple",
    "backpack", "football", "calendar", "notebook", "rainbow"
]

lives = 6

print(logo)

random_word = random.choice(word_list)

correct_letters = []
guessed_letters = []

game_over = False

while not game_over:

    print("\n" + "=" * 40)
    print(f"Lives Remaining: {lives}/6")
    print(stages[lives])

    display = ""
    for letter in random_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word:", " ".join(display))

    if guessed_letters:
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))

    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in random_word:
        correct_letters.append(guess)
        print(f"Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    # Win condition
    if all(letter in correct_letters for letter in random_word):
        print("\n Congratulations! You guessed the word:", random_word)
        game_over = True

    # Lose condition
    elif lives == 0:
        print(stages[lives])
        print(f"\n💀 Game Over! The word was '{random_word}'.")
        game_over = True
