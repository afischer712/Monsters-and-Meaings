# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:22:20 2022

@author: adfis
"""



import spacy # semantic analysius
import selenium # web scraping
from time import sleep # helps w/ web scraping
import pickle# serialization
import pandas as pd # used with spacy

class Description:
    def __init__(self, nounList, verbList, adjList, Name, monster):
        self.nounList = nounList
        self.verbList = verbList
        self.adjList = adjList
        self.Name = Name
        self.monster = monster

class SimScorer:
    def __init__(self, desc1, desc2):
        self.desc1 = desc1
        self.desc2 = desc2
    
    def Score(desc1, desc2):
        
        
        score = 0
        print(desc1.name + " has a similarity score of " + score + " with " + desc2.name)
        return score
    

nlp = spacy.load("en_core_web_sm")

# THIS IS WHERE STUFF BEGINS
print('WELCOME TO MONSTERS & MEANINGS, YOUR TTRPG CREATION COMPANION')
print('-------------------------------------------------------------')
print('A - Add a Monster Description to our collection!')
print('B - Test our Monster Collection for description similarity!')
print('C - Information on how Monsters & Meanings works!')
print('D - Search a piece of literature for a monster description!')
print('-------------------------------------------------------------')

userchoice = input()
switchstate = userchoice.capitalize()

if(switchstate == 'B'):
    
    print('daf')
    
elif(switchstate == 'A'):
    
    print('Awesome! Now enter the description of the monster!')
    print('A - Enter a .txt file')
    print('B - Type the description into the console')
    print('C - Build the collection from DNDBeyond (DO NOT PRESS)')
    
    input2 = input()
    
    if(input2 == 'B'):
        
        descrip = Description()
        
        # NOTE: THIS WOULD ALSO REQUIRE A FULL INPUT OF DND STUFF
        #        im just using this to test for now
        print('Enter the name of the monster!')
        
        monstername = input()
        descrip.Name = monstername
        descrip.monster = True
        
        print('Go ahead and enter the description now!')
        userDescrip = input()
       
        
        doc = nlp(userDescrip)
        
        for t in doc:# sorts words into lists by part of speech
    
            if(t.pos_ == 'NOUN'):
                descrip.nounList.append(t.lemma_)
            elif(t.pos_ == 'VERB'):
                descrip.verbList.append(t.lemma_)
            elif(t.pos_ == "ADJ"):
                descrip.adjList.append(t.lemma_)
                
        for x in descrip.nounList:
            print(x)
           # row = [t.text, t.lemma_, t.pos_, spacy.explain(t.pos_), t.is_stop]
           
    elif(input2 =='A'):
        print('dummy text')# this is where i take in a txt file
        #ITERATE through txt to make a descrip object, then pickle it
        
    elif(input2 =="C"):
        #now we use web scraping to grab some monsters. good fucking luck
        
        scrapeurl = 'https://www.dndbeyond.com/monsters?filter-type=0&filter-search=&filter-cr-min=&filter-cr-max=&filter-armor-class-min=&filter-armor-class-max=&filter-average-hp-min=&filter-average-hp-max=&filter-is-legendary=&filter-is-mythic=&filter-has-lair=&filter-source=1'
           
    
elif(switchstate == 'C'):# info about how M&M works
    
    print('filler text, I\'ll do it later')
    
elif(switchstate == 'D'): # look through book w/ gutendex, will need to enter monster stuff too
    
    print('Would you like to input a book or choose between some options?')
    print('A - Input Title')
    print('B - Receive some options')
    
    #what to do while page scraping w/ gutendex
    choice = input()
    gutenstring =''
    
    if(choice == 'A'):
        
        print('Enter the title or the Author\s name (or both!)')
        searchstring = str(input())
        s = ''
        
        for x in searchstring:
            if(x==' '):
                s+='%20'
            else:
                s+= x
            
        
        gutenstring = '?search='+s
        print(gutenstring)
    elif(choice =='B'):
        gutenstring = '?topic=monster'
    else:
        print("That wasn't an option, pal")
        
    # do the web scraping here with gutenstring

    
    
else:
    print("THAT WAS NOT AN OPTION\nTHE REAL MONSTER IS YOU")
    
    
    
    
    
    
    
    
    
    
    
    
    