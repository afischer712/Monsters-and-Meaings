"""
Created on Tue Feb 15 12:22:20 2022

@author: Adam Fischer

Monsters & Meanings, a Semantic Analysis Companion to TTRPGs
   
Spring 2022
CS 451 - Capstone Project 

"""


import spacy # semantic analysius
import selenium # web scraping
from time import sleep # helps w/ web scraping
import pickle# serialization
import pandas as pd # used with spacy
import os # helpful for a lot, like deleting a file



# this object is a representation of the important parts of a description
class Description:
    
    # constructor
    def __init__(self, Name, monster, monstertype, descriptxt):
        self.nounList = []
        self.verbList = []
        self.adjList = []
        self.Name = Name
        self.monster = monster
        self.monstertype = monstertype
        self.descriptxt = descriptxt
        self.PartsOfSpeech()
        
        
    #automatically generates the lists for parts of speech, called by constructor
    def PartsOfSpeech(self):
        
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.descriptxt)

        for t in doc:# sorts words into lists by part of speech
            
            if(t.pos_ == 'NOUN'):
                self.nounList.append(t.lemma_)
            elif(t.pos_ == 'VERB'):
                self.verbList.append(t.lemma_)
            elif(t.pos_ == ("ADJ" or "ADV") ):
                self.adjList.append(t.lemma_)
        
        
    # to string mostly to test stuff
    def tostring(self):
        outputString = self.Name + "\n" + self.monstertype + "\n"
        
        for x in self.nounList:
            outputString += x + " "
        outputString+="\n"
        for x in self.verbList:
            outputString += x + " "
        outputString+="\n"
        for x in self.adjList:
            outputString +=x + " "
        outputString+="\n" + self.descriptxt
        
        return outputString



# this object is just to facilitate comparisons between description objects
class SimScorer:
    
    # constructor
    def __init__(self, desc1, desc2):
        self.desc1 = desc1
        self.desc2 = desc2
    
    #this function will actually provide the similarity score btwn two descriptions
    def Score(desc1, desc2):
        
        # this is where the vector stuff needs to occur with semantic analysis
        score = 0
        print(desc1.name + " has a similarity score of " + score + " with " + desc2.name)
        return score
    
    
    
class ToDescrip:
    
    #constructor
    def __init__(self, filename):
        self.filename = filename
      
    # This method is for turning strings into a Description and writing it to a txt file
    def StringDescrip(self, name, monstertype, descriptxt):
        stringdescrip = Description(name, True, monstertype, descriptxt)
        
        # NEEDS TO WRITE NEW FILE TOO AND ADD TO MONSTERLIST
        
    #creates description object from contents of file
    def TxtDescrip(self):
        
        
        file = open(self.filename, 'r')
        
        name = file.readline()
        monstertype = file.readline()
        
"""        # loops for the lists
            nouns = []
            verbs = []
            adjs = []
        
            nounstring = file.readline()
            s = ""
            for x in nounstring: 
                if x != ' ':
                    s+=x
                else:
                    nouns.append(s)
                    s = ""
                nouns.append(s)
                
            verbstring = file.readline()
            s = ""
            for x in verbstring:
                if x != ' ':
                    s+=x
                else:
                    verbs.append(s)
                    s = ""
            verbs.append(s)
                
            adjstring = file.readline()
            s = ""
            for x in adjstring:
                if x != ' ':
                    s+=x
                else:
                    adjs.append(s)
                    s = ""
            adjs.append(s)
        
        
            description = file.readline()
            
            descrip = Description(nouns, verbs, adjs, name, True, monstertype, description)
        
            return descrip.tostring()
        
        elif inputtype == "string":
            
            x = 1# what did i even want this method to do
        
"""








# THIS IS WHERE STUFF BEGINS
print('WELCOME TO MONSTERS & MEANINGS, YOUR TTRPG CREATION COMPANION')
print('-------------------------------------------------------------')
print('A - Test our Monster Collection for description similarity!')
print('B - Add a Monster Description to our collection!')
print('B+ - View all Monster Descriptions!')# really need to reorder and simplify
print('C - Information on how Monsters & Meanings works!')
print('D - Search a piece of literature for a monster description!')
print('-------------------------------------------------------------')

userchoice = input()
switchstate = userchoice.capitalize()

if(switchstate == 'A'):
    
    namefile = open("MonsterList.txt", 'r')
    names = [] = namefile.readlines()
    
    for x in names:
        print(x)
        
    print('daf')
    
elif(switchstate == 'B'):
    
    print('-------------------------------------------------------------')
    print('Awesome! Now enter the description of the monster!')
    print('A - Enter a .txt file')
    print('B - Type the description into the console')
    print('C - Build the collection from DNDBeyond (DO NOT PRESS)')
    
    input2 = input()
    print('-------------------------------------------------------------')
    
    if(input2 == 'B'):
        
        
        
        # NOTE: THIS WOULD ALSO REQUIRE A FULL INPUT OF DND STUFF
        #        im just using this to test for now
        #       no longer just using to test, It's fine w/ monster type alone
        print('Enter the name of the monster!')
        monstername = input()
        print('-------------------------------------------------------------')
        print('Enter the type of the monster in D&D!')
        monstertype = input()
        print('-------------------------------------------------------------')
        ismonster = True
        
        print('Go ahead and enter the description now!')
        
        userDescrip = input()
       
        
       
                
        descrip = Description(monstername, ismonster,monstertype, userDescrip)
        
        print('-------------------------------------------------------------')
        print(descrip.tostring())
        print('-------------------------------------------------------------')
        
        
        
        filename = descrip.Name + '.txt'
        file1 = open(filename, 'w')
        file1.write(descrip.tostring())
        
        file2 = open("MonsterList.txt", "a")
        file2.write(descrip.Name + "\n")
        # add monster name into a txt file that I can go through to get other descriptions
        
        
        
            
        
    elif(input2 =='A'):
        
        
        print('Make sure that your .txt file is in the following format:')# this is where i take in a txt file
        print('-------------------------------------------------------------\n')
        
        print('Monster Name')
        print('Monster Type (Such as a construct, monstrosity, etc)')
        print('Monster Description\n')
        
        print('-------------------------------------------------------------')
        print('   NOTE: A new .txt file will be created for that monster,')
        print('         under the the name of ____.txt where the blank is')
        print('         the name of your monster.\n')
        
        print('Go ahead and enter the name of the file here:')
        print('-------------------------------------------------------------\n')
        
        txtfilename = input()
        
        print('\n-------------------------------------------------------------')
        
        MakeADescrip = ToDescrip(txtfilename)
        MakeADescrip.TxtDescrip()
        print(MakeADescrip.toDescrip())
        
        
        # there's a difference between adding a new txt file to the thing and accessing it
        # this part of the application is supposed to add
        # i shouldn't try to use the same method for both and the same with a string
        
       
        
        
                
        
        
        
        
    elif(input2 =="C"):
        #now we use web scraping to grab some monsters. good fucking luck
        print('you rebel you')
        scrapeurl = 'https://www.dndbeyond.com/monsters?filter-type=0&filter-search=&filter-cr-min=&filter-cr-max=&filter-armor-class-min=&filter-armor-class-max=&filter-average-hp-min=&filter-average-hp-max=&filter-is-legendary=&filter-is-mythic=&filter-has-lair=&filter-source=1'
           
    
elif(switchstate == 'C'):# info about how M&M works
    
    print('filler text, I\'ll do it later')
    
elif(switchstate == 'D'): # look through book w/ gutendex, will need to enter monster stuff too
    
    print('-------------------------------------------------------------')
    print('Would you like to input a book or choose between some options?')
    print('A - Input Title')
    print('B - Receive some options')
    
    #what to do while page scraping w/ gutendex
    choice = input()
    print('-------------------------------------------------------------')
    gutenstring =''
    
    if(choice == 'A'):
        
        print('Enter the title or the Author\'s name (or both!)')
        searchstring = str(input())
        s = ''
        
        for x in searchstring:# formats things the way they need to be for gutendex
            if(x==' '):
                s+='%20'
            else:
                s+= x
            
        
        gutenstring = '?search='+s
        print(gutenstring)
    elif(choice =='B'):# this will just list all of the availible options for monster lit
        gutenstring = '?topic=monster'
    else:
        print("That wasn't an option, pal")
        
    # do the web scraping here with gutenstring

    
    
else:# this is just here for fun
    print("THAT WAS NOT AN OPTION\nTHE REAL MONSTER IS YOU")
    
    
    
    
    
    
    
    
    #i dont need to be claws scuttling across silent seas
    #i need a nap
    # z z z z z z z z z z
    
    
    
    