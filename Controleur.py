from inspect import ClassFoundException
import os
from turtle import position
# from turtle import position
import keyboard
import time
import subprocess

from VueJeu import AireDeJeu 
from Modele import Daleks, Docteur, Matrix, TasDeFeraille




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
        for x in range(0, len(Daleks.positionOccupe)):   
            matrix.array[Daleks.positionOccupe[x]] = Daleks.VALEUR_DALEKS
            if daleks.positionOccupe[x] != 0:
                if daleks.compteur != 1:
                    matrix.array[Daleks.positionOccupeAncienne[x]] = 0
                    Daleks.positionOccupeAncienne[x] = Daleks.positionOccupe[x]
        daleks.compteur += 1


    def setTfPosition(self, matrix):
        for x in range(0, len(TasDeFeraille.positionTF)):      # on regarde toujours si il a des tas de feraille dans le tableau
            if 0 == len(TasDeFeraille.positionTF):
                break
            matrix.array[TasDeFeraille.positionTF[x]] = TasDeFeraille.VALEUR_TF
            
    def getPostionsDaleks(self):
        
        positionsComparaison = []
        for i in range(0, len(Daleks.positionOccupe)):
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
    
    def getPostionsDoc(self, doc):
        
        colomns = doc.positionDocActuellle
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
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - 1):
                    doc.positionDocActuellle -= 1 
                    success = True         
        
        elif keyboard.is_pressed("right arrow"):
            if doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + 1):
                    doc.positionDocActuellle += 1
                    success = True   
                
        elif keyboard.is_pressed("up arrow"):
            if doc.positionDocActuellle - Matrix.LONGUEUR >= 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - Matrix.LONGUEUR):
                    doc.positionDocActuellle -= Matrix.LONGUEUR 
                    success = True       
                
        elif keyboard.is_pressed("down arrow"):
            if doc.positionDocActuellle + Matrix.LONGUEUR <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + Matrix.LONGUEUR):
                    doc.positionDocActuellle += Matrix.LONGUEUR
                    success = True  

        elif keyboard.is_pressed("Home"):
            if (doc.positionDocActuellle - Matrix.LONGUEUR) - 1 >= 0 and doc.positionDocActuellle % Matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (Matrix.LONGUEUR + 1)):
                    doc.positionDocActuellle -=  Matrix.LONGUEUR + 1
                    success = True  

        elif keyboard.is_pressed("Page_Up"):
            if (doc.positionDocActuellle - Matrix.LONGUEUR) + 1 >= 0 and doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (Matrix.LONGUEUR - 1)):
                    doc.positionDocActuellle -=  Matrix.LONGUEUR - 1
                    success = True 

        elif keyboard.is_pressed("End"):
            if (doc.positionDocActuellle + Matrix.LONGUEUR) - 1 <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1 and doc.positionDocActuellle % Matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (Matrix.LONGUEUR - 1)):
                    doc.positionDocActuellle +=  Matrix.LONGUEUR - 1
                    success = True 

        elif keyboard.is_pressed("Page_Down"):
            if (doc.positionDocActuellle + Matrix.LONGUEUR) + 1 <= (Matrix.LONGUEUR * Matrix.LARGEUR) - 1 and doc.positionDocActuellle % Matrix.LONGUEUR != Matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (Matrix.LONGUEUR + 1)):
                    doc.positionDocActuellle +=  Matrix.LONGUEUR + 1
                    success = True 
        
        
        if success == True:
            positions.setDocPosition(matrix, doc)
            os.system('cls')
            adj.afficherMatrix(matrix)
            time.sleep(1) 
            if mouvement.verifierCollisionDoc_Dalek():      # verifie si le docteur va sur le dalek
                Matrix.gameOver = True
            mouvement.moveDalek(positions.getPostionsDaleks(), positions.getPostionsDoc(doc))
            if mouvement.verifierCollisionDoc_Dalek():      # verifie si le dalek va sur le docteur
                Matrix.gameOver = True

            # verifier s'il y a des collisions
                
           
                    
            mouvement.verifierCollisionDalek_Dalek()
            mouvement.verifierCollisionDalek_Tf()

            positions.setTfPosition(matrix)
            positions.setDalekPosition(matrix)  # code bug, erreur avec positionDalekAncienne 
            os.system('cls')
            adj.afficherMatrix(matrix)
            # print(positions.getPostionsDoc(doc)) #
            # print(doc.positionDocActuellle)
            time.sleep(0.2)      
            
            # cette methode est l'algorithme qui permet a chaque dalek de savoir dans quelle direction est le docteur
    def moveDalek(self, positionsDaleks, positionDoc):
        for i in range(0, len(Daleks.positionOccupe)): # multiplie par niveau
            if positionsDaleks[i][0] == positionDoc[0]:
                if positionsDaleks[i][1] > positionDoc[1]:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR     # en haut
                else:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR     # en bas
                    
            elif positionsDaleks[i][1] == positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] -= 1                   # gauche
                else:
                    Daleks.positionOccupe[i] += 1                   # droite
                    
            elif positionsDaleks[i][1] > positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR + 1 # en haut a gauche
                else:
                    Daleks.positionOccupe[i] -= Matrix.LONGUEUR - 1 # en haut a droite
                    
            elif positionsDaleks[i][1] < positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR - 1 # en bas a gauche
                else:
                    Daleks.positionOccupe[i] += Matrix.LONGUEUR + 1 # en bas a droite
            
    def verifierCollisionDalek_Dalek(self):

        # verifier les collision entre les daleks et les daleks

        daleks.positionOccupe.sort()
        daleks.positionOccupeAncienne.sort()
        nbrDeDaleks = len(daleks.positionOccupe) - 1   # - 1 car on regarde le dernier indice avec le i + 1 dans la condition du if
        
        i = 0
        while i < nbrDeDaleks:
            if daleks.positionOccupe[i] == daleks.positionOccupe[i + 1]:
                tf.positionTF.append(daleks.positionOccupe[i])
                daleks.positionOccupe.remove(daleks.positionOccupe[i + 1])
                daleks.positionOccupe.remove(daleks.positionOccupe[i])
                matrix.array[Daleks.positionOccupeAncienne[i + 1]] = 0
                matrix.array[Daleks.positionOccupeAncienne[i]] = 0
                daleks.positionOccupeAncienne.remove(daleks.positionOccupeAncienne[i + 1])
                daleks.positionOccupeAncienne.remove(daleks.positionOccupeAncienne[i])
                nbrDeDaleks =  len(daleks.positionOccupe) - 1
                i = 0
            else:
                i +=1

    def verifierCollisionDalek_Tf(self):

        nbrDeTf = len(tf.positionTF)
        nbrDeDaleks = len(daleks.positionOccupe)

        for i in range(0, nbrDeTf):
            x = 0
            while x < nbrDeDaleks:
                if daleks.positionOccupe[x] == tf.positionTF[i]:
                    daleks.positionOccupe.remove(daleks.positionOccupe[x])
                    matrix.array[Daleks.positionOccupeAncienne[x]] = 0
                    daleks.positionOccupeAncienne.remove(daleks.positionOccupeAncienne[x])
                    nbrDeDaleks = len(daleks.positionOccupe)
                    x=0
                else:
                    x+=1
                


    def verifierCollisionDoc_Dalek(self):
        nbrDeDaleks = len(daleks.positionOccupe)

        x = 0
        while x < nbrDeDaleks:
            if daleks.positionOccupe[x] == doc.positionDocActuellle:
                return True
            x += 1   
        return False
            
    # verifier les collisions entre les daleks et le docteur

    def verifierCollisionDoc_Tf(self, positionDocActuelle):
        for i in range(0, len(tf.positionTF)):
            if positionDocActuelle == tf.positionTF[i]:
                return False
        return True




# Objets de Controleur
mouvement = Mouvement()
positions = Positions()

# Objets de Modele
matrix = Matrix()
doc = Docteur()
daleks = Daleks()
tf = TasDeFeraille()

# Generer des positions aleatoires pour les daleks 
# daleks.genererDaleks()
positions.setDalekPosition(matrix)
positions.setTfPosition(matrix)



# Objets de VueJeu
adj = AireDeJeu()



os.system('cls')
adj.afficherMatrix(matrix)

print(positions.getPostionsDaleks())

while matrix.gameOver == False:
    mouvement.moveDoc(matrix, doc, adj)

print('Game Over') # test
    