import os
from turtle import position
import keyboard
import time
import subprocess

from VueJeu import AireDeJeu 
from Modele import Daleks, Docteur, Matrix


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
            
    def getPostionsDaleks(self):
        
        positionsComparaison = []
        for i in range(0, 5):
            colomns = Daleks.positionOccupe[i]
            ranges = 0
            tab = []
            
            while colomns >= Matrix.LONGUEUR:
                colomns -= Matrix.LONGUEUR
                ranges += 1
        
            tab.append(colomns)
            tab.append(ranges)
            positionsComparaison.append(tab)
        
        return positionsComparaison    
    
    def getPostionsDoc(self):
        
        colomns = Docteur.positionDocActuellle
        ranges = 0
        positionsComparaison = []
        
        while colomns >= Matrix.LONGUEUR:
            colomns -= Matrix.LONGUEUR
            ranges += 1
    
        positionsComparaison.append(colomns)
        positionsComparaison.append(ranges)
        
        return positionsComparaison
        
                
    
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
            
    def moveDalek(self, positionsDaleks, positionDoc):
        for i in range(0, 5): # multiplie par niveau
            if positionsDaleks[i][0] == positionDoc[0]:
                if positionsDaleks[i][1] > positionDoc[1]:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR
                else:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR
                    
            elif positionsDaleks[i][1] == positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] -= 1
                else:
                    Daleks.positionOccupe[i] += 1
                    
            elif positionsDaleks[i][1] > positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR + 1
                else:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR - 1
                    
            elif positionsDaleks[i][1] < positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR - 1
                else:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR + 1
            
            



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

print(positions.getPostionsDaleks())

while True:
    mouvement.moveDoc(matrix, doc, adj)
    mouvement.moveDalek(positions.getPostionsDaleks(), positions.getPostionsDoc())
    positions.setDalekPosition(matrix)
    