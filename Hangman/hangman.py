from hangman_art import logo , stages
from hangman_words import wordlist
import random

# get random word from hangman_words
random_word = random.choice(wordlist)
word_len = len(random_word)

print(logo)
print('This is your word.Try to guess it!!')
print('Word : ',end =" ")

guess_word = ['_'] * word_len
print(*guess_word)

chances = 6
end_of_game = False

# game logic
while not end_of_game and chances != 0:

	flag = 0
	letter = input('\n\nGuess a letter: ').lower()

	if (letter.isdigit() or len(letter) != 1):
		print('Please enter single letter (Numbers not allowed)')
		continue

	if letter in guess_word:
		print(f"You've already guessed {letter}")

	for i in range(word_len):
		if random_word[i] == letter:
			guess_word[i] = letter
			flag = 1

	if '_' not in guess_word:
		end_of_game = True
		print('\nCongo!! You won. :)')
		break

	if flag == 0:
		print(f"You guessed {letter}, that's not in the word. You lose a life")
		chances -= 1
	
	print('Guessed Word : ',end =" ")	
	print(*guess_word)
	print(stages[6-chances])
		
else:
	print('\nYou lost :(\nCorrect word:',random_word)




