##Student Name: Joshua Pascascio
## ID: 52192782
import os
import time
import re
import operator
import sys
##Basic built-in libraries to import to make error handling and string analyzing and parsing more efficient

strip_Chars = "`;~!.@#$%^&*?:()_-+=[]{}|\\/>,<\"\'"
## Characters to strip off the beginning and ends of words, only filters off characters at the ends,
## not the middle of the words. So words like email addresses or IPs wont be split up.


class TextProcessor:
    def __init__(self,fileName): ##TextProcessor classes must be initialized with a fileName string to try to initialize and open
        self.fileName = fileName ##fileName String
        self.countObj = {} ##Word frequency dictionary each filtered lower case word will be a key and its frequency in the text document will be the value
        self.getText() ## Open and read the file and handle any errors if necessary
    def getText(self):
        try:
            baseFile = open(self.fileName,"r") ##Open File in read mode
            fileLines = baseFile.readlines()
            for line in fileLines:
                modifiedLine = re.split("\s",line)
                self.parseText(modifiedLine)
            #self.filePassage = baseFile.read() ##Read file and extract text data to string
            #self.words = re.split("\s",self.filePassage) ##Split into iterable list
        except FileNotFoundError: ##Handle OS and FileErrors
            print("There has been a File I/O error\n.The file or pathname you have selected likely does not exist.\nPlease try another filename")
        except PermissionError:
            print("You do not have permission to read this file.\n Try another file or go into you OS and change the file permissions")
        except UnicodeDecodeError:
            print("There are characters or data in this file that does not match the ASCII or UTF-8 characters this program handles.")
            baseFile.close()
        else:
            baseFile.close() ##The file only needs to be open for extracting the text data once finished it should be closed, to prevent unecessary OS Errors
    def parseText(self,lineArr):  ##Initialize main dictionary object: .countObj attribute from the word list
        for word in lineArr: 
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
            sortedItems = sorted(self.countObj.items(),key = lambda item: (-1 * item[1],item[0]) ) ##sorted sor ts lists or iterables, key= determines what function or attribute
            ## to sort by, reverse= determines ascending or descending order
            ##self.countObj.items() makes list of key,value pairs, key = lambda item: (-1 * item[1],item[0]) means sort by the dictionary's value
            ## first, in descending order, and then alphabetically if words have the same frequency
            for pair in sortedItems:
                if pair[0] != "": ##Do not process empty strings
                    returnStr = returnStr + pair[0] + " - " + str(pair[1]) + "\n" ##Notation: word + " - " values + "\n"
            return returnStr

def loadSysCall():
    try:
        print("CS121 Assignment 1 Part 1")
        part1String = sys.argv[1]
        a = TextProcessor(part1String) 
        print(a.outputWordCount()) ##Assignment 1 Part 1
    except IndexError:
        print("I am sorry there may be missing or too many files loaded in your command-line system call!\nPlease try again with just one file")
    except KeyboardInterrupt:
        print("There was an I/O Interrupt error.\nTry letting the file fully process before typing or hitting Ctrl-Z or Ctrl-C")
    except:
        print("An error has occurred.\nPlease try reloading the program")
    finally:
        print("Long text files were retrieved through textfiles.com\nThe files used in this module and \
many others can be retrieved from https://textfiles.com/adventure\n")
    
if __name__=="__main__": ##Sample main function... textfiles retrieved from https://textfile.com/adventure
    loadSysCall()


