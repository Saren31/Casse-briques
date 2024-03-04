from classBalle import *
from classBrique import *
from classRaquette import *
from classeScore import *
from classePowerUp import *

from random import *
add_library('minim')
#il faut importer la librairie minim sur processing

height=600
width=800

def setup():
    global listeBalles,mur1, mur2, mur3, mur4, mur5, mur6, mur7,raquette,etatJeu,score,powerUp,kick, bounce, explosion, casse, death, tp, iron, win, state, oldmur, difficulty, vie, powerup
    size(width,height)
    mur1 = creeTableauAlea()
    mur2 = creerTableauNiveau(1)
    mur3 = creerTableauNiveau(2)
    mur4 = creerTableauNiveau(3)
    mur5 = creerTableauNiveau(4)
    mur6 = creerTableauNiveau(5)
    mur7 = creerTableauNiveau(6)
    #les six niveaux du mode aventure et le niveau aléatoire sont générés
    listeBalles = []
    listeBalles.append(Balle(400,550))
    raquette=Raquette(width/2,580,140,20)
    #la raquette et la première balle sont générés
    powerUp = []
    imageMode(CENTER)
    rectMode(CENTER)
    score = score(0)
    etatJeu=1
    kick = Minim(this).loadSample("mur_detruit.mp3")
    bounce = Minim(this).loadSample("raquette_snd.mp3")
    explosion = Minim(this).loadSample("explosion.mp3")
    casse = Minim(this).loadSample("mur_casse.mp3")
    death = Minim(this).loadSample("death.mp3")
    tp = Minim(this).loadSample("tp.mp3")
    iron = Minim(this).loadSample("iron.mp3")
    win = Minim(this).loadSample("win.mp3")
    powerup = Minim(this).loadSample("powerup.mp3")
    #tous les sons du casse brique sont importés, ils seront activés avec un "son".trigger()
    state = "menud"
    #le jeu commence par défaut en mode difficile
    vie = 0

def draw():
    global listeBalles,mur,raquette,etatJeu,score,powerUp, oldmur, difficulty, mur, vie
    #il y a 3 menus différents en fonction du nombre de points de vie
    if state == "menud":
        background(0)
        noFill()
        textAlign(CENTER, CENTER)
        textSize(26)
        stroke(255)
        rect(width/2, height/3, width/4, height/6)
        text("AVENTURE",width/2,height/3)
        rect(width/2,height/2,width/4,height/6)
        text("CLASSIQUE", width/2,height/2)
        #les "graphismes" du premier menu sont crées
        rect(100, 550, 200, 100)
        text("DIFFICILE",100,550)
    elif state == "menun":
        background(0)
        noFill()
        textAlign(CENTER, CENTER)
        textSize(26)
        stroke(255)
        rect(width/2, height/3, width/4, height/6)
        text("AVENTURE",width/2,height/3)
        rect(width/2,height/2,width/4,height/6)
        text("CLASSIQUE", width/2,height/2)
        #les "graphismes" du premier menu sont crées
        rect(100, 550, 200, 100)
        text("NORMAL",100,550)
    elif state == "menuf":
        background(0)
        noFill()
        textAlign(CENTER, CENTER)
        textSize(26)
        stroke(255)
        rect(width/2, height/3, width/4, height/6)
        text("AVENTURE",width/2,height/3)
        rect(width/2,height/2,width/4,height/6)
        text("CLASSIQUE", width/2,height/2)
        #les "graphismes" du premier menu sont crées
        rect(100, 550, 200, 100)
        text("FACILE",100,550)
    elif state == "aventure":
        background(0)
        noFill()
        textAlign(CENTER, CENTER)
        textSize(26)
        stroke(255)
        rect(width/2, 50, width/4, height/6)
        text("NIVEAU 1",width/2,50)
        rect(width/2,150,width/4, height/6)
        text("NIVEAU 2", width/2,150)
        rect(width/2, 250,width/4, height/6)
        text("NIVEAU 3",width/2,250)
        rect(width/2,350,width/4, height/6)
        text("NIVEAU 4", width/2,350)
        rect(width/2, 450,width/4, height/6)
        text("NIVEAU 5",width/2,450)
        rect(width/2,550,width/4, height/6)
        text("NIVEAU 6", width/2,550)
        #les graphismes du second menu (obtenu si on clique sur aventure) sont crées
    elif etatJeu==-1:
        #si le jeu est terminé, on vérifie si le joueur a gagné ou perdu pour lui afficher l'écran correspondant
        if testVictoire(mur) == False :
            ecranVictoire()
        else :
            ecranFinJeu()
    else:   
        #définit quel mur est utilisé en fonction du niveau choisi
        if state == "niveau1" and etatJeu == 1:
            mur = mur2
        if state =="niveau2" and etatJeu ==1:
            mur = mur3
        if state =="niveau3" and etatJeu ==1:
            mur = mur4
        if state =="niveau4" and etatJeu ==1:
            mur = mur5
        if state =="niveau5" and etatJeu ==1:
            mur = mur6
        if state =="niveau6" and etatJeu ==1:
            mur = mur7
        if state == "classique" and etatJeu == 1:
            mur = mur1
        dessinFond()
        score.afficherScore()
        for balle in listeBalles :
            balle.dessine()
        if powerUp == [] :
            #un bonus est envoyé si un x est égal à une certaine valeur
            x = randint(0,1000)
            if x == 25 :
                powerUp.append(PowerUp(randint(0,800),"bonusBalle",randint(5,10)))
            if x == 75 :
                powerUp.append(PowerUp(randint(0,800),"bonusTailleRaquette",randint(5,10)))
        else :
            powerUp[0].dessine()
            powerUp[0].avance()
            if powerUp[0].rebonditContreRaquette(raquette) == True :
                powerup.trigger()
                #si un bonus est touché par la raquette, des effets ont lieu en fonction du type du bonus
                if powerUp[0]._type == "bonusBalle" :
                    listeBalles.append(Balle(400,550))
                else :
                    raquette._largeur += 10
                del powerUp[0]
            elif powerUp[0]._posY > height :
                #si le bonus passe en dessous de l'écran, il est supprimé
                del powerUp[0]
        raquette.dessine()
        raquette.deplace(mouseX)
        for balle in listeBalles :
            if(balle.rebonditContreMurs()==False):
                #si la balle n'est plus dans l'écran, elle est supprimée
                listeBalles.remove(balle)
                if listeBalles == [] and vie == 0:
                    #si il ne reste plus de balle, le joueur perd la partie
                    etatJeu=-1
                    death.trigger()
                elif listeBalles == [] and vie != 0:
                    #si on le joueur n'a plus de balle sur le terrain mais qu'il lui reste une vie alors une nouvelle balle apparaît
                    listeBalles.append(Balle(400,550))
                    vie -= 1
                    
        if testVictoire(mur) == False :
            win.trigger()
            etatJeu=-1
        for balle in listeBalles :
            balle.rebonditContreRaquette(raquette)
            balle.deplace()
            if balle.rebonditContreRaquette(raquette) == True:
                bounce.trigger()
            for brique in mur:
                #détermine la réaction de la brique après avoir été touchée par la balle en fonction du type de la brique
                if balle.rebonditContreBrique(brique):
                    if brique._type == "indestructible":
                        iron.trigger()
                    if brique._type == "teleporteur" or brique._type == "teleporteurSecret" :
                        tp.trigger()
                        if brique._type == "teleporteurSecret" :
                            #si un téléporteur secret est découvert, l'image du téléporteur change
                            brique._image = loadImage("briqueTeleporteur.png")
                        for brique2 in mur :
                            if (brique2._type == "recepteur") or (brique2._type == "recepteurSecret")  :
                                balle._posX = brique2._posX
                                balle._posY = brique2._posY
                    if brique._type == "bombe" :
                        #les 4 briques à côté de la bombe (ainsi que la bombe) sont supprimées
                        try :
                            if mur[mur.index(brique) + 1]._type != "teleporteur" and mur[mur.index(brique) - 1]._type != "recepteur" : 
                                mur[mur.index(brique) + 1]._resistance = 0
                        except :
                            pass
                        try :
                            if mur[mur.index(brique) - 1]._type != "teleporteur" and mur[mur.index(brique) - 1]._type != "recepteur" :
                                mur[mur.index(brique) - 1]._resistance = 0
                        except :
                            pass
                        try :
                            if mur[mur.index(brique) + 10]._type != "teleporteur" and mur[mur.index(brique) - 1]._type != "recepteur" :
                                mur[mur.index(brique) + 10]._resistance = 0
                        except :
                            pass
                        try :
                            if mur[mur.index(brique) - 10]._type != "teleporteur" and mur[mur.index(brique) - 1]._type != "recepteur" :
                                mur[mur.index(brique) - 10]._resistance = 0
                        except :
                            pass                         
                        brique._resistance = brique._resistance-1
                        score.ajouterScore(5,balle)
                        explosion.trigger()
                    if brique._type == "recepteurSecret" :
                        #quand on touche un recepteur secret, il devient visible
                        brique._image = loadImage("briqueRecepteur.png")
                    if brique._type == None :
                        #cas de base
                        brique._resistance = brique._resistance-1
                        if brique._resistance == 0 :
                            score.ajouterScore(2,balle)
                            kick.trigger()
                        else :
                            score.ajouterScore(1,balle)
                            casse.trigger()
    
                            
                        
    
    

                
    
def dessinFond():
    #la fonction charge l'image des briques en fonction de leur résistance
    global mur
    imageBrique1=loadImage("brique1.png")
    imageBrique2=loadImage("brique2.png")
    imageBrique3=loadImage("brique3.png")
    background(0)
    for brique in mur:
        if brique._type == None :
            if brique._resistance == 1 :
                brique._image = imageBrique1
            elif brique._resistance == 2 :
                brique._image = imageBrique2
            elif brique._resistance == 3 :
                brique._image = imageBrique3
        brique.dessine()
        
def testVictoire(mur):
    #la fonction vérifie si la partie a été gagnée par le joueur
    verif = False
    for brique in mur :
        if brique._resistance > 0 :
            if (brique._type == None) or (brique._type == "bombe") :
                verif = True
    return(verif)
    
        
def ecranFinJeu():
    #la partie est perdue
    textSize(50)
    text("FIN DE PARTIE",width/2,300)
    
    
def ecranVictoire():
    #la partie est gagnée
    textSize(50)
    text("VICTOIRE",width/2,300)

    
def creerTableauNiveau(niveau):
    #la fonction crée les niveaux du mode aventure
    imageBrique1=loadImage("brique1.png")
    imageBrique2=loadImage("brique2.png")
    imageBrique3=loadImage("brique3.png")
    imageBriqueIndestructible = loadImage("briqueIndestructible.png")
    imageBriqueBombe = loadImage("briqueBombe.png")
    imageBriqueSecrete = loadImage("briqueSecrete.png")
    longueur = 0
    if niveau == 1:
        longueur = 7
        brick = [(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),
                (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),
                (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),
                (3, imageBrique3, None), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),
                (2, imageBrique2, None), (3, imageBrique3, None), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),
                (1, imageBrique1, None),(2, imageBrique2, None), (3, imageBrique3, None), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueBombe,"bombe"),
                (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None), (3, imageBrique3, None), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(2, imageBrique2, None),(3, imageBrique3, None),(1,imageBriqueIndestructible,"indestructible")]
    if niveau == 2:
        longueur = 7
        brick = [(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),
                (1, imageBrique1, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(1, imageBrique1, None),
               (1, imageBrique1, None), (2, imageBrique2, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(2, imageBrique2, None),(1, imageBrique1, None),
               (1, imageBrique1, None), (2, imageBrique2, None), (3, imageBrique3, None),(1,imageBriqueSecrete,"teleporteurSecret"),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueSecrete, "recepteurSecret"),(3, imageBrique3, None),(2, imageBrique2, None),(1, imageBrique1, None),
              (1, imageBrique1, None), (2, imageBrique2, None), (3, imageBrique3, None), (3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(2, imageBrique2, None),(1, imageBrique1, None),
                (1, imageBrique1, None),(2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(1, imageBrique1, None),
                (1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None)]
    if niveau == 3:
        longueur = 7
        brick = [(0, None, None),(1,imageBriqueBombe,"bombe"),(3, imageBrique3, None),(1, imageBrique1, None),(1, imageBrique1, None),(1,imageBriqueSecrete, "recepteurSecret"),(1, imageBrique1, None),(3, imageBrique3, None),(1,imageBriqueBombe,"bombe"),(0, None, None),
                (0, None, None),(1,imageBriqueBombe,"bombe"),(3, imageBrique3, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(3, imageBrique3, None),(1,imageBriqueBombe,"bombe"),(0, None, None),
                (0, None, None), (1,imageBriqueBombe,"bombe"),(3, imageBrique3, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(3, imageBrique3, None),(1,imageBriqueBombe,"bombe"),(0, None, None),
                (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"),
                (2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None), (3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),
                (1, imageBrique1, None),(2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None), (3, imageBrique3, None),(1,imageBriqueSecrete,"teleporteurSecret"),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(1, imageBrique1, None),
                (1, imageBrique1, None),(1, imageBrique1, None),(2, imageBrique2, None), (3, imageBrique3, None),(1, imageBrique1, None), (1, imageBrique1, None),(3, imageBrique3, None),(2, imageBrique2, None),(1, imageBrique1, None),(1, imageBrique1, None)]
    if niveau == 4:
        longueur = 8
        brick = [(1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None),(1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None),
                 (1, imageBrique1, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (1, imageBrique1, None),
               (1, imageBrique1, None), (0, None, None), (0, None, None), (3, imageBrique3, None), (3, imageBrique3, None), (3, imageBrique3, None),(3, imageBrique3, None), (0, None, None), (0, None, None), (1, imageBrique1, None),
                 (1, imageBrique1, None), (0, None, None), (3, imageBrique3, None), (2, imageBrique2, None), (1,imageBriqueBombe,"bombe"), (1, imageBrique1, None), (2, imageBrique2, None), (3, imageBrique3, None), (0, None, None), (1, imageBrique1, None),
                 (1, imageBrique1, None), (0, None, None), (3, imageBrique3, None), (2, imageBrique2, None), (1, imageBrique1, None), (1,imageBriqueBombe,"bombe"), (2, imageBrique2, None), (3, imageBrique3, None), (0, None, None), (1, imageBrique1, None),
               (1, imageBrique1, None), (0, None, None), (0, None, None), (3, imageBrique3, None), (3, imageBrique3, None), (3, imageBrique3, None), (3, imageBrique3, None), (0, None, None), (0, None, None), (1, imageBrique1, None),
                 (1, imageBrique1, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (1, imageBrique1, None),
               (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None),(1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None), (1, imageBrique1, None)]
                 

    if niveau == 5:
         longueur = 10
         brick = [(0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None),
                  (0, None, None), (0, None, None),(1, imageBrique1, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(0, None, None),(1, imageBrique1, None), (1, imageBrique1, None),(0, None, None),
                  (0, None, None),(1, imageBrique1, None),(1,imageBriqueBombe,"bombe"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(1,imageBriqueBombe,"bombe"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),
                  (0, None, None), (1, imageBrique1, None),(3, imageBrique3, None),(1,imageBriqueSecrete,"teleporteurSecret"),(1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(1,imageBriqueSecrete, "recepteurSecret"),(3, imageBrique3, None),(1, imageBrique1, None),
                  (0, None, None), (1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),
                  (0, None, None), (1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),
                  (0, None, None), (1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),(1, imageBrique1, None),
                  (0, None, None), (2, imageBrique2, None), (0, None, None), (0, None, None),(2, imageBrique2, None),(0, None, None), (2, imageBrique2, None),(0, None, None), (0, None, None),(2, imageBrique2, None),
                  (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None), (0, None, None),
                 (1, imageBrique1, None), (1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"), (1,imageBriqueIndestructible,"indestructible"), (1, imageBrique1, None)]
    if niveau == 6:
        longueur = 15
        brick = [(0, None, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(0, None, None),
                (0, None, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(1,imageBriqueBombe,"bombe"),(1,imageBriqueBombe,"bombe"),(1, imageBrique1, None),(0, None, None),(0, None, None),(0, None, None),
                (0, None, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(0, None, None),
                (0, None, None),(1, imageBrique1, None),(0, None, None),(0, None, None),(2, imageBrique2, None),(2, imageBrique2, None),(0, None, None),(0, None, None),(1, imageBrique1, None),(0, None, None),
                (0, None, None), (0, None, None), (1, imageBrique1, None), (2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(1, imageBrique1, None),(0, None, None),(0, None, None),
                (0, None, None), (0, None, None),  (0, None, None), (3, imageBrique3, None), (3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None), (0, None, None), (0, None, None), (0, None, None),
                 (0, None, None),(1, imageBrique1, None),  (0, None, None),   (0, None, None),(3, imageBrique3, None), (3, imageBrique3, None),  (0, None, None),  (0, None, None),(1, imageBrique1, None),  (0, None, None),
                 (1, imageBrique1, None),(0, None, None),(1, imageBrique1, None),(0, None, None),(2, imageBrique2, None),(2, imageBrique2, None),(0, None, None),(1, imageBrique1, None), (0, None, None),(1, imageBrique1, None),
                 (1, imageBrique1, None),(0, None, None),(0, None, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(0, None, None),(0, None, None),(1, imageBrique1, None),
                (0, None, None), (0, None, None),(1, imageBrique1, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(1, imageBrique1, None),(0, None, None),(0, None, None),
                (0, None, None),(1, imageBrique1, None), (3, imageBrique3, None), (3, imageBrique3, None), (3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(1, imageBrique1, None), (0, None, None),
                (1, imageBrique1, None),(0, None, None), (2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(0, None, None),(1, imageBrique1, None),
                (1, imageBrique1, None),(0, None, None), (2, imageBrique2, None), (2, imageBrique2, None), (2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(2, imageBrique2, None),(0, None, None),(1, imageBrique1, None),
                (0, None, None),(1, imageBrique1, None),(0, None, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(3, imageBrique3, None),(0, None, None),(1, imageBrique1, None),(0, None, None),
                (0, None, None),(0, None, None),(1, imageBrique1, None), (0, None, None),(1,imageBriqueIndestructible,"indestructible"),(1,imageBriqueIndestructible,"indestructible"),(0, None, None),(1, imageBrique1, None),(0, None, None),(0, None, None)]
    mur=[]
    largeur=70
    hauteur=20
    g = 0
    for j in range(longueur):
        for i in range(10):        
            #chaque rangée fait 10 briques
            x=i*(largeur+5)+60
            y=j*(hauteur+2)+35
            resistance,imageBrique, type = brick[g]
            brique = Brique(x, y, largeur, hauteur, resistance, imageBrique, type)
            print(brique)
            g+=1
            mur.append(brique)
    return mur
    
        
def creeTableauAlea():
    #la fonction crée un niveau aléatoire
    imageBrique1=loadImage("brique1.png")
    imageBrique2=loadImage("brique2.png")
    imageBrique3=loadImage("brique3.png")
    imageBriqueIndestructible = loadImage("briqueIndestructible.png")
    imageBriqueBombe = loadImage("briqueBombe.png")
    imageBriqueSecrete = loadImage("briqueSecrete.png")
    mur=[]
    largeur=70
    hauteur=20
    for j in range(randint(5,8)):
        for i in range(10):
            x=i*(largeur+5)+60
            y=j*(hauteur+2)+35
            alea = randint(0,100)
            if alea < 90 :
                if alea < 45 :
                    brique = Brique(x,y,largeur,hauteur,1,imageBrique1)
                elif alea < 75 :
                    brique = Brique(x,y,largeur,hauteur,2,imageBrique2)
                else :
                    brique = Brique(x,y,largeur,hauteur,3,imageBrique3)
            elif alea < 98 :
                brique=Brique(x,y,largeur,hauteur,1,imageBriqueBombe,"bombe")
            else :
                brique=Brique(x,y,largeur,hauteur,1,imageBriqueIndestructible,"indestructible")
            mur.append(brique)
    alea1 = randint(0,len(mur)-1)
    alea2 = alea1
    while alea2 == alea1 :
        alea2 = randint(0,len(mur)-1)
    mur[alea1]._image = imageBriqueSecrete
    mur[alea2]._image = imageBriqueSecrete
    mur[alea1]._type = "teleporteurSecret"
    mur[alea2]._type = "recepteurSecret"
    return mur


def mousePressed():
    #la fonction permet une réaction du jeu à chaque fois qu'on clique sur un bouton
    global state, etatJeu, difficulty, vie
    if state == "menud":
        if ((mouseX>300) and (mouseY>250) and (mouseX<500) and (mouseY<350)):
            state = "classique"
            etatJeu = 1
        if ((mouseX>300) and (mouseY>150) and (mouseX<500) and (mouseY<250)):
            state = "aventure"
        if ((mouseX>0) and (mouseY>450) and (mouseX<200) and (mouseY<550)):
            state = "menun"
            vie = 1
    elif state == "menun":
        if ((mouseX>300) and (mouseY>250) and (mouseX<500) and (mouseY<350)):
            state = "classique"
            etatJeu = 1
        if ((mouseX>300) and (mouseY>150) and (mouseX<500) and (mouseY<250)):
            state = "aventure"
        if ((mouseX>0) and (mouseY>450) and (mouseX<200) and (mouseY<550)):
            state = "menuf"
            vie = 2
    elif state == "menuf":
        if ((mouseX>300) and (mouseY>250) and (mouseX<500) and (mouseY<350)):
            state = "classique"
            etatJeu = 1
        if ((mouseX>300) and (mouseY>150) and (mouseX<500) and (mouseY<250)):
            state = "aventure"
        if ((mouseX>0) and (mouseY>450) and (mouseX<200) and (mouseY<550)):
            state = "menud"
            vie = 0
                
    elif state == "aventure":
         if ((mouseX>300) and (mouseY>0) and (mouseX<500) and (mouseY<100)):
            state = "niveau1"
            etatJeu = 1
         if ((mouseX>300) and (mouseY>100) and (mouseX<500) and (mouseY<200)):
            state = "niveau2"
            etatJeu = 1
         if ((mouseX>300) and (mouseY>200) and (mouseX<500) and (mouseY<300)):
            state = "niveau3"
            etatJeu = 1
         if ((mouseX>300) and (mouseY>300) and (mouseX<500) and (mouseY<400)):
            state = "niveau4"
            etatJeu = 1
         if ((mouseX>300) and (mouseY>400) and (mouseX<500) and (mouseY<500)):
            state = "niveau5"
            etatJeu = 1
         if ((mouseX>300) and (mouseY>500) and (mouseX<500) and (mouseY<600)):
            state = "niveau6"
            etatJeu = 1
    

        
