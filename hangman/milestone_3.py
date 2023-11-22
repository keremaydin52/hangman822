import random

def random_fruit_picker():
    word_list = ['Apple', 'Banana', 'Strawberry', 'Grape', 'Melon']
    word = random.choice(word_list)
    return word

def check_guess(guess, word):
    letter = str(guess).lower()
    if guess in word:
        print(f"Good guess! {letter} is in the word.")
    else:
        print(f"Sorry, {letter} is not in the word. Try again.")

def ask_for_input():
    while(True):
        guess = input('Guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

my_word = random_fruit_picker()
my_guess = ask_for_input()
check_guess(my_guess, my_word)