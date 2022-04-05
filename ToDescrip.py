# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:19:45 2022

@author: adfis
"""

from Description import Description

class ToDescrip:
    
    # makes a .txt file in the proper format for storing and using descriptions
    # also adds the monster to the monsterlist to be recalled
    def WriteToFile(self, descrip):
        
        namename = descrip.Name.strip()
        filename = namename + '.txt'
        
        file = open(filename, "w")
        
        descrip.toList()
        
        for x in descrip.outputlist:
            file.write(x + '\n')
        file.close()
        
        namefile = open("MonsterList.txt", "a")
        namefile.write(descrip.Name + "\n")  
    
    # makes a description object out of the .txt file
    def FileToDescrip(self, monstername):
        
        filename = monstername + '.txt'
        
        file = open(filename, 'r')
        
        name = file.readline()
        monstertype = file.readline()
        
        nouns = []
        nounstring = file.readline()
        noun = ''
        
        for x in nounstring:
            
            if x == " " and noun != "":
                nouns.append(noun)
                noun = ""
            else:
                noun += x
        
        verbs = []
        verbstring = file.readline()
        verb = ''
        
        for x in verbstring:
            
            if x == " " and verb != "":
                verbs.append(verb)
                verb = ""
            else:
                verb += x
        
        adjs = []
        adjstring = file.readline()
        adj = ''
        
        for x in adjstring:
            
            if x == " " and adj != "":
                adjs.append(adj)
                adj = ""
            else:
                adj += x
                
        descriptxt = file.readline()
        
        descrip = Description(name, monstertype, descriptxt, True)
        descrip.AlreadySorted(nouns, verbs, adjs)
        
        return descrip
      
    # This method is for turning strings into a Description and writing it to a txt file
    def StringDescrip(self, name, monstertype, descriptxt):
        
        stringdescrip = Description(name, monstertype, descriptxt, True)
        self.WriteToFile(stringdescrip)
        
        print(stringdescrip.tostring())
        
        
        
    #creates description object from contents of file
    def TxtDescrip(self, filename):
        
        
        file = open(filename, 'r')
        
        name = file.readline()
        monstertype = file.readline()
        descriptxt = file.readline()
        
        
        file.close()
        
     
        
        newDescrip = Description(name, monstertype, descriptxt, True)
        self.WriteToFile(newDescrip)
        print(newDescrip.tostring())