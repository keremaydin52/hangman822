import random

def random_fruit_picker():
    word_list = ['Apple', 'Banana', 'Strawberry', 'Grape', 'Melon']
    print(word_list)

    word = random.choice(word_list)
    print(word)

def guess_letter():
    guess = input('Enter a single letter: ')

    if len(guess) == 1 and guess.isalpha():
        print("Good guess")
    else:
        print("Oops! That is not a valid input.")

random_fruit_picker()
guess_letter()