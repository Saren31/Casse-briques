#Ne pas effacer cette instruction
from processing import *
#
#
"""version Bac A Sable"""
from random import * #pour mode BAC A SABLE

height=600
width=800

def setup():
    global balle,mur,raquette,etatJeu
    size(width,height)
    mur=creeTableau1()
    balle = Balle(width/2,height/2)
    raquette=Raquette(width/2,580,140,20)
    imageMode(CENTER)
    rectMode(CENTER)
    etatJeu=1

def draw():
    global balle,mur,raquette,etatJeu
    if etatJeu==1:
        dessinFond()
        balle.dessine()
        raquette.dessine()
        raquette.deplace(mouse.x)
        #processing normal raquette.deplace(mouseX)
        if(balle.rebonditContreMurs()==False):
            etatJeu=-1
        balle.rebonditContreRaquette(raquette)
        balle.deplace()
        for brique in mur:
            if balle.rebonditContreBrique(brique):
                brique._resistance=brique._resistance-1
    elif etatJeu==-1:
        ecranFinJeu()
                
def dessinFond():
    global mur
    #dessine le fond et les briques
    background(0)
    for brique in mur:
        brique.dessine()
        
def ecranFinJeu():
    textSize(50)
    text("FIN DE PARTIE",100,100)
        
def creeTableau1():
    # Si brique.png est dans le dossier data
    # imageBrique=loadImage("brique.png")
    # Sinon (bac a sable) on trace un rectangle de couleur
    imageBrique=None
    mur=[]
    largeur=70
    hauteur=20
    for j in range(5):
        for i in range(10):
            x=i*(largeur+5)+60
            y=j*(hauteur+2)+35
            brique=Brique(x,y,largeur,hauteur,1,imageBrique)
            mur.append(brique)
    return mur

#####################################################################
#########                                                   #########  
#########                                                   #########  
#########              CLASS BALLE                          #########  
#########                                                   #########  
#########                                                   #########  
#####################################################################


class Balle():
    def __init__(self,posX=50,posY=50,rayon=15,vitesseX=random()+4,vitesseY=random()*(-2)-3):
        self._posX=posX #position X de la balle
        self._posY=posY #position Y de la balle
        self._rayon=rayon # rayon de la balle
        self._vitesseX=vitesseX #vitesse horizontale de la balle
        self._vitesseY=vitesseY #vitesse verticale de la balle
        # seulement en processing installé
        # self._image=loadImage("balleBleue.png") #image de la balle
        # en mode Bac à Sable : on trace un cercle rouge
        self._image = None
        
    def dessine(self):
        #dessine l'image de la balle à sa position centrées sur posX et posY 
        #car imageMode=CENTER
        translate(self._posX,self._posY)
        if self._image != None:
            image(self._image,0,0,self._rayon*2,self._rayon*2)
        else:
            fill(255,0,0)
            ellipse(0,0,self._rayon*2,self._rayon*2)
        translate(-self._posX,-self._posY)

    def deplace(self):
        self._posX+=self._vitesseX
        self._posY+=self._vitesseY
    
    def rebonditContreMurs(self):
        if self._posX<0:
            self._vitesseX=abs(self._vitesseX)
        if self._posX>width:
            self._vitesseX=-abs(self._vitesseX)
        if self._posY<0:
            self._vitesseY=abs(self._vitesseY)
        if self._posY>width:
            return False

    def rebonditContreBrique(self,brique):
        #Une brique est touchée par la balle si la distance entre le centre de la balle
        #et un des cotés est inférieure au rayon de la balle
        #distanceDroite
        x=self._posX
        y=self._posY
        if brique._resistance<=0:
            return False
        distanceDroite=abs(brique._coteDroit-x)
        distanceHaut=abs(brique._coteHaut-y)
        distanceBas=abs(brique._coteBas-y)
        distanceGauche=abs(brique._coteGauche-x)
        if distanceDroite<=self._rayon and y>=brique._coteHaut and y<=brique._coteBas:
            #rebond vers la droite
            self._vitesseX=abs(self._vitesseX)
            return True
        if distanceGauche<=self._rayon and y>=brique._coteHaut and y<=brique._coteBas:
            #rebond vers la gauche
            self._vitesseX=-abs(self._vitesseX)
            return True
        if distanceBas<=self._rayon and x>=brique._coteGauche and x<=brique._coteDroit:
            #rebond vers le bas
            self._vitesseY=abs(self._vitesseY)
            return True
        if distanceHaut<=self._rayon and x>=brique._coteGauche and x<=brique._coteDroit:
            #rebond vers le haut
            self._vitesseY=-abs(self._vitesseY)
            return True
        return False
       
    def rebonditContreRaquette(self,raquette):
        x=self._posX
        y=self._posY
        if x>=raquette._coteGauche and x<=raquette._coteDroit:
            distanceHaut=abs(raquette._coteHaut-y)
            if distanceHaut<=self._rayon : 
                #rebond vers le haut
                self._vitesseY=-abs(self._vitesseY)
                return True
        return False
        
    def __str__(self):
        return str(int(self._posX))+","+str(int(self._posY))
            
   
#####################################################################
#########                                                   #########  
#########                                                   #########  
#########              CLASS BRIQUE                         #########  
#########                                                   #########  
#########                                                   #########  
#####################################################################

class Brique:
    def __init__(self,posX,posY,largeur,hauteur,resistance,imageBrique=None):
        self._posX=posX #position X de la brique
        self._posY=posY #position Y de la brique
        self._largeur=largeur #largeur de la brique
        self._hauteur=hauteur #hauteur de la brique
        self._resistance=resistance #nombre de coups avant disparition
        self._image=imageBrique #image de la brique
        self._coteGauche=posX-largeur/2 #position X du côté gauche
        self._coteDroit=posX+largeur/2 #position X du côté droit
        self._coteHaut=posY-hauteur/2 #position Y du côté haut
        self._coteBas=posY+hauteur/2 #position Y du côté bas
        
    def dessine(self):
        #dessine la brique sauf si sa résistance est nulle
        #à sa position centrées sur posX et posY car imageMode=CENTER
        translate(self._posX,self._posY)
        if self._resistance>0:
            if self._image==None:
                fill(0,0,255)
                rect(0,0,self._largeur,self._hauteur)
            else:
                image(self._image,0,0,self._largeur,self._hauteur)
        translate(-self._posX,-self._posY)
    
#####################################################################
#########                                                   #########  
#########                                                   #########  
#########              CLASS RAQUETTE                       #########  
#########                                                   #########  
#########                                                   #########  
#####################################################################


class Raquette():    
    def __init__(self,posX,posY,largeur,hauteur):
        self._posX=posX #positionX de la raquette
        self._posY=posY #positionY de la raquette
        self._largeur=largeur #largeur de la raquette
        self._hauteur=hauteur #hauteur de la raquette
        self._coteDroit=posX+largeur/2 #position X du côté droit
        self._coteGauche=posX-largeur/2 #position X du coté gauche
        self._coteHaut=posY-hauteur/2 #position Y du coté haut
        self._coteBas=posY+hauteur/2 #position Y du côté bas
        self._vitesse=0 #vitesse de déplacement
        self._vitesseMax=10 #vitesse maximale de déplacement
        #seulement en mode Processing normal
        #self._image=loadImage("raquette.png") #image de la raquette
        #en mode bac a sable on dessine un rectangle
        self._image = None
    def dessine(self):
        #dessine l'image de la raquette à sa position centrées sur posX et posY car imageMode=CENTER
        if self._image==None:
            fill(255)
            rect(self._posX,self._posY,self._largeur,self._hauteur)
        else:
            image(self._image,self._posX,self._posY,self._largeur,self._hauteur)
    
    def deplace(self,mouseX):
        #défini la vitesse de la raquette vers l'abscisse de la souris mouseX
        #et déplace la souris en fonction de sa vitesse
        self.setVitesse(mouseX)
        self._posX+=self._vitesse
        self._coteGauche=self._posX-self._largeur/2
        self._coteDroit=self._posX+self._largeur/2
        
    def setVitesse(self,mouseX):
        #la vitesse est proportionnelle à la distance de la souris, avec un max de 10
        v = (mouseX-self._posX)/20
        if v>self._vitesseMax:
            v=self._vitesseMax
        elif v<-self._vitesseMax:
            v=-self._vitesseMax
        self._vitesse=v
        
        
#####################################################################
#########                                                   #########  
#########                                                   #########  
#########              INSTRUCTIONS                         #########  
#########                                                   #########  
#########                                                   #########  
#####################################################################


"""

Vous pouvez mener à bien les tâches suivantes pour augmenter la note de votre projet

* ajouter un attribut couleur aux briques : 1 point
* ajouter plusieurs vies : 1 point
* faire exploser les briques lorsqu'elles ont touchées : 3 points
* faire des briques bonus qui permettent de jouer avec 3 balles en même temps : 5 point
* faire bouger les briques : 1 à 3 points
* proposer au moins 3 tableaux de jeu : 3 points
* proposer au moins 6 tableaux de jeu : 5 points
* faire une brique qui modifie la taille de la balle en + ou en - quand elle est touchée : 3 points
* faire une brique qui modifie la taille de la raquette si elle est touchée : 3 points
* rajouter du son : 1 à 4 points
* rajouter une mitrailleuse sur la raquette quand on atteint une certaine brique : 5 points
* faire une raquette collante, qui retient la balle une seconde : 3 points
* rajouter de la gravité qui attire la balle sur le côté ou vers le haut pendant un certain temps : 5 points
* multiplier le nombre de raquettes : 2 points
* rajouter un score et l'afficher : 2 points
* ajouter des briques indestructibles : 1 point
* modifier la direction du rebond en fonction de l'endroit de la raquette touché : 3 points
* permettre de cliquer à l'écran pour rajouter un point de gravité qui atteire la balle un certain temps : 4 points
* faire des briques "passage-secret" qui envoient la balle à un autre endroit quand elles sont touchées : 3 points
* faire des briques tournantes : 2 points
* faire un tableau d'accueil et de fin : 3 points
* ajouter une "trainée" à la balle : 2 points
* modifier la vitesse de la balle en fonction de divers événements : 2 points
* imaginer autre chose : de 1 à 10 points     """           


      
#toujours terminer par
#
run()
