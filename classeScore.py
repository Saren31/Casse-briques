class score() :
    def __init__(self,valeur) :
        self._score = valeur
        
    def afficherScore(self) :
        textSize(20)
        text(str(self._score),700,500)
        
    def ajouterScore(self,ajout,balle) :
        self._score += ajout
        textSize(20)
        text("+" + str(ajout),balle._posX,balle._posY)
        
    def retireScore(self,retrait,balle) :
        self._score -= retrait
        textSize(20)
        text("-" + str(retrait),balle._posX,balle._posY)
