import string #String module will import all the nessary ascii character
import random #random module help us to import functions needed to generate random element.

passwrd = string.ascii_letters+string.digits+string.punctuation #This will generate a string consist of all ascii character.

numPass = int(input("How many passwords do you need to be generated? "))
length = int(input("Enter the length of the password(s): "))

print("List(s) of Generated passwords: ")

for _ in range(numPass):
    print(''.join(random.sample(passwrd, k=length))) #sample() generates an array of random characters of length k
