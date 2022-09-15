import os
import keyboard

from Modele import Docteur 
# Creer et initializer une liste de taille 6 x 8 a zero
        
class Matrix:
    
    longueur = 5
    largeur = 5

    # le constructeur
    def __init__(self, doc):
        
        self.matrix = list()
        for i in range(0, self.longueur * self.largeur):
            if i == doc.positionDocInitiale:
                self.matrix.append(doc.valeurDoc)
            else:
                self.matrix.append(0)
                
    def setDocPosition(self, doc):
        self.matrix[doc.positionDocActuellle] = doc.valeurDoc
        
    def annuleDocAnciennePosition(self, doc):
        self.matrix[doc.positionDocAncienne] = 0
        doc.positionDocAncienne = doc.positionDocActuellle
        

    # fonction afficher matrice
    def showMatrix(self):
        print(self.matrix)


class AireDeJeu: 
# adj pour 'aire de jeu'
    def __init__(self):
        self.ligne = Matrix.largeur

    def afficherMatrix(self, matrix):
        self.matriceDuJeu = matrix
        for i in range(0, Matrix.longueur * Matrix.largeur):
            # a chaque 8 valeur change de ligne
            if i % self.ligne == 0:
                print('\n')
            print(self.matriceDuJeu.matrix[i], end = ' ')
            
        print("\n")
            


class Mouvement:
    
    def __init__(self):
        pass
    
    def moveDoc(self, doc, matrix, adj):
        
        success = False
        if keyboard.is_pressed("left arrow"):
            if doc.positionDocActuellle % Matrix.longueur != 0:
                doc.positionDocActuellle -= 1 
                success = True         
        
        elif keyboard.is_pressed("right arrow"):
            if doc.positionDocActuellle % Matrix.longueur != Matrix.longueur - 1:
                doc.positionDocActuellle += 1
                success = True   
                
        elif keyboard.is_pressed("up arrow"):
            if doc.positionDocActuellle - Matrix.longueur >= 0:
                doc.positionDocActuellle -= Matrix.longueur 
                success = True       
                
        elif keyboard.is_pressed("down arrow"):
            if doc.positionDocActuellle + Matrix.longueur <= (Matrix.longueur * Matrix.largeur) - 1:
                doc.positionDocActuellle += Matrix.longueur
                success = True   
        
        
        if success == True:
            matrix.setDocPosition(doc)
            matrix.annuleDocAnciennePosition(doc)
            os.system('cls')
            adj.afficherMatrix(matrix)
                
                
os.system('cls')          

doc = Docteur()

matrix = Matrix(doc) # creer une vairable matrice
adj = AireDeJeu() # afficher cette variable
adj.afficherMatrix(matrix)

move = Mouvement()

while 1 > 0:
    
    move.moveDoc(doc, matrix, adj)