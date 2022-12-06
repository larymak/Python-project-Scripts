import json
from difflib import SequenceMatcher
from difflib import get_close_matches

# accessing the data.json file
data = json.load(open("076 data.json"))

# function to check if entered word is present in the 076_data.json file and print neccessary output
def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]    
    elif len(get_close_matches(w,data.keys())) > 0:
        answer = input("Did you mean %s instead? enter Y if yes or N if no:"%get_close_matches(w,data.keys())[0])
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            return data[get_close_matches(w,data.keys())[0]]
        elif answer == "n" or answer == "no":
            return "TRY ANOTHER WORD:"
        else:
            return "We didn't Understand what you wanted Type y for yes and n for no: "
    else:
        print ("THE WORD DOESNT EXIST in the data.json database!!!!! ")

word = input("Enter a word:")

word = word.lower()

print(translate(word))
output = translate(word)
#can comment this below not so neccessary.....
if type(output) == list:

    for item in output:
        print(item)
else:
    print (output)
