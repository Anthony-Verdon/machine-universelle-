class machineUniverselle:
    
    def machine(self):
        ruban=[None,self.memoireInterne,None,[],None,None,None,None,None]
        nombreBinaire=self.decversbin()
        for x in range (len(nombreBinaire)):
            ruban.append((nombreBinaire[x]))
        
        for x in range(0,5):
            ruban.append(None)
        
        tete=[1,8]
        
        while True:
            ruban[3]=[]
        
            ruban[3].append(tete[0])
            ruban[3].append(tete[1])
            ruban[3][1]=ruban[ruban[3][1]]
            #print(ruban[3])
        
            #print("-----------------------------------")
            for x in range (len(ruban[1])):
                if ruban[3]==ruban[1][x][0]:
                    ruban[3]=ruban[1][x][1]
            #print(ruban[3])
            #print("-----------------------------------")
        
            tete[0]=ruban[3][0]
            #print(tete[1])
            ruban[tete[1]]=ruban[3][1]
            if ruban[3][2]=="fin":
                break
            else:   
                tete[1]+=ruban[3][2]
                
            reponse=[]
            for x in range(len(ruban)):
                if type(ruban[x])==int:
                    reponse.append(ruban[x])
            print(reponse)   
        reponse=[]
        for x in range(len(ruban)):
            if type(ruban[x])==int:
                reponse.append(ruban[x])
        print(reponse)
        
    def x2(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[2,0,"fin"])]
        self.nombre=nombre
        return self.machine()

    def doublerUn(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[3,0,-1]),([2,None],[4,None,-1]),([3,0],[3,0,-1]),([3,None],[2,0,1]),([4,0],[4,1,-1]),([4,None],[4,None,'fin'])]
        self.nombre=nombre
        return self.machine()

    def Plus1(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[3,None,-1]),([3,0],[3,1,'fin']),([3,1],[3,0,-1]),([3,None],[3,1,'fin'])]
        self.nombre=nombre
        return self.machine()

    def Moins1(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[3,None,-1]),([3,0],[3,1,-1]),([3,1],[3,0,'fin']),([3,None],[3,None,'fin'])]
        self.nombre=nombre
        return self.machine()

    def Inversion(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,1,1]),([2,1],[2,0,1]),([2,None],[2,None,'fin'])]
        self.nombre=nombre
        return self.machine()
        
    def decversbin(self):
            base=2
            resultat=[]
            while self.nombre!=0:
                resultat.append(self.nombre%base)
                self.nombre=self.nombre//base
            resultat.reverse()
            return resultat

machine=machineUniverselle()
machine.x2(15)
print("-------------------------")
machine.doublerUn(15)
print("-------------------------")
machine.Plus1(15)
print("-------------------------")
machine.Moins1(15)
print("-------------------------")
machine.Inversion(15)