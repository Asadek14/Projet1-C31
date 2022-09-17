import os
import keyboard

from VueJeu import AireDeJeu 
from Modele import Docteur, Matrix


# Cette classe va s'occuper de setter les postions de Docteur/Daleks/TasDeFerailles recu par la classe Mouvement
class Postions: 
    
    def __init__(self):
        pass         
                
    def setDocPosition(self, matrix, doc):
        matrix.matrix[doc.positionDocActuellle] = Docteur.VALEUR_DOC
        matrix.matrix[doc.positionDocAncienne] = 0
        doc.positionDocAncienne = doc.positionDocActuellle
        
    def setDalekPosition(self, matrix, dalek):
        pass
    
    
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
            if doc.positionDocActuellle + Matrix.LONGUEUR <= (Matrix.LONGUEUR * Matrix.LONGUEUR) - 1:
                doc.positionDocActuellle += Matrix.LONGUEUR
                success = True   
        
        
        if success == True:
            positions.setDocPosition(matrix, doc)
            os.system('cls')
            adj.afficherMatrix(matrix)       



# Objets de Controleur
mouvement = Mouvement()
positions = Postions()

# Objets de Modele
matrix = Matrix()
doc = Docteur()

# Objets de VueJeu
adj = AireDeJeu()

adj.afficherMatrix(matrix)

while True:
    mouvement.moveDoc(matrix, doc, adj)