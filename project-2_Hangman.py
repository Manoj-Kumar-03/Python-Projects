import  random
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
=========''']

word_list = ["python", "computer", "keyboard", "monitor", "program", "network", "internet", "science", "diamond", "elephant", "giraffe", "mountain", "adventure", "treasure", "airplane", "hospital", "umbrella", "sandwich", "chocolate", "pineapple", "backpack", "football", "calendar", "notebook", "rainbow"]

lives = 6

print(logo)
random_word = random.choice(word_list).lower()
placeholder = ''
word_len = len(random_word)
for _ in range(word_len):
    placeholder += '_'

print(random_word)
print("Word to guess : ", placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"You have {lives}/6 lives left")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ''
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print("Word to guess: " + display)

    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in word.you lose a life")
        if lives == 0:
            game_over = True
            print(f'You Lose!, the chosen word is {random_word}')

    if '_' not in display:
        game_over = True
        print('You Won!!')

    print(stages[lives])

