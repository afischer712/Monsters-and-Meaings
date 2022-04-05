# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:38:27 2022

@author: adfis
"""

import spacy # semantic analysis

class Description:
    
    # constructor for description, boolean is for overloading
    def __init__(self, Name, monstertype, descriptxt, parts):
        self.nounList = []
        self.verbList = []
        self.adjList = []
        self.Name = Name
        self.monstertype = monstertype
        self.descriptxt = descriptxt
        if parts == False:    
            self.PartsOfSpeech()
        self.outputlist = []
        
        
    #automatically generates the lists for parts of speech
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
    
    # python doesn't support overloading, so here's wonderwall
    def AlreadySorted(self, nouns, verbs, adjs):
        self.nounList = nouns
        self.verbList = verbs
        self.adjList = adjs
        
        
    # to string mostly to test stuff, but also just shows user things are working
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
    
    # toList is used for generating the right strings for saving info
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