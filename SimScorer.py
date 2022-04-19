# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:18:46 2022

@author: adfis
"""

from Description import Description
import spacy

class SimScorer:
    
    # constructor - also automatically scores, but I need to do more with that
    def __init__(self, desc1, desc2):
        self.desc1 = desc1
        self.desc2 = desc2
        self.score = 0
        self.Score()
        
    # just compares types, might delete
    def TypeCompare(self):
        
        if self.desc1.monstertype == self.desc2.monstertype:
            self.score += 20
           
    # Does the brunt of comparison work, looks at shared words and synonyms
    def ListScorer(self):
        
        nlp = spacy.load("en_core_web_lg")
            
        for x in self.desc1.nounList:
            
            for y in self.desc2.nounList:  
               
                if x == y:
                    self.score+=3
                
                doc1 = nlp(x)
                doc2 = nlp(y)
                self.score += doc1.similarity(doc2)
        
        for x in self.desc1.verbList: 
            for y in self.desc2.verbList:  
                if x == y:
                    self.score+=2
                    
        for x in self.desc1.adjList: 
            for y in self.desc2.adjList:   
                if x == y:
                    self.score+=4
            
        
    #this function will actually provide the similarity score btwn two descriptions
    def Score(self):
        # this is where the vector stuff needs to occur with semantic analysis
        self.score = 0
        
        self.TypeCompare()
        self.ListScorer()
        print(self.desc1.Name + " has a similarity score of " + str(self.score) + " with " + self.desc2.Name)
        
        return self.score