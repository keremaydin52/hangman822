from milestone_2 import random_fruit_picker
 
def guess_letter_2():
    while(True):
        guess = input('Guess a letter: ')
        word = random_fruit_picker()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            break
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while(True):
        guess = input('Guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()