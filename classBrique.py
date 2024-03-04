# coding: utf-8
class Brique:
    def __init__(self,posX,posY,largeur,hauteur,resistance,imageBrique=None,type = None):
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
        self._type = type
        
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
    
    
        
        
        
        
        
        
    
