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
        self.outputlist = []
        
        
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
        outputString = self.Name + self.monstertype
        
        for x in self.nounList:
            outputString += x + " "
        
        for x in self.verbList:
            outputString += x + " "
        
        for x in self.adjList:
            outputString +=x + " "
        outputString+= self.descriptxt
        
        return outputString
    
    def toList(self):
        outputlist = []
        
        outputlist.append(self.Name)
        outputlist.append(self.monstertype)
        
        nounstring = ''
        verbstring = ''
        adjstring = ''
        
        for x in self.nounList:
            nounstring += " " + x
        for x in self.verbList:
            verbstring += " " + x
        for x in self.adjList:
            adjstring += " " + x
        
        outputlist.append(nounstring)
        outputlist.append(verbstring)
        outputlist.append(adjstring)
        
        outputlist.append(self.descriptxt)
        
        self.outputlist = outputlist
        
        return outputlist



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
    
    # makes a .txt file in the proper format for storing and using descriptions
    # also adds the monster to the monsterlist to be recalled
    def writeToFile(self, descrip):
        
        namename = descrip.Name.strip()
        filename = namename + '.txt'
        
        file = open(filename, "w")
        
        descrip.toList()
        
        for x in descrip.outputlist:
            file.write(x + '\n')
        file.close()
        
        namefile = open("MonsterList.txt", "a")
        namefile.write(descrip.Name + "\n")  
      
    # This method is for turning strings into a Description and writing it to a txt file
    def StringDescrip(self, name, monstertype, descriptxt):
        
        stringdescrip = Description(name, True, monstertype, descriptxt)
        self.writeToFile(stringdescrip)
        
        print(stringdescrip.tostring())
        
        
        
    #creates description object from contents of file
    def TxtDescrip(self, filename):
        
        
        file = open(filename, 'r')
        
        name = file.readline()
        monstertype = file.readline()
        descriptxt = file.readline()
        
        
        file.close()
        
     
        
        newDescrip = Description(name, True, monstertype, descriptxt)
        self.writeToFile(newDescrip)
        print(newDescrip.tostring())




# THIS IS WHERE STUFF BEGINS
loopChar = 'y'
while loopChar != 'n':
    
    print('WELCOME TO MONSTERS & MEANINGS, YOUR TTRPG CREATION COMPANION')
    print('-------------------------------------------------------------')
    print('A - Test our Monster Collection for description similarity!')
    print('B - Add a Monster Description to our collection!')
    print('C - View all Monster Descriptions!')
    print('D - Search a piece of literature for a monster description!')
    print('E - Information on how Monsters & Meanings works!')
    print('-------------------------------------------------------------')
    
    userchoice = input()
    switchstate = userchoice.capitalize()
    
    if(switchstate == 'A'): # monster comparison
        
        print('-------------------------------------------------------------')
        print('Enter the name of your monster!')
        monstername = input()
        
        print('-------------------------------------------------------------')
        print('Enter the type of the monster!')
        print('-------------------------------------------------------------')
        print('1 - Aberration\n2 - Beast\n3 - Celestial\n4 - Construct\n5 - Dragon\n6 - Elemental\n7 - Fey\n8 - Fiend\n9 - Giant\n10 - Humanoid\n11 - Monstrosity\n12 - Ooze\n13 - Plant\n14 - Undead')
        print('-------------------------------------------------------------')
        print('(Enter TYPE for options and explanations)')
        mt = input()
        
        if mt == "TYPE":
            
            print('-------------------------------------------------------------\n')
            print("1 - Abberation - Aberrations are utterly alien beings. Many \nof them have innate magical abilities drawn from the creature’s\nalien mind rather than the mystical forces of the world\n")
            print("2 - Beast - Beasts are nonhumanoid creatures that are a natural\npart of the fantasy ecology. Some of them have magical powers,\nbut most are unintelligent and lack any society or language.\nBeasts include all varieties of ordinary animals, dinosaurs,\nand giant versions of animals\n")
            print("3 - Celestial - Celestials are creatures native to the Upper\nPlanes. Many of them are the servants of deities, employed as\nmessengers or agents in the mortal realm and throughout the\nplanes. Celestials are good by nature, so the exceptional\ncelestial who strays from a good alignment is a horrifying\nrarity. Celestials include angels, couatls, and pegasi\n")
            print("4 - Construct - Constructs are made, not born. Some are\nprogrammed by their creators to follow a simple set of\ninstructions, while others are imbued with sentience and\ncapable of independent thought. Golems are the iconic\nconstructs. Many creatures native to the outer plane of\nMechanus, such as modrons, are constructs shaped from the raw\nmaterial of the plane by the will of more powerful creature\n")
            print("5 - Dragon - Dragons are large reptilian creatures of ancient\norigin and tremendous power. True dragons, including the good\nmetallic dragons and the evil chromatic dragons, are highly\nintelligent and have innate magic. Also in this category are\ncreatures distantly related to true dragons, but less powerful,\nless intelligent, and less magical, such as wyverns and\n pseudodragons\n")
            print("6 - Elemental - Elementals are creatures native to the elemental\nplanes. Some creatures of this type are little more than animate\nmasses of their respective elements, including the creatures\nsimply called elementals. Others have biological forms infused\nwith elemental energy. The races of genies, including djinn\nand efreet, form the most important civilizations on the\nelemental planes. Other elemental creatures include azers,\ninvisible stalkers, and water weirds\n")
            print("7 - Fey - Fey are magical creatures closely tied to the forces\nof nature. They dwell in twilight groves and misty forests. In\nsome worlds, they are closely tied to the Plane of Faerie. Some\nare also found in the Outer Planes, particularly the planes of\nArborea and the Beastlands. Fey include dryads, pixies, and satyrs\n")
            print("8 - Fiend - Fiends are creatures of wickedness that are native\nto the Lower Planes. A few are the servants of deities, but many\nmore labor under the leadership of archdevils and demon princes.\nEvil priests and mages sometimes summon fiends to the material\nworld to do their bidding. If an evil celestial is a rarity, a\ngood fiend is almost inconceivable. Fiends include demons,\ndevils, hell hounds, rakshasas, and yugoloths\n")
            print("9 - Giant - Giants tower over humans and their kind. They are\nhumanlike in shape, though some have multiple heads (ettins) or\ndeformities (fomorians). The six varieties of true giant are\nhill giants, stone giants, frost giants, fire giants, cloud\ngiants, and storm giants. Besides these, creatures such as\nogres and trolls are giants\n")
            print("10 - Humanoid - Humanoids are the main peoples of a fantasy\ngaming world, both civilized and savage, including humans and\na tremendous variety of other species. They have language and\nculture, few if any innate magical abilities (though most\nhumanoids can learn spellcasting), and a bipedal form. The\nmost common humanoid races are the ones most suitable as player\ncharacters: humans, dwarves, elves, and halflings\n")
            print("11 - Monstrosity - Monstrosities are monsters in the strictest\nsense—frightening creatures that are not ordinary, not truly\nnatural, and almost never benign. Some are the results of\nmagical experimentation gone awry (such as owlbears), and\nothers are the product of terrible curses (including minotaurs\nand yuan-ti). They defy categorization, and in some sense\nserve as a catch-all category for creatures that don’t fit\ninto any other type\n")
            print("12 - Ooze - Oozes are gelatinous creatures that rarely have a\nfixed shape. They are mostly subterranean, dwelling in caves\nand dungeons and feeding on refuse, carrion, or creatures\nunlucky enough to get in their way. Black puddings and\ngelatinous cubes are among the most recognizable oozes\n")
            print("13 - Plant - Plants in this context are vegetable creatures,\nnot ordinary flora. Most of them are ambulatory, and some are\ncarnivorous. The quintessential plants are the shambling mound\nand the treant. Fungal creatures such as the gas spore and the\nmyconid also fall into this category\n")
            print("14 - Undead - Undead are once-living creatures brought to a\nhorrifying state of undeath through the practice of necromantic\nmagic or some unholy curse. Undead include walking corpses,\nsuch as vampires and zombies, as well as bodiless spirits, such\nas ghosts and specters\n")
            print('-------------------------------------------------------------')
            mt = input()
            
        if(mt==1):
            monstertype = 'Abberation'
        if(mt==2):
            monstertype = 'Beast'
        if(mt==3):
            monstertype = 'Celestial'
        if(mt==4):
            monstertype = 'Construct'
        if(mt==5):
            monstertype = 'Dragon'
        if(mt==6):
            monstertype = 'Elemental'
        if(mt==7):
            monstertype = 'Fey'
        if(mt==8):
            monstertype = 'Fiend'
        if(mt==9):
            monstertype = 'Giant'
        if(mt==10):
            monstertype = 'Humanoid'
        if(mt==11):
            monstertype = 'Monstrosity'
        if(mt==12):
            monstertype = 'Ooze'
        if(mt==13):
            monstertype = 'Plant'
        if(mt==14):
            monstertype = 'Undead'
        
        print('-------------------------------------------------------------')
        print('Enter a description of the monster!')
        descriptxt = input()
        
        userDescrip = Description(monstername, True, monstertype, descriptxt)
        
        print('-------------------------------------------------------------')
        print('Here are your results!')# add stuff here
        print('-------------------------------------------------------------')
        
        print('-------------------------------------------------------------')
        print('Would you like to add this monster to our collection? (y/n)')
        
        decision = input()
        if decision == 'y':
            print('Great! Your monster has been added!')
            fileMaker = ToDescrip()
            fileMaker.writeToFile(userDescrip)
        elif decision == 'n':
            print('That\'s alright!')
        
        
            
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
           
            
            print('-------------------------------------------------------------')
            descripMaker = ToDescrip()
            descripMaker.StringDescrip(monstername, monstertype, userDescrip)
            print('-------------------------------------------------------------')
            
            
            
            
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
            
            MakeADescrip = ToDescrip()
            MakeADescrip.TxtDescrip(txtfilename)
            
            
            
            # there's a difference between adding a new txt file to the thing and accessing it
            # this part of the application is supposed to add
            # i shouldn't try to use the same method for both and the same with a string
            
           
            
            
                    
            
            
            
            
        elif(input2 =="C"):
            #now we use web scraping to grab some monsters. good fucking luck
            print('you rebel you')
            scrapeurl = 'https://www.dndbeyond.com/monsters?filter-type=0&filter-search=&filter-cr-min=&filter-cr-max=&filter-armor-class-min=&filter-armor-class-max=&filter-average-hp-min=&filter-average-hp-max=&filter-is-legendary=&filter-is-mythic=&filter-has-lair=&filter-source=1'
               
        
    
    elif(switchstate == 'C'):
        
        print('-------------------------------------------------------------')
        print('Here are the availible monsters:')
        
        file = open('MonsterList.txt', 'r')
        monsternames = file.readlines()
        
        for x in monsternames:
            print(x)
        
        print('-------------------------------------------------------------')
        print('Enter the name of a monster to view its description!')
        
        thismonster = input()
        
        
        file2 = open(thismonster + ".txt", 'r')
        outputdescrip = file2.readlines()
        
        print('-------------------------------------------------------------')
        for x in outputdescrip:
            print(x)
        print('-------------------------------------------------------------')
        
        
        
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
    
    elif(switchstate == 'E'):# info about how M&M works
          
          print('filler text, I\'ll do it later')  
        
    else:# this is just here for fun
        print("THAT WAS NOT AN OPTION\nTHE REAL MONSTER IS YOU")
        
    print('-------------------------------------------------------------')
    print("Would you like to return to the main menu? (y/n)")
    loopChar = input()
    print('-------------------------------------------------------------')

print("Thank you for using Monsters & Meanings!")
        
    
    
    
    
    
    
    
    #i dont need to be claws scuttling across silent seas
    #i need a nap
    # z z z z z z z z z z
    
    
    
    