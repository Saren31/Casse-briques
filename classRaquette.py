# coding: utf-8
class Raquette():    
    def __init__(self,posX,posY,largeur,hauteur):
        self._posX=posX #positionX de la raquette
        self._posY=posY #positionY de la raquette
        self._largeur=largeur #largeur de la raquette
        self._hauteur=hauteur #hauteur de la raquette
        self._image=loadImage("raquette.png") #image de la raquette
        self._coteDroit=posX+largeur/2 #position X du côté droit
        self._coteGauche=posX-largeur/2 #position X du coté gauche
        self._coteHaut=posY-hauteur/2 #position Y du coté haut
        self._coteBas=posY+hauteur/2 #position Y du côté bas
        self._vitesse=0 #vitesse de déplacement
        self._vitesseMax=10 #vitesse maximale de déplacement
        
    def dessine(self):
        #dessine l'image de la raquette à sa position centrées sur posX et posY car imageMode=CENTER
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
        
    
