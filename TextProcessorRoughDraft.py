##Student Name: Joshua Pascascio
## ID: 52192782
import os
import re
import operator
##Rough Draft Version 1
##Basic built-in libraries to import to make error handling and string analyzing and parsing more efficient

strip_Chars = "!.@#$%^&*()_-+=[]{}|\/>,<\""
## Characters to strip off the beginning and ends of words, only filters off characters at the ends,
## not the middle of the words. So words like email addresses or IPs wont be split up.


## Set function psuedocode
## var matched_set = set(fileNameTextProcessor1.countObj.keys()) & set(fileNameTextProcessor2.countObj.keys())
## commonDict = {}
## for item in matched_set:
##      if fileNameTextProcessor1.countObj[item] > fileNameTextProcessor2.countObj[item]:
##          commonDict[item] = fileNameTextProcessor2.countObj[item]
##      else:
##          commonDict[item] = fileNameTextProcessor1.countObj[item]
## commonTotal = 0
## for pair in commonDict:
##      commonTotal += commonDict[pair]
## return matched_set, commonTotals

class TextProcessor:
    def __init__(self,fileName): ##TextProcessor classes must be initialized with a fileName string to try to initialize and open
        self.fileName = fileName ##fileName String
        self.countObj = {} ##Word frequency dictionary each filtered lower case word will be a key and its frequency in the text document will be the value
        self.words = [] ## Stripped list of all the words in the filtered, the list is created through .split() method with \s as the delimiter to split
        ## on spaces, tabs, and newlines
        self.filePassage = "" ##The whole text passage of the file
        self.getText() ## Open and read the file and handle any errors if necessary
    def getText(self):
        try:
            baseFile = open(self.fileName,"r") ##Open File in read mode
            self.filePassage = baseFile.read() ##Read file and extract text data to string
            self.words = re.split("\s",self.filePassage) ##Split into iterable list
        except FileNotFoundError: ##Handle OS and FileErrors
            print("There has been a File I/O error\n.The file or pathname you have selected likely does not exist.\nPlease try another filename")
        except PermissionError:
            print("You do not have permission to read this file.\n Try another file or go into you OS and change the file permissions")
        else:
            baseFile.close() ##The file only needs to be open for extracting the text data once finished it should be closed, to prevent unecessary OS Errors
    def parseText(self):  ##Initialize main dictionary object: .countObj attribute from the word list
        for word in self.words: 
            if word.lower().strip(strip_Chars) not in self.countObj: ##Every unique word, after accounting for case and leading and trailing punctuation marks
                ## that is not already in the dictionary should be added to the dictionary or have its frequency incremented 
                self.countObj[word.lower().strip(strip_Chars)] = 1
            else:
                self.countObj[word.lower().strip(strip_Chars)] += 1
    def outputWordCount(self): ##Returns a formatted output of all the words and their frequencies of the TextProcessor's file attribute, must be called after parseText() method
        returnStr = "" ##Base string
        if len(self.countObj) == 0: ##Return notification to call parseText() if dictionary is uninitialized or left empty 
            return "You have not initialized the word count object!!\nPlease call parseText() method to initial with the text of .txt file of your choosing!"
        else: 
            sortedItems = sorted(self.countObj.items(),key=operator.itemgetter(1),reverse=True) ##sorted sor ts lists or iterables, key= determines what function or attribute
            ## to sort by, reverse= determines ascending or descending order
            ##self.countObj.items() makes list of key,value pairs, key=operator.itemgetter(1) means sort by the dictionary's value, the word frequency, not in alphabetical order
            ## reverse=True means sort in descending order
            for pair in sortedItems:
                if pair[0] != "": ##Do not process empty strings
                    returnStr = returnStr + pair[0] + " - " + str(pair[1]) + "\n" ##Notation: word + " - " values + "\n"
            return returnStr
            
def compareFiles(file1,file2): ##Compare Files and see what words they share, must be in text file or unencoded format
        textProcess1 = TextProcessor(file1) ##Make and initialize two TextProcessor objects from the two passed-in filenames
        textProcess2 = TextProcessor(file2) ## TextProcessor initialization involves opening and reading textfiles and handling any errors along the way
        sharedDict = {} ##SharedDict is an object that shows the common words as keys and how many times those words are repeated in BOTH documents as the key's values
        textProcess1.parseText() ##Initialize both textProcess's .countObj's 
        textProcess2.parseText()
        for pair in textProcess1.countObj: ##For every key in the dictionary check if it is in the other's dictionary and by default pass in its frequency
            if pair in textProcess2.countObj: 
                if pair not in sharedDict:
                    sharedDict[pair] = textProcess1.countObj[pair]
        for word in textProcess2.countObj: ## Reverse the process for the same pair if it is in the other dictionary but the frequency is lower, replace the value
            if word in textProcess1.countObj:
                if sharedDict[word] > textProcess2.countObj[word]:
                    sharedDict[word] = textProcess2.countObj[word]
        sharedTotal = 0 ##Running total of all words in common 
        for key in sharedDict: 
            sharedTotal += sharedDict[key] ##Increment by each key's value
        return sharedDict.keys(),sharedTotal ##Return word set, then total

if __name__=="__main__": ##Sample main function... textfiles retrieved from https://textfile.com/adventure
    a = TextProcessor("ftpStory.txt") 
    a.parseText()
    print(a.outputWordCount()) ##Assignment 1 Part 1
    print("Long text files were retrieved through textfiles.com\nThe files used in this module and \
many others can be retrieved from https://textfiles.com/adventure\n")
    print(compareFiles("ftpStory.txt","Asimov.txt")) ##Assignment 1 Part 2
