import string
import re

fhand = open('novel.txt',  encoding="utf8")
lineCount = 0
uniqueWordList = []
for line in fhand :
    line = line.rstrip().lower()
    lineCount += 1
   # print(line)
    lineNoPunct = re.sub(r'[^\w\s]', '', line)
    words = lineNoPunct.split()
    #print(words)
    for word in words:
        #word.translate(None, string.punctuation)   #doesnt work
       # wordNoPunct = re.sub(r'[^\w\s]', '', word) #trying it earlier
        if word not in uniqueWordList:
            #check for punctuation
            uniqueWordList.append(word)
            print(word + ' has been added to the word list.')
print('Line Count:', lineCount)
print(('How many unique words you used: ' + str(len(uniqueWordList))))