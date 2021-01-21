import requests
from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co'

r = requests.get(url)
text = r.text
# print(text)

# We are splitting the words to clear out the empty spaces
individual_word = text.split()
# print(individual_word)

# Next we need it to extract a random name we will use random library
random_number = randint(0, len(individual_word))

# print(individual_word[random_number])

#to get random word with number
print(individual_word[random_number] + str(random_number))