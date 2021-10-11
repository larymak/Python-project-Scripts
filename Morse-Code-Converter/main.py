from morse import MorseCode

# Creating a traslate object using MorseCode class
translate = MorseCode()

# Converting English to morse (encode)
text = input("enter a message to convert to morse code: ")
morse_code = translate.to_morse(text)
print(morse_code)

#Converting Morse to english (decode)
text = input("enter morse code to convert to actual message: ")
english_text = translate.to_english(text)
print(english_text)