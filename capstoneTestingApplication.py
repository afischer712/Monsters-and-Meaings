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

from Description import Description # Description object
from SimScorer import SimScorer # used for the Similarity score
from ToDescrip import ToDescrip # txt / string / file / description transfer



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
          
            
        valid = False
        while valid !=True:
            valid = True
            
            mt = mt.isdigit()
            
            if(mt==1):
                monstertype = 'Abberation'
            elif(mt==2):
                monstertype = 'Beast'
            elif(mt==3):
                monstertype = 'Celestial'
            elif(mt==4):
                monstertype = 'Construct'
            elif(mt==5):
                monstertype = 'Dragon'
            elif(mt==6):
                monstertype = 'Elemental'
            elif(mt==7):
                monstertype = 'Fey'
            elif(mt==8):
                monstertype = 'Fiend'
            elif(mt==9):
                monstertype = 'Giant'
            elif(mt==10):
                monstertype = 'Humanoid'
            elif(mt==11):
                monstertype = 'Monstrosity'
            elif(mt==12):
                monstertype = 'Ooze'
            elif(mt==13):
                monstertype = 'Plant'
            elif(mt==14):
                monstertype = 'Undead'
            else:
                print("That wasn't an option. Please select a real choice")
                valid = False
            
        print('-------------------------------------------------------------')
        print('Enter a description of the monster!')
        descriptxt = input()
        
        userDescrip = Description(monstername, monstertype, descriptxt, False)
        
        print('-------------------------------------------------------------')
        print('Would you like a specific similarity score or a ranking with all monsters?')
        print('A - Pick a Monster')
        print('B - Compare with all Monsters')
        
        choice = input()
        
        if choice == 'A':# compare with one monster, faster
        
            print('-------------------------------------------------------------')
            print('Here are the availible monsters:')
            
            file = open('MonsterList.txt', 'r')# try catch?
            monsternames = file.readlines()
            
            for x in monsternames:
                print(x)
            
            print('-------------------------------------------------------------')
            print('Enter the name of a monster to compare your monster to it!')
            
            thismonster = input()
            
            newDescrip = ToDescrip()
            compareMonster = newDescrip.FileToDescrip(thismonster)
            
            print('Here are your results!')# add stuff here
            print('-------------------------------------------------------------')
            Scorer = SimScorer(userDescrip, compareMonster)
           
            
            
            
        elif choice == 'B':# compare with all monsters, will take time
        
            print('This might take a while!')
            
            print('Here are your results!')# add stuff here
            print('-------------------------------------------------------------')
        
        
        
        print('-------------------------------------------------------------')
        print('Would you like to add this monster to our collection? (y/n)')
        
        decision = input()
        if decision == 'y':
            print('Great! Your monster has been added!')
            fileMaker = ToDescrip()
            fileMaker.WriteToFile(userDescrip)
        elif decision == 'n':
            print('That\'s alright!')
        
        
            
    elif(switchstate == 'B'):# enter a monster into the system
        
        print('-------------------------------------------------------------')
        print('Awesome! Now enter the description of the monster!')
        print('A - Enter a .txt file')
        print('B - Type the description into the console')
        print('C - Build the collection from DNDBeyond (DO NOT PRESS)')
        
        input2 = input()
        print('-------------------------------------------------------------')
        
        if(input2 == 'B'):# enter one at a time
            
            
            
            # NOTE: THIS WOULD ALSO REQUIRE A FULL INPUT OF DND STUFF
            #        im just using this to test for now
            #       no longer just using to test, It's fine w/ monster type alone
            print('Enter the name of the monster!')
            monstername = input()
            print('-------------------------------------------------------------')
            print('Enter the type of the monster in D&D!')
            
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
                
            valid = False
            while valid !=True:
                valid = True
                
                if(mt==1):
                    monstertype = 'Abberation'
                elif(mt==2):
                    monstertype = 'Beast'
                elif(mt==3):
                    monstertype = 'Celestial'
                elif(mt==4):
                    monstertype = 'Construct'
                elif(mt==5):
                    monstertype = 'Dragon'
                elif(mt==6):
                    monstertype = 'Elemental'
                elif(mt==7):
                    monstertype = 'Fey'
                elif(mt==8):
                    monstertype = 'Fiend'
                elif(mt==9):
                    monstertype = 'Giant'
                elif(mt==10):
                    monstertype = 'Humanoid'
                elif(mt==11):
                    monstertype = 'Monstrosity'
                elif(mt==12):
                    monstertype = 'Ooze'
                elif(mt==13):
                    monstertype = 'Plant'
                elif(mt==14):
                    monstertype = 'Undead'
                else:
                    print("That wasn't an option. Please select a real choice")
                    valid = False
            
            print('-------------------------------------------------------------')
            ismonster = True
            
            print('Go ahead and enter the description now!')
            
            userDescrip = input()
           
            
            print('-------------------------------------------------------------')
            descripMaker = ToDescrip()
            descripMaker.StringDescrip(monstername, monstertype, userDescrip)
            print('-------------------------------------------------------------')
            
            
            # add monster name into a txt file that I can go through to get other descriptions
            
                        
        elif(input2 =='A'):# enter a txt file without parts of speech sorted
            
            
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
            
            
        elif(input2 =="C"): # this will eventually be the part that builds the system
            #now we use web scraping to grab some monsters. good fucking luck
            print('you rebel you')
            scrapeurl = 'https://www.dndbeyond.com/monsters?filter-type=0&filter-search=&filter-cr-min=&filter-cr-max=&filter-armor-class-min=&filter-armor-class-max=&filter-average-hp-min=&filter-average-hp-max=&filter-is-legendary=&filter-is-mythic=&filter-has-lair=&filter-source=1'
               
        
    
    elif(switchstate == 'C'):# just shows monsters, allows for users to view them
        
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
        print("That wasn't a choice, please return to the main menu.")
        
    print('-------------------------------------------------------------')
    print("Would you like to return to the main menu? (y/n)")
    loopChar = input()
    print('-------------------------------------------------------------')

print("Thank you for using Monsters & Meanings!")
       
    