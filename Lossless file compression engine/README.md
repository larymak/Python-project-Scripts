# Compression-Engine
Compression Engine uses Huffman Compression Algorithm to compress .txt files using a lossless compression library. 

This program is currently compressing a file that is named "foo.txt" which is a book downloaded from the website "Projet Gutenberg".  

This program compressed the file which was originally 175 KB to 78 KB which is an increase in efficiency by 43%


# Code can be run via Python 3

Link: https://www.python.org/downloads/

Needs bitstring and huffman modules

pip install bitstring

pip install huffman

# The way this program works is :


Firstly, the code open a text file with following method:

myfile = open("foo.txt","r") 

allofthefile = myfile.read() 

myfile.close() 
	
	The above lines simply open a text file for reading and saves all the characters to a variable. Then I declared all the UTF-8 characters to create a look-up table via the following lines:
mycharset = u"\u000A"

mycharset = u"\u000A" # unicode of the new line character needed for resurrection of the file later

mycharset = mycharset + " abcdefghijklmnopqrstuvwxyz"+\

    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+\
    
        "0123456789!#$%&'()\"*+,-./:;<=>?@[\]^_`{|}~"+\
	
            "àæçèéêôëü" # all of the other unicode charecters
	    
First character of my look-up table is new line character then second character is the space character. Other characters taken from the website: http://www.utf8-chartable.de/. Since the contents of the text file contains non-western characters, also other utf-8 characters were added at the end of the look-up table. Then, the variable that contains the number of appearance of each character was declared as the following line:

 countset = [0 for i in range (0,len(mycharset))]
	The length of this set was determined by the length of the characters those are in look-up table. Then, there is a big for nested loop that contains the main algorithm:
	
for i in range (0,len(allofthefile)):

singlechar = allofthefile[i]

for j in range (0,len(mycharset)):

if mycharset[j] == singlechar:

countset[j] = countset[j]+1

break

It simply gets the array variable characters that created by getting the characters from the text file, then it compares the chosen character with the character loop-up table. If there is a match, then increase the corresponding counter value of the character. With this nested loops, now the numbers of appearances of each character was determined. Since the probability is simply the desired outcome divided by total outcome, the length of the text file is needed. This length was calculated by the following lines:

totalcount = 0 

for i in range (0,len(countset)):

 totalcount = totalcount + countset[i] 
 
Since there can be an undesired character inside the text file (like non UTF-8 characters), instead of getting the length of the file, the entire numbers of appearances were summed up.  Then, the array variable that contains the probabilities of each character was declared and calculated with the following lines:

probabilityset = [0 for i in range (0,len(mycharset))] 

for i in range (0,len(countset)):

 probabilityset[i] = countset[i]/totalcount 
 
	Then the dictionary is needed to easily reach characters and their probabilities. The below codes create a Python dictionary to hold characters and their probabilities:
	
	for i in range (0,len(mycharset)):
	
if countset[i] != 0:

mydict[str(mycharset[i])] = probabilityset[i] 

	A third-party Python module helps to create Huffman codebook. The below code uses this module to create binary sequences for Huffman coding:
	
mycodebook = huffman.codebook(mydict.items())

To observe the output, the calculated probabilities must be print out to the command line with the following code:

for i in range (0,len(mycharset)):

if countset[i]!= 0:

print(mycharset[i] ," has " ,'{0:04d}'.format(countset[i]) ," times appeared."+\

"Probability = " ,'{:.10f}'.format(probabilityset[i]) + " Huffman: " + mycodebook[str(mycharset[i])]) # just a print out operation

	Now we have the characters, their probabilities and corresponding Huffman codes. To compress the file, each character must be encoded as their Huffman codes to create bit array via the following code lines:
	
for i in range (0,len(allofthefile)):

onesandzeros = onesandzeros + mycodebook[str(allofthefile[i])] 

To create the compressed file, open a non-existing file with writing byte permissions. The below code gets 8 bits from the above bit array and creates a character with it and writes it to the compressed file. This operation must be done at the end of the bit sequence to prevent information loss:

	binary_file = open('compressed_foo.bin','wb') 
	
i = 0

while (i < len(onesandzeros)):

b = BitArray(bin=onesandzeros[i:i+8]) 

b.tofile(binary_file) 

i = i+8

binary_file.close()

	From this moment, we have the compressed file of the text file. To decompress the binary file to original file, it is necessary to open the binary file one last time, but as a reading byte permissions:
	
	binary_file = open('compressed_foo.bin',"rb") 
	
allofthebinaryfile = binary_file.read() 

binary_file.close()

Above codes get the binary file as a string of bytes. It is necessary to divide this byte array into bit array via the following code:

newonesandzeros = "" 

for i in range (0,len(allofthebinaryfile)):

newonesandzeros = newonesandzeros + str(bin(allofthebinaryfile[i])[2:].zfill(8)) 

	Now the array of bits must be investigated bits by bits to find a match from the Huffman codebook. In a row, get the first Huffman code. Check the first number of bits that matches the length of the Huffman code, if it matches, increment the counter by Huffman code's length, if it is not, check the next Huffman code and so on:
	
mynewfile = "" 

i=0

while (i < len(newonesandzeros)):

for j in range (0,len(list(mycodebook.values()))):

check = list(mycodebook.values())[j]

if (newonesandzeros[i:i+len(check)] == check): 

mynewfile = mynewfile + list(mycodebook.keys())[j] 

i = i + len(check)

break  

	Now it is good to go save the char string to save to a new file:
	
mynewfile = mynewfile[:-1] 

newfile = open("foonew.txt" ,"w" )

newfile.write(mynewfile) 

newfile.close() 

Code and the example output of the console are attached at the end of the report. foo.txt is 175KB of text file. The compressed file that is created with my algorithm holds 78KB of hard drive space. And the decompressed file holds again 175KB of space and it is a text file without any corruption. 

