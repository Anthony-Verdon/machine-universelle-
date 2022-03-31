# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:50:34 2022

@author: Wuufa
"""

class TuringMachine:
    def __init__(self,chiffre,mode):
        self._mode=mode
        self._chiffre=chiffre
        
    def decversbin(self):
        base=2
        resultat=[]
        while self._chiffre!=0:
            resultat.append(self._chiffre%base)
            self._chiffre=self._chiffre//base
        resultat.reverse()
        resultat.append("*")
        resultat.insert(0,"*")
    
        return resultat
    
    
    def plusun(self):
        chiffrebin=self.decversbin()
        etat=1
        case=0
        while etat==1:
            if chiffrebin[case]=="*":
                case+=1
                etat+=1
        while etat==2:
            if chiffrebin[case]==0:
                case+=1
            if chiffrebin[case]==1:
                case+=1
            if chiffrebin[case]=="*":
                case-=1
                etat+=1
        while etat==3:
            if chiffrebin[case]==0:
                chiffrebin[case]=1
                return chiffrebin[1:len(chiffrebin)-1]
            if chiffrebin[case]==1:
                chiffrebin[case]=0
                case-=1
            if chiffrebin[case]=="*":
                chiffrebin[case]=1
                return chiffrebin[:len(chiffrebin)-1]
                
            
    def foisdeux(self):
        chiffrebin=self.decversbin()
        etat=1
        case=0
        while etat==1:
            if chiffrebin[case]=="*":
                case+=1
                etat+=1
        while etat==2:
            if chiffrebin[case]==0:
                case+=1
            if chiffrebin[case]==1:
                case+=1
            if chiffrebin[case]=="*":
                chiffrebin[case]=0
                return chiffrebin[1:]
                
          
        
    
test=TuringMachine(15,"yay")
print(test.plusun())
#print(test.foisdeux())