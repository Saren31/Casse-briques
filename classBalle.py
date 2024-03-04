# coding: utf-8
height=600
width=800
class Balle():
    def __init__(self,posX=50,posY=50,rayon=15,vitesseX=random(4,5),vitesseY=random(-3,-5)):
        self._posX=posX #position X de la balle
        self._posY=posY #position Y de la balle
        self._rayon=rayon # rayon de la balle
        self._vitesseX=vitesseX #vitesse horizontale de la balle
        self._vitesseY=vitesseY #vitesse verticale de la balle
        self._image=loadImage("balle.png") #image de la balle
    
    def dessine(self):
        #dessine l'image de la balle à sa position centrées sur posX et posY car imageMode=CENTER
        translate(self._posX,self._posY)
        image(self._image,0,0,self._rayon*2,self._rayon*2)
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
            if brique._type != "teleporteur" :
                self._vitesseX=abs(self._vitesseX)
            return True
        if distanceGauche<=self._rayon and y>=brique._coteHaut and y<=brique._coteBas:
            #rebond vers la gauche
            if brique._type != "teleporteur" :
                self._vitesseX=-abs(self._vitesseX)
            return True
        if distanceBas<=self._rayon and x>=brique._coteGauche and x<=brique._coteDroit:
            #rebond vers le bas
            if brique._type != "teleporteur" :
                self._vitesseY=abs(self._vitesseY)
            return True
        if distanceHaut<=self._rayon and x>=brique._coteGauche and x<=brique._coteDroit:
            #rebond vers le haut
            if brique._type != "teleporteur" :
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
   
        
