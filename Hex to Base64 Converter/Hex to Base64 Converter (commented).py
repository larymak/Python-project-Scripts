#49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
########https://base64.guru/converter/encode/hex;
hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
hexdecalph = '0123456789abcdef'
finalascii = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""
fname = 'NEWtestoutput.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#
#
#
#below starts the function
def hextodec(hexstring) :
    #initialize empty list to contain hex pairs
    hexlist = []
    #turn the input string into a list
    hexinput = list(hexstring)
    #loop through the list of characters and pair them up
    while len(hexinput) > 0 :
        #take first two characters, turn them into a string, assign them to a variable
        hexpair = ''.join(hexinput[:2])
        fhand.write(f'Parsed hex pair {hexpair}\n')
        #add the hex pair to the list
        hexlist.append(hexpair)
        #remove the first two characters from the original input string list
        hexinput = hexinput[2:]
    fhand.write(f'List of parsed hex pairs is {hexlist}\n')
    declist = []
    #going through each pair, organizing, and converting to decimal
    for pair in hexlist :
        #turn the pair into a list and change to lowercase to match hex character list above
        hextodecinput = list(pair.lower())
        fhand.write(f'Lowercase pair list is {hextodecinput}\n')
        #reverse the list to process from lowest priority to highest
        hextodecinput.reverse()
        fhand.write(f'Reversed list is {hextodecinput}\n')
        total = 0
        #loop through each character and convert from hexadecimal to decimal
        for char in hextodecinput :
            fhand.write(f'{hexdecalph.index(char)} is index of character in hexdecalph list\n')
            fhand.write(f'{hextodecinput.index(char)} is index of character in input\n')
            fhand.write(f'{16 ** hextodecinput.index(char)} is 16 to the power of the index of the character in the input\n')
            fhand.write(f'---Equation will be {hexdecalph.index(char)} * {16 ** hextodecinput.index(char)}\n')
            #do the actual hexadecimal conversion
            total += ((hexdecalph.index(char)) * (16 ** hextodecinput.index(char)))
            fhand.write(f'---Running total is {total}\n')
        #turn total into a string and append to list
        total = str(total)
        fhand.write(f'{total} is decimal conversion\n')
        declist.append(total)
    fhand.write(f'{declist} is list of decimal conversions\n')
    binlist = []
    #loop through each decimal in the list to convert to final base64 ASCII characters
    for dec in declist :
        #convert to integer
        dec2 = int(dec)
        #convert to binary, padding with leading zeros if necessary for 8 total characters
        decbin = f'{dec2:08b}'
        decbin = list(decbin)
        decbin = ''.join(decbin)
        fhand.write(f'{decbin} is binary conversion of decimal\n')
        binlist.append(decbin)
    binlist = ''.join(binlist)
    #to convert to base64, 6bit words are needed. this ensures the list is divisible by 6
    if not len(binlist) % 6 == 0 :
        binlist = list(binlist)
        binlist.append('00')
        binlist = ''.join(binlist)
    if not len(binlist) % 6 == 0 :
        binlist = list(binlist)
        binlist.append('00')
        binlist = ''.join(binlist)
    sixbitlist = []
    #loop through the list, separating bits out into words of 6
    while len(binlist) > 0 :
        binword = binlist[:6]
        binlist = binlist[6:]
        binword = ''.join(binword)
        fhand.write(f'Parsed 6-bit word {binword}\n')
        sixbitlist.append(binword)
    finaldeclist = []
    #loop through each 6-bit word in list, converting to decimal
    for item in sixbitlist :
        #convert the word to integer in base2
        newdec = int(item, 2)
        newdec = str(newdec)
        fhand.write(f'{newdec} is decimal conversion of 6-bit word {item}\n')
        finaldeclist.append(newdec)
    finalcharlist = []
    #loop through list of decimal conversions, converting to ASCII using the base64 conversion table
    for item in finaldeclist :
        finalchar = int(item)
        finalchar = finalascii[finalchar]
        finalchar = str(finalchar)
        fhand.write(f'{item} is decimal in list to convert using base64 table\n')
        fhand.write(f'{finalchar} is final character in base64 list using decimal conversion of 6-bit binary word as index\n')
        finalcharlist.append(finalchar)
    finalword = ''.join(finalcharlist)
    finalword = list(finalword)
    #base64 strings are divisible by 4, so the following three lines ensure that the string is padded with ending '=' if necessary
    if not len(finalword) % 4 == 0 :
        finalword.append('=')
    if not len(finalword) % 4 == 0 :
        finalword.append('=')
    if not len(finalword) % 4 == 0 :
        finalword.append('=')
    finalword = ''.join(finalword)
    fhand.write(f'{finalword} is base64 conversion of {hexstring}\n')
    return finalword
print(hextodec(input('')))