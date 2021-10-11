from data import morse_code

class MorseCode:
    def __init__(self):
        self.in_morse = ""
        self.in_english = ""
    
    def to_morse(self, sentence):
        '''
        Takes one required parameter sentence of type string and
        converts it into the equivalent morse code.
        '''
        self.in_morse = ""
        sentence = sentence.split(" ")
        # print(sentence)

        morse_translation = []
        for word in sentence:
            # Converting each word to a list of characters
            word_ = list(word)

            # Matching every character with morse code in data.py
            for letter in word_:
                morse_translation.append(morse_code[letter.lower()])

            # Adding a forwars slash at end of each word except the last word
            if sentence.index(word) != len(sentence)-1:
                morse_translation.append("/")

        # Joining the final list to make a string of morse code characters
        self.in_morse = " ".join(morse_translation)

        return self.in_morse

    def to_english(self, code_in_morse):
        '''
        Converts morse code to english takes one required parameter
        code_in_morse as a string
        '''
        self.in_english = ""
        # Checking if the entered code has "/" as seperator or not?
        if "/" in code_in_morse:
            code_list = code_in_morse.split(" / ")
        else:
            code_list = code_in_morse.split(" ")

        # Creating a list for morse code to convert it later to english
        morse_list = []
        for code in code_list:
            code = code.split(" ")
            morse_list.append(code)
        
        # Looping through the dictionary of morse code and replacing morse to letter
        for word in morse_list:
            for letter in word:
                for key, value in morse_code.items():
                    if letter == value:
                        self.in_english += key
            
            # After each word concatinating the white space
            self.in_english += " "
        
        return self.in_english