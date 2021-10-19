import huffman
import bitstring
from bitstring import BitArray

myfile = open("foo.txt","r") 
allofthefile = myfile.read() 
myfile.close() 

mycharset = u"\u000A" 
mycharset = mycharset + " abcdefghijklmnopqrstuvwxyz"+\
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+\
        "0123456789!#$%&'()\"*+,-./:;<=>?@[\]^_`{|}~"+\
            "àæçèéêôëü" 
countset = [0 for i in range (0,len(mycharset))] 

for i in range (0,len(allofthefile)):
    singlechar = allofthefile[i]
    for j in range (0,len(mycharset)):
        if mycharset[j] == singlechar:
            countset[j] = countset[j]+1 # count the apperance of the charecters
            break

totalcount = 0
for i in range (0,len(countset)):
    totalcount = totalcount + countset[i] # count how many charecters text contains

probabilityset = [0 for i in range (0,len(mycharset))] 

for i in range (0,len(countset)):
    probabilityset[i] = countset[i]/totalcount # calculate appearance probability of the charecters

mydict = {} 

for i in range (0, len(mycharset)):
    if countset[i] != 0: # precaution to dont create a Huffman code for zero elements
        mydict[str(mycharset[i])] = probabilityset[i] 
mycodebook = huffman.codebook(mydict.items()) 


for i in range (0,len(mycharset)):
    if countset[i] != 0: # suppress the zero appearance charecters
        print(mycharset[i] , " has " , '{0:04d}'.format(countset[i]) , " times appeared. "+\
              "Probability = " , '{:.10f}'.format(probabilityset[i]) + " Huffman: " + mycodebook[str(mycharset[i])]) # just a print out operation

onesandzeros = "" 
for i in range (0, len(allofthefile)):
    onesandzeros = onesandzeros + mycodebook[str(allofthefile[i])] 

binary_file = open('compressed_foo.bin', 'wb') 

i = 0
while (i < len(onesandzeros)):
    b = BitArray(bin=onesandzeros[i:i+8]) # divide array with 8 many bits and make them into a byte
    b.tofile(binary_file) 
    i = i+8

binary_file.close()

binary_file = open('compressed_foo.bin', "rb") 
allofthebinaryfile = binary_file.read() 
binary_file.close()

newonesandzeros = "" 

for i in range (0, len(allofthebinaryfile)):
    newonesandzeros = newonesandzeros + str(bin(allofthebinaryfile[i])[2:].zfill(8)) # tranform bytes into bit array

mynewfile = "" 
i=0
while (i < len(newonesandzeros)):
    for j in range (0, len(list(mycodebook.values()))):
        check = list(mycodebook.values())[j]
        if (newonesandzeros[i:i+len(check)] == check): # check the Binary Huffman sequence in the bit array
            mynewfile = mynewfile + list(mycodebook.keys())[j] # if the sequence is found, transform it into the character and add it to the character array
            i = i + len(check)
            break

mynewfile = mynewfile[:-1] 

newfile = open("foonew.txt","w") 
newfile.write(mynewfile) 
newfile.close() 

