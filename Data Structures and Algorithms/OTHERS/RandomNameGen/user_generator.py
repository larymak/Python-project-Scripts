import requests
import random

url = 'https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co'

names = requests.get(url).text

# We are splitting the words to clear out the empty spaces and create iterable
individual_words = names.split()

# to get random word
print(random.choice(individual_words))
