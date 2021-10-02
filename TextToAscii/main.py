import pyfiglet

text = str(input("Text to Convert?: "))

output = pyfiglet.figlet_format(text)
print(output)
