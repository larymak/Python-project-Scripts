
wordsTallied = {}
with open(input("Please enter file name: "), 'r') as f:
    for line in f:
        words = line.lower().split() #Divides line into words
        for word in words:
            if word not in wordsTallied: #New Word
                if len(word) >= 4: #Adds new word to dictionary if longer than 3 letters
                    wordsTallied[word] = 1
            else: #Repeated word
                wordsTallied[word] += 1 #Updates number of times word appears
    f.closed

maxWord = max(wordsTallied, key=wordsTallied.get) #Gets the most lyric word of song
maxCount = wordsTallied[maxWord] #Gets number of times the lyric appears
print("\n" + "The most popular lyric is: '" + maxWord + "' \nIt appears " + str(maxCount) + " times in the song" ) #Prints most popular lyric and the number of occurences in the song
