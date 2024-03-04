class PowerUp() :
    def __init__(self,posX,type,vitesse):
        self._posX = posX
        self._posY = 0
        self._type = type
        self._vitesse = vitesse
        self._image = loadImage(type + '.png')
        self._rayon = 15
        
    def dessine(self) :
        image(self._image,self._posX,self._posY,self._rayon*2,self._rayon*2)
    
    def avance(self):
        self._posY += self._vitesse
        
    def rebonditContreRaquette(self,raquette):
        x=self._posX
        y=self._posY
        if x>=raquette._coteGauche and x<=raquette._coteDroit:
            distanceHaut=abs(raquette._coteHaut-y)
            if distanceHaut<=self._rayon : 
                return True
        return False
    
