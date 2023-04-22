import random

class Hangman:
    def __init__(self, category, difficulty):
        self.category = category
        self.difficulty = difficulty
        self.word = None
        self.word_list = None
        self.hint_words = None
        self.hint_indices = None
        self.num_of_hint_words = None
        self.guess_display = None
        self.user_guess = None
        self.game_active = None
        self.attempts = None
        self.restart = None

    def assign_words_for_category(self): # you can add more categories here.
        if self.category == "fruit":
            self.word_list = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple",
                              "kiwi", "pear", "peach", "plum", "watermelon", "melon", "cherry", "blueberry", "raspberry"]
        elif self.category == "vegetable":
            self.word_list = ['carrot', 'potato', 'broccoli', 'cauliflower', 'cucumber', 'lettuce', 'kale',
                                  'cabbage', 'onion', 'garlic', 'tomato', 'eggplant', 'beetroot', 'radish', 'asparagus', 'beans', 'peas']
        elif self.category == "animal":
            self.word_list = ["dog", "cat", "lion", "tiger", "elephant", "giraffe", "monkey", "kangaroo", "penguin",
                               "whale", "dolphin", "shark", "alligator", "crocodile", "snake", "spider", "bee", "ant", "bird", "fish"]

    def randomize_words(self):
        self.word = random.choice(self.word_list)

    def create_hint(self): # this creates hint letters as indices.
        self.hint_indices = random.sample(range(len(self.word)), self.num_of_hint_words)

    def set_difficulty(self): # here you can configure different difficulties
        if self.difficulty == "easy":
            self.num_of_hint_words = round(len(self.word)*0.4)  # amounts of hints equals to 40% of length 
            self.attempts = 10
        elif self.difficulty == "normal":
            self.num_of_hint_words = round(len(self.word)*0.3)  # amounts of hints equals to 30% of length
            self.attempts = 7
        elif self.difficulty == "hard":
            self.num_of_hint_words = round(len(self.word)*0.2)  # amounts of hints equals to 20% of length
            self.attempts = 5
            
    def start_the_game(self):
        self.assign_words_for_category()
        self.randomize_words()
        self.set_difficulty()
        self.create_hint()
        self.place_chars()
        self.input_guess()
        self.ask_if_restart()

    def welcome_message(self):
        print("Welcome to Hangman!")
        print("Here you can try guessing letters of a randomly generated words based on hints!")
        print(f"Category: {self.category}")
        print("Good luck!")

    def place_chars(self):
        self.guess_display = ["_" for char in self.word]
        for i in self.hint_indices:
            self.guess_display[i] = self.word[i] 
        print("--------------------------------------")
        print(" ".join(self.guess_display))

    def input_guess(self):
        self.game_active = True
        while self.game_active and self.attempts > 0:
            self.user_guess = input("Guess a letter: ")

            if self.user_guess in self.word:
                self.guess_display = [self.user_guess if list(self.word)[i] == self.user_guess else char for i, char in enumerate(self.guess_display)]
                print("--------------------------------------")
                print(" ".join(self.guess_display))

            else:
                print("wrong!")
                self.attempts -= 1
                print(f"{self.attempts} attempt(s) remaining")
            
            if "_" not in self.guess_display:
                print("You won!")
                break
            
            if self.attempts == 0:
                print("You ran out of attempts!")
                break
        
    def ask_if_restart(self):
        self.restart = input("Do you want to play more? [Y/N]: ")
        if self.restart == "Y" or self.restart == "y":
            self.start_the_game()
        elif self.restart == "N" or self.restart == "n":
            quit()

# This is where you create an instance
try:
    my_hangman = Hangman("fruit", "hard") # (Category, Difficulty) Categories: fruit, vegetable, animal. Difficulties: easy, normal, hard.
    my_hangman.welcome_message()
    my_hangman.start_the_game()

except:        
    print("Please make sure the initialization arguments are strings.")              