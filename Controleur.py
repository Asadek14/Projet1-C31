import os
from turtle import position
import keyboard
import time
import random

from VueJeu import AireDeJeu 
from Modele import Daleks, Docteur, Matrix

#Cette classe va s'occuper de la teleportation du docteur a une cordonnée aléatoire, selon le mode de jeu choisi par l'utilisateur
class Teleporteur:
    def __init__(self, modeJeu):      
        self.modeJeu = modeJeu

    def teleportation(self):
        while True:
                if keyboard.is_pressed('T'): #si on appuie la touche T
                    if self.modeJeu == "F": # Facile
                        self.tpModeJeuF(); break
                    elif self.modeJeu == "M": # Moyen
                        self.tpModeJeuM(); break
                    elif self.modeJeu == "D": # Difficile
                        self.tpModeJeuD(); break
    #methode pour teleportation mode de jeu Facile            
    def tpModeJeuF(self):
        while True:
            positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1) #generation position aleatoire pour TP

            for i in daleks.positionOccupe[i]:#for pour passer dans toutes les positions des daleks selon le niveau (5, 10, 15, etc)
                if positionTP == daleks.positionOccupe[i]:#si la position du TP est la meme que celle occupé par un dalek, refaire la generation position aléatoire
                    continue
                elif positionTP == daleks.positionOccupe[i-2]:#si la position est a une distance d'au moins deux cases, retourner la position
                    return positionTP
            break
    #methode pour teleportaton mode de jeu moyen        
    def tpModeJeuM(self):
        while True:
            positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)

            for i in daleks.positionOccupe[i]:
                if positionTP == daleks.positionOccupe[i]:
                    continue
                else:
                    return positionTP
            break
    #methode pour teleportation mode de jeu difficile        
    def tpModeJeuD(self):
        positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)
        return positionTP

                    
# Cette classe va s'occuper de setter les postions de Docteur/Daleks/TasDeFerailles recu par la classe Mouvement
class Positions: 
    

    def __init__(self):
        pass         
                

    def setDocPosition(self, matrix, doc):
        matrix.array[doc.positionDocActuellle] = Docteur.VALEUR_DOC
        matrix.array[doc.positionDocAncienne] = 0
        doc.positionDocAncienne = doc.positionDocActuellle


    def setDocPositionInitiale(self, matrix, doc):
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != Docteur.POSITION_DOC_INITIALE:
                matrix.array[i] = 0
            else:
                matrix.array[i] = Docteur.VALEUR_DOC


    def setDalekPosition(self, matrix):
        for x in range(0, 5):
            matrix.array[Daleks.positionOccupe[x]] = Daleks.VALEUR_DALEKS
    
    
# Cette classe va s'occuper de bouger les characteres de jeu (Docteur/Daleks/TasDeFerailles) dans la matrice si les conditions sont valides
class Mouvement:
    
    def __init__(self):
        pass
    
    def moveDoc(self, matrix, doc, adj):
        
        success = False
        if keyboard.is_pressed("left arrow"):
            if doc.positionDocActuellle % Matrix.LONGUEUR != 0:
                doc.positionDocActuellle -= 1 
                success = True         
        
        elif keyboard.is_pressed("right arrow"):
            if doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                doc.positionDocActuellle += 1
                success = True   
                
        elif keyboard.is_pressed("up arrow"):
            if doc.positionDocActuellle - Matrix.LONGUEUR >= 0:
                doc.positionDocActuellle -= Matrix.LONGUEUR 
                success = True       
                
        elif keyboard.is_pressed("down arrow"):
            if doc.positionDocActuellle + Matrix.LONGUEUR <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1:
                doc.positionDocActuellle += Matrix.LONGUEUR
                success = True  

        elif keyboard.is_pressed("Home"):
            if (doc.positionDocActuellle - Matrix.LONGUEUR) - 1 >= 0 and doc.positionDocActuellle % Matrix.LONGUEUR != 0:
                doc.positionDocActuellle -=  Matrix.LONGUEUR + 1
                success = True  

        elif keyboard.is_pressed("Page_Up"):
            if (doc.positionDocActuellle - Matrix.LONGUEUR) + 1 >= 0 and doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                doc.positionDocActuellle -=  Matrix.LONGUEUR - 1
                success = True 

        elif keyboard.is_pressed("End"):
            if (doc.positionDocActuellle + Matrix.LONGUEUR) - 1 <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1 and doc.positionDocActuellle % Matrix.LONGUEUR != 0:
                doc.positionDocActuellle +=  Matrix.LONGUEUR - 1
                success = True 

        elif keyboard.is_pressed("Page_Down"):
            if (doc.positionDocActuellle + Matrix.LONGUEUR) + 1 <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1 and doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                doc.positionDocActuellle +=  Matrix.LONGUEUR + 1
                success = True 
        
        
        if success == True:
            positions.setDocPosition(matrix, doc)
            os.system('cls')
            adj.afficherMatrix(matrix)
            time.sleep(0.20)      



# Objets de Controleur
mouvement = Mouvement()
positions = Positions()

# Objets de Modele
matrix = Matrix()
doc = Docteur()
daleks = Daleks()

# Generer des positions aleatoires pour les daleks 
daleks.genererDaleks()
positions.setDalekPosition(matrix)


# Objets de VueJeu
adj = AireDeJeu()

os.system('cls')
adj.afficherMatrix(matrix)

while True:
    mouvement.moveDoc(matrix, doc, adj)