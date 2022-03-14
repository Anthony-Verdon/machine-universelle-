import time
import tkinter
from PIL import ImageTk, Image

#classe menu, se charge de la page menu
class Menu:
    
    #créer nos différents objets ( boutons ou frame contenant d'autres objets )
    def __init__(self):
        
        self.calcul=""
        
        self.menu=tkinter.Tk()#créer la fenêtre
        self.frameBouton=tkinter.Frame(bg="#EB9F1B")#créer la frame bouton
        self.frameImage=tkinter.Frame(bg="#EB9F1B")#créer la frame image
        self.frameInput=tkinter.Frame(bg="#EB9F1B")#créer la frame Input
        self.frameCalcul=tkinter.Frame(bg="#EB9F1B")#créer la frame bouton
        
        
        self.boutonTab1=tkinter.Button(self.frameBouton,text="lancer la machine",font=("Kokonor",20),bg="#EB9F1B",command=self.Commande1)#créer le bouton pour lancer la machine
        self.boutonQuitter=tkinter.Button(self.menu,text="quitter",font=("Kokonor",20),bg="#EB9F1B",command=self.quitter)#créer le bouton " Quitter "
        self.boutonInput=tkinter.Button(self.frameInput,text="envoyer les informations",font=("Kokonor",20),bg="#EB9F1B",command=self.InputUtilisateur)#créer le bouton " envoyer les informations "
        
        self.boutonX2=tkinter.Button(self.frameCalcul,text="x2",font=("Kokonor",20),bg="#EB9F1B",command=self.commandex2)#créer le bouton pour choisir le calcul x2
        self.boutonDOUBLER1=tkinter.Button(self.frameCalcul,text="doubler une liste de 1",font=("Kokonor",20),bg="#EB9F1B",command=self.commandeDoublerUn)#créer le bouton pour choisir le calcul " doubler une liste de 1 "
        self.boutonPLUS1=tkinter.Button(self.frameCalcul,text="+1",font=("Kokonor",20),bg="#EB9F1B",command=self.commandePlus1)#créer le bouton pour choisir le calcul +1
        self.boutonMOINS1=tkinter.Button(self.frameCalcul,text="-1",font=("Kokonor",20),bg="#EB9F1B",command=self.commandeMoins1)#créer le bouton pour choisir le calcul -1
        self.boutonINVERSION=tkinter.Button(self.frameCalcul,text="inverser les 1 et les 0",font=("Kokonor",20),bg="#EB9F1B",command=self.commandeInversion)#créer le bouton pour inverser les 1 et les 0
    
    #se charge de faire apparaître et de placer les images, boutons  et entrées de texte
    def lancerMenu(self):
        
        self.menu.title("Jeu de la Vie")#ajoute un titre à la fenêtre
        self.menu.geometry("1920x1080")#donne les dimensions de la fenêtre
        self.menu.iconbitmap("logo.ico")#ajoute une icône à la fenêtre
        self.menu.minsize(1920,1080)#donne une taille minimale à la fenêtre
        self.menu.config(background="#EB9F1B")#change la couleur de fond de la fenêtre
        
        self.frameImage.pack(expand="yes")#affiche et centre la frame image
        
        self.InputTour=tkinter.Entry(self.frameInput,font=("Kokonor",20))#créer un input 
        self.InputTour.insert(0,"noter nombre à changer")#le placeholder de l'input
        self.InputTour.bind('<FocusIn>', self.removeTour)#si on clique dessus, lance la fonction removeTour
        self.InputTour.pack(pady=10)#affiche l'input avec une marge externe en haut et en bas
        
        img4 = ImageTk.PhotoImage(Image.open("PointInterrogation.png"))
        panel4 = tkinter.Button(self.menu, image = img4,bg="#EB9F1B",command=self.PointInterrogation)#créer un bouton à partir de l'image 
        panel4.place(x=1325,y=25)#place le bouton à des coordonnées précises
        
        #bouton pratique
        self.boutonInput.pack(pady=10)
        self.frameInput.place(x=1200,y=540)
        self.boutonTab1.pack(side="left",padx=10)
        self.frameBouton.pack(expand="yes")
        self.boutonQuitter.place(x=1400,y=25)
        
        #bouton calcul
        self.boutonX2.pack(side="left",padx=10)
        self.boutonDOUBLER1.pack(side="left",padx=10)
        self.boutonPLUS1.pack(side="left",padx=10)
        self.boutonMOINS1.pack(side="left",padx=10)
        self.boutonINVERSION.pack(side="left",padx=10)
        self.frameCalcul.pack(expand="yes")
        
        self.menu.mainloop()#permet de voir si il y a des interactions avec la fenêtre 
    
    #commande du bouton " Envoyer les informations ",récupère les informations envoyé par l'utilisateur
    def InputUtilisateur(self):
        self.NbTour=self.InputTour.get()#reçoit les informations données par l'utilisateur pour pouvoir les utiliser afin de lancer le jeu
        return self.NbTour
       
    #commande qui supprime le placeholder dans l'entree tour
    def removeTour(self,event):
        self.InputTour.delete(0, tkinter.END)#supprime le texte, appelez placeholder, qui est afficher dans l'input quand on clique dessus

    #message d'information
    def PointInterrogation(self):
        popUp=tkinter.Tk()
        popUp.title("Informations supplémentaires")
        popUp.geometry("1080x360+200+200")
        popUp.iconbitmap("logo.ico")
        popUp.minsize(1080,360)
        popUp.config(background="#EB9F1B")
        labelPopUp=tkinter.Label(popUp, text="Bonjour et merci d'utiliser notre application !\n Pour faire un calcul, vous devez d'abord envoyer les informations demandées en bas à droite,\n puis choisir votre calcul.\n A chaque utilisation, vous devrez renoter les informations. ",justify="center",font=("Kokonor",20),bg="#EB9F1B")
        labelPopUp.pack(expand="yes")
        
    #commande du bouton " quitter ",ferme la fenêtre menu
    def quitter(self):
        self.menu.destroy()
       
    #permet de savoir quelle calcul on va faire quand on lancera la machine
    def commandex2(self):
        self.calcul="x2"
    
    def commandeDoublerUn(self):
        self.calcul="doublerUn"
    
    def commandePlus1(self):
        self.calcul="Plus1"
    
    def commandeMoins1(self):
        self.calcul="Moins1"
    
    def commandeInversion(self):
        self.calcul="inversion"
    
    
    #commande du bouton " lancer la machine ", lance la fenêtre jeu et ferme la fenêtre menu
    def Commande1(self):
        try:
            if int(self.NbTour)<0 or self.calcul=="":
                self.Erreur()
            else:
                self.menu.destroy()#ferme la fenêtre menu
                JeuVie=Jeu()#créer un objet de la classe jeu
                JeuVie.lancerJeu(int(self.NbTour),self.calcul)#lance le jeu avec les informations de l'utilisateur
            
        except AttributeError:#si attribut non conforme, on envoie une erreur
            self.Erreur()   
            
        except TypeError:#si attribut non conforme, on envoie une erreur
            self.Erreur()
        
        except IndexError:#si attribut non conforme, on envoie une erreur
            self.Erreur()
        except ValueError:#si valeur non conforme, on envoie une erreur
            self.Erreur()   
        
#message d'erreur
    def Erreur(self):
        MessageErreur=tkinter.Tk()
        MessageErreur.title("Erreur : informations manquantes")
        MessageErreur.geometry("1080x360+200+200")
        MessageErreur.iconbitmap("logo.ico")
        MessageErreur.minsize(1080,360)#donne une taille minimale à la fenêtre
        MessageErreur.config(background="#EB9F1B")
        labelErreur=tkinter.Label(MessageErreur, text="Informations manquantes ou problèmes,\n merci de spécifier les valeurs nécessaires\n en chiffres ( supérieurs ou égaux à 0 ) en bas à droite.\n Pour plus d'informations cliquez sur le bouton  ? en haut à droite ou contacter le développeur ",justify="center",font=("Kokonor",20),bg="#EB9F1B")
        labelErreur.pack(expand="yes")

#classe jeu, se charge de la page jeu
class Jeu:
    
    #créer nos différents objets ( boutons ou frame contenant d'autres objets )
    def __init__(self):
        self.jeu=tkinter.Tk()
        self.bigframe=tkinter.Frame(self.jeu,bd=10,relief=tkinter.SUNKEN)
        self.frameCompteur=tkinter.Frame(self.jeu)
        self.bouton=tkinter.Button(self.jeu,text="revenir au menu",font=("Kokonor",20),bg="#EB9F1B",command=self.quitter) 
        
    #gère l'affichage de la page jeu
    def lancerJeu(self,nombre,calcul):
        
        self.jeu.title("Jeu de la Vie")
        self.jeu.geometry("1920x1080")
        self.jeu.iconbitmap("logo.ico")
        self.jeu.minsize(1920,1080)
        self.jeu.config(background="#EB9F1B")
        
        #bouton Pause
        self.nbPause=1#créer une variable égal à 1 de base pour que le jeu soit en pause quand on lance le jeu
        self.img5 = ImageTk.PhotoImage(Image.open("PauseImageResize.png"))
        self.img6 = ImageTk.PhotoImage(Image.open("PlayImageResize.png"))
        self.Pause = tkinter.Button(self.jeu,image = self.img6,bg="#EB9F1B",command=self.etatBouton) 
        self.Pause.place(x=200,y=390)
        self.bouton.place(x=1300,y=25)
        
        #donne la bonne mémoire en fonction du choix fait plus tôt
        if calcul=="x2":
            self.x2(nombre)
        elif calcul=="doublerUn":
            self.doublerUn(nombre)
        elif calcul=="Plus1":
            self.Plus1(nombre)
        elif calcul=="Moins1":
            self.Moins1(nombre)
        elif calcul=="inversion":
            self.inversion(nombre)
            
        #création du ruban
        self.ruban=[None,self.memoireInterne,None,[],None,None,None,None,None]
        nombreBinaire=self.decversbin()#on adapte le chiffre en binaire ( des 1 et des 0)
        for x in range (len(nombreBinaire)):#on l'ajoute au ruban
            self.ruban.append((nombreBinaire[x]))
        
        for x in range(0,7):#on rajoute du vide
            self.ruban.append(None)
        
        self.tete=[1,8]#on définit l'état de la tête et sa position, à adapter en fonction du nombre de None
        
        #permet d'afficher la partie du ruban qui nous intéresse, le vide et les nombres, avant de cliquer sur le bouton play
        reponse=[]
        for x in range(len(self.ruban)):
            if type(self.ruban[x])==int or self.ruban[x]==None:
                reponse.append(self.ruban[x])
        self._tableau=reponse
        self.AffichageTableau()
        
        #update du tableau : on regarde la case, et l'état de la tête, on stocke dans la mémoire vive, on cherche ce qui correspond dans la mémoire interne et ensuite on adapte la case, l'état de la tête et enfin sa position
        while True:
            time.sleep(1)#pour qu'on voit ce qu'il se passe
            if self.nbPause%2==1:#si la variable%2 == 1, on met en pause tant que c'est égal à 1
                while self.nbPause%2==1:
                    self.jeu.update()
    
            self.ruban[3]=[]
        
            self.ruban[3].append(self.tete[0])
            self.ruban[3].append(self.tete[1])
            self.ruban[3][1]=self.ruban[self.ruban[3][1]]
            for x in range (len(self.ruban[1])):
                if self.ruban[3]==self.ruban[1][x][0]:
                    self.ruban[3]=self.ruban[1][x][1]
        
            self.tete[0]=self.ruban[3][0]
            self.ruban[self.tete[1]]=self.ruban[3][1]
            if self.ruban[3][2]=="fin":
                break
            else:   
                self.tete[1]+=self.ruban[3][2]
                
            reponse=[]
            for x in range(len(self.ruban)):
                if type(self.ruban[x])==int or self.ruban[x]==None:
                    reponse.append(self.ruban[x])
            self._tableau=reponse
           
            self.compteur()
            self.AffichageTableau()
            
        reponse=[]
        for x in range(len(self.ruban)):
            if type(self.ruban[x])==int or self.ruban[x]==None:
                reponse.append(self.ruban[x])
        self._tableau=reponse
        
        self.AffichageTableau()
        self.compteur()
        self.jeu.mainloop()
    
    #affiche le tableau 
    def AffichageTableau(self):
        
        self.clear_frame()#lance la méthode clear_frame pour vider le tableau
        tabFrame=[]#créer un 2nd tableau
        self.bigframe=tkinter.Frame(self.jeu,bd=10,relief=tkinter.SUNKEN)
        self.bigframe.pack(expand="yes")
        for x in range(1):
            #creation et affichage de la nouvelle frame ( 1 par ligne du tableau )
            tabFrame.append(tkinter.Frame(self.bigframe))
            tabFrame[x].pack()
            for y in range(len(self._tableau)):
                if self._tableau[y]==None:
                    
                    if y==self.tete[1]-2:
                        label_title=tkinter.Label(tabFrame[x],text=" ",font=("Courrier",20),fg="black",bg="red")
                        label_title.pack(side="left")#pour que cela s'affiche en ligne
            
                    else:
                        label_title=tkinter.Label(tabFrame[x],text=" ",font=("Courrier",20),fg="black")
                        label_title.pack(side="left")#pour que cela s'affiche en ligne
                else:
                    if y==self.tete[1]-2:
                        label_title=tkinter.Label(tabFrame[x],text=self._tableau[y],font=("Courrier",20),fg="black",bg="red")
                        label_title.pack(side="left")#pour que cela s'affiche en ligne
            
                    else:
                        label_title=tkinter.Label(tabFrame[x],text=self._tableau[y],font=("Courrier",20),fg="black")
                        label_title.pack(side="left")#pour que cela s'affiche en ligne
        
        self.jeu.update()#permet de mettre à jour le tableau
    
    #supprime le tableau
    def clear_frame(self):
        self.bigframe.destroy()
        
        
    #modifie l'affichage à côté du bouton Pause
    def etatBouton(self):
        self.nbPause+=1
        if self.nbPause%2==1:
            self.Pause.configure(image=self.img6)#si on est en pause, on affiche le logo play 
        else:
            self.Pause.configure(image=self.img5)#sinon le logo pause
         
    #donne la mémoire en fonction du calcul qu'on fait
    def x2(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[2,0,"fin"])]
        self.nombre=nombre
        
    def doublerUn(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[3,0,-1]),([2,None],[4,None,-1]),([3,0],[3,0,-1]),([3,None],[2,0,1]),([4,0],[4,1,-1]),([4,None],[4,None,'fin'])]
        self.nombre=nombre
        

    def Plus1(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[3,None,-1]),([3,0],[3,1,'fin']),([3,1],[3,0,-1]),([3,None],[3,1,'fin'])]
        self.nombre=nombre
        

    def Moins1(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,0,1]),([2,1],[2,1,1]),([2,None],[3,None,-1]),([3,0],[3,1,-1]),([3,1],[3,0,'fin']),([3,None],[3,None,'fin'])]
        self.nombre=nombre
        

    def inversion(self,nombre):
        self.memoireInterne=[([1,None],[2,None,1]),([2,0],[2,1,1]),([2,1],[2,0,1]),([2,None],[2,None,'fin'])]
        self.nombre=nombre
        
        
    #compte et affiche le nombre de tours
    def compteur(self):
            self.frameCompteur.destroy()
            self.frameCompteur=tkinter.Frame(self.jeu)
            self.frameCompteur.place(x=200,y=150)
            if self.ruban[3][2]=="fin":
                reponse=[]
                for x in range(len(self.ruban)):
                    if type(self.ruban[x])==int:
                        reponse.append(self.ruban[x])
                self.reponse = ''.join(str(elem)for elem in reponse)
                reponse=self.binversdec()
                label_title=tkinter.Label(self.frameCompteur,text="fin, nombre après le calcul : "+str(reponse)+" en base 10",font=("Kokonor",20),bg="#EB9F1B",fg="black") 
            else:
                label_title=tkinter.Label(self.frameCompteur,text="chiffre lu : '" + str(self.ruban[self.tete[1]]) + "', position : " + str(self.tete[1]-8) + ", état : " + str(self.tete[0]) + " --> chiffre écrit : '" + str(self.ruban[3][1]) + "', position : " + str(self.tete[1]-8+self.ruban[3][2]) + ", état : " + str(self.ruban[3][0]),font=("Kokonor",20),bg="#EB9F1B",fg="black")#montre notre état, le chiffre lu et la position, et le futur de tout cela
            label_title.pack()
    
    #pour mettre sur le ruban
    def decversbin(self):
            base=2
            resultat=[]
            while self.nombre!=0:
                resultat.append(self.nombre%base)
                self.nombre=self.nombre//base
            resultat.reverse()
            return resultat
    
    #pour rendre en base 10 le résultat du calcul
    def binversdec(self):
        compteur=x=puissance=résultat=0
        nombreCaractère=len(str(self.reponse))#compte le nombre de caractère du nombre
        liste=list(str(self.reponse))#transforme un nombre compact en liste
        liste.reverse()#inverse les valeurs de la liste
        while compteur!=nombreCaractère:
            résultat=résultat+int(liste[x])*2**puissance
            compteur=compteur+1
            x=x+1
            puissance=puissance+1
        return résultat
    
    #quitte la fenêtre jeu et nous renvoie à la fenêtre menu
    def quitter(self):
        self.jeu.destroy()
        MenuVie=Menu()
        MenuVie.lancerMenu()

MenuVie=Menu()
MenuVie.lancerMenu()