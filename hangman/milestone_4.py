import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = str(guess).lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)]
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
            self.num_letters -= 1

    
    def ask_for_input(self):
        while(True):
            guess = input('Guess a letter: ')
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
hangman = Hangman(['apple', 'banana', 'strawberry', 'grape', 'melon'])
hangman.ask_for_input()