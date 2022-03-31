class machineUniverselle:
    
    def machine(self):
        #creation du ruban
        ruban=[None,self.memoireInterne,None,[],None,None,None,None,None]
        #on convertit le nombre en binaire pour le mettre dans le ruban
        nombreBinaire=self.decversbin()
        for x in range (len(nombreBinaire)):
            ruban.append((nombreBinaire[x]))
        #on ajoute du vide derriere le nombre
        for x in range(0,5):
            ruban.append(None)
        #on definit la tete dans l'etat 1 et a la position 8 ( juste avant le nombre )
        tete=[1,8]
        
        while True:
            ruban[3]=[]#on vide la memoire vive
            ruban[3].append(tete[0])#etat de la tete
            ruban[3].append(tete[1])#position 
            ruban[3][1]=ruban[ruban[3][1]]#position devient chiffre lu
            
            for x in range (len(ruban[1])):#on cherche dans la memoire interne ce qui 
            #correspond a notre memoire vive, et on remplace la memoire vive par ce qui 
            #doit etre renvoye apres
                if ruban[3]==ruban[1][x][0]:
                    ruban[3]=ruban[1][x][1]
            
            #on modifie l'etat de la tete, la valeur du ruban et apres on modifie la position
            tete[0]=ruban[3][0]
            ruban[tete[1]]=ruban[3][1]
            #si c'est la fin on sort de la boucle
            if ruban[3][2]=="fin":
                break
            else:  
            #sinon on ajoute ou enleve 1
                tete[1]+=ruban[3][2]
              
            #permet d'afficher que le nombre qui se trouve dans le ruban
            reponse=[]
            for x in range(len(ruban)):
                if type(ruban[x])==int:
                    reponse.append(ruban[x])      
            print(reponse)  
            
        #affiche a la fin lorsque c'est fini
        reponse=[]
        for x in range(len(ruban)):
            if type(ruban[x])==int:
                reponse.append(ruban[x])
        print(reponse)
        
    #toutes les memoires internes en fonction du calcul fait 
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
        
    #methode pour convertir en binaire notre nombre
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
print(" x2 : -------------------------")
machine.doublerUn(15)
print(" Plus 1 : -------------------------")
machine.Plus1(15)
print(" Moins 1 : -------------------------")
machine.Moins1(15)
print(" inversion : -------------------------")
machine.Inversion(15)