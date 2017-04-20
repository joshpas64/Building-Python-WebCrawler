import os
import time
import sys
import re
import operator
## CS121 Assignment 1 Part 2
## Student Name: Joshua Pascascio
## Student ID: 52192782
STRIP = "`~!.@#$%^&*?:()_-+=[]{}|\\/>,<\"\'"

class SharedText:
    def __init__(self,wordDict,wordCount,fileName1,fileName2):
        self.commonWords = wordDict
        self.commonCount = wordCount
        self.wordList = list(wordDict.keys())
        self.fileName1 = fileName1
        self.fileName2 = fileName2
        print("Preparing to format shared words from " + self.fileName1 + " and " + self.fileName2)
    def getFileName1(self):
        return self.fileName1
    def getFileName2(self):
        return self.fileName2
    def formattedWords(self,sharedWords):
        sharedWords.sort()
        counter = 1
        for word in sharedWords:
            print("Common word " + str(counter) + ": " + word)
            counter += 1
    def formatPairs(self,pairsDict):
        pairsList = sorted(pairsDict.items(), key = lambda item: (-1 * item[1],item[0]))
        for pair in pairsList:
            if pair[0] != "":
                print(pair[0] + " - " + str(pair[1]))
    def truncatedOutput(self):
        display_Str = "The number of words in common between " + self.fileName1 + " and " + self.fileName2 + " is:  " + str(self.commonCount)
        print(display_Str)
        prompt1 = input("Would you like to see all the words held in common?\n [Yes to display; Any other input to continue]\n")
        if(prompt1.lower().strip() == "yes"):
            self.formattedWords(self.wordList)
        else:
            print("Skipping this portion of output")
        prompt2 = input("Would you like to see the words held in common by frequency as well?\n [Yes to display; Any other input to continue]\n")
        if(prompt2.lower().strip() == "yes"):
            self.formatPairs(self.commonWords)
        else:
            print("Skipping word-frequency portion of output")
        print("Done displaying data between " + self.fileName1 + " and " + self.fileName2)

        
class FileComparator:
    def __init__(self,fileName1,fileName2):
        self.file1 = fileName1
        self.file2 = fileName2
        self.frequency1 = {}
        self.frequency2 = {}
        self.commonFrequency = {}
        self.words1 = []
        self.words2 = []
        self.loadText()
    def setFile1(self,file):
        self.file1 = file
    def setFile2(self,file):
        self.file2 = file
    def getFirstFrequency(self):
        return self.frequency1
    def getSecondFrequency(self):
        return self.frequency2
    def resetFiles(self,file1,file2):
        if file1.closed == False:
            file1.close()
        if file2.closed == False:
            file2.close()
    def loadText(self):
        try:
            baseFile1 = open(self.file1,"r")
            baseFile2 = open(self.file2, "r")
            file1Lines = baseFile1.readlines()
            file2Lines = baseFile2.readlines()
            file1Length = len(file1Lines)
            file2Length = len(file2Lines)
            upperBound = file2Length
            if file1Length > upperBound:
                upperBound = file1Length
            for i in range(upperBound):
                if i >= file1Length:
                    if baseFile1.closed == False:
                        baseFile1.close()
                else:
                    self.parseLine(re.split("\s",file1Lines[i]),self.frequency1)
                if i >= file2Length:
                    if baseFile2.closed == False:
                        baseFile2.close()
                else:
                    self.parseLine(re.split("\s",file2Lines[i]),self.frequency2)
            self.resetFiles(baseFile1,baseFile2)
        except FileNotFoundError: ##Handle OS and FileErrors
            print("There has been a File I/O error\n.The file or pathname you have selected likely does not exist.\nPlease try another filename")
            self.resetFiles(baseFile1,baseFile2)
        except PermissionError:
            print("You do not have permission to read this file.\n Try another file or go into you OS and change the file permissions")
            self.resetFiles(baseFile1,baseFile2)
        except UnicodeDecodeError:
            print("There are characters or data in this file that does not match the ASCII or UTF-8 characters this program handles.")
            baseFile1.close()
            baseFile2.close()
    def parseLine(self,lineArr,dictToPut):
        for word in lineArr:
            if word.lower().strip(STRIP) not in dictToPut:
                dictToPut[word.lower().strip(STRIP)] = 1
            else:
                dictToPut[word.lower().strip(STRIP)] += 1
    def mergeFormattedFiles(self):
        if len(self.frequency1) == 0 or len(self.frequency2) == 0:
            print("Files are either empty or not initialized properly please try again!")
            empty = SharedText({},0,"ERROR","ERROR")
            return empty
        else:
            print("Beginning Dual-File Analysis on File: " + self.file1 + " and File: " + self.file2)
            matched_set = set(self.frequency1.keys()) & set(self.frequency2.keys())
            commonTotal = 0
            for item in matched_set:
                if self.frequency1[item] > self.frequency2[item]:
                    self.commonFrequency[item] = self.frequency2[item]
                else:
                    self.commonFrequency[item] = self.frequency1[item]
                commonTotal += self.commonFrequency[item]
            sharedText = SharedText(self.commonFrequency,commonTotal,self.file1,self.file2)
            return sharedText

def processedOutput(frequencies):
    returnStr = ""
    if len(frequencies) == 0:  
        return "You have not initialized your word count object!!\nPlease initialize your FileComparator Object with readable non-empty files!"
    else: 
        sortedItems = sorted(frequencies.items(),key = lambda item: (-1 * item[1],item[0])) ##sorted sor ts lists or iterables, key= determines what function or attribute
        ## to sort by, reverse= determines ascending or descending order
        ##self.countObj.items() makes list of key,value pairs, key=operator.itemgetter(1) means sort by the dictionary's value, the word frequency, not in alphabetical order
        ## reverse=True means sort in descending order
        for pair in sortedItems:
            if pair[0] != "": ##Do not process empty strings
                returnStr = returnStr + pair[0] + " - " + str(pair[1]) + "\n" ##Notation: word + " - " values + "\n"
        return returnStr


if __name__=="__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    print("CS121 Assignment 1 Part 2")
    f = FileComparator(file1,file2)    
    sharedResult = f.mergeFormattedFiles()
    if sharedResult.getFileName1 == "ERROR" or sharedResult.getFileName2 == "ERROR":
        print("Unable to retrieve successful analysis")
    else:
        sharedResult.truncatedOutput()
