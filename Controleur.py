from importlib.resources import path
from inspect import ClassFoundException
from operator import truediv
import os
from turtle import position
from unittest.util import sorted_list_difference
# from turtle import position

os.system("pip install keyboard")
os.system('cls')

import keyboard
import time
import subprocess
import csv
from VueJeu import AireDeJeu,VueMenu 
from Modele import Daleks, Docteur, Matrix, NbZappeurs, Niveau, TasDeFeraille, Pointage
import random

class Zappeur:
    def __init__(self):
        pass
    
    def zappeur(self, matrix, doc, daleks):
         
            if doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - 1):
                    if doc.positionDocActuellle - 1 in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle - 1)]
                        daleks.positionOccupe.remove(doc.positionDocActuellle - 1)
                    matrix.array[doc.positionDocActuellle - 1] = 0
       
        
            if doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + 1):
                    if doc.positionDocActuellle + 1 in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle + 1)]
                        daleks.positionOccupe.remove(doc.positionDocActuellle + 1)
                    matrix.array[doc.positionDocActuellle + 1] = 0
 
                
            if doc.positionDocActuellle - matrix.LONGUEUR >= 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - matrix.LONGUEUR):
                    if doc.positionDocActuellle - matrix.LONGUEUR in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle - matrix.LONGUEUR)]
                        daleks.positionOccupe.remove(doc.positionDocActuellle - matrix.LONGUEUR)
                    matrix.array[doc.positionDocActuellle - matrix.LONGUEUR] = 0
    
                
            if doc.positionDocActuellle + matrix.LONGUEUR <= (matrix.LONGUEUR * matrix.LARGEUR) - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + matrix.LONGUEUR):
                    if doc.positionDocActuellle + matrix.LONGUEUR in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle + matrix.LONGUEUR)]
                        daleks.positionOccupe.remove(doc.positionDocActuellle + matrix.LONGUEUR)
                    matrix.array[doc.positionDocActuellle + matrix.LONGUEUR] = 0
                    

            if (doc.positionDocActuellle - matrix.LONGUEUR) - 1 >= 0 and doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (matrix.LONGUEUR + 1)):
                    if doc.positionDocActuellle -  (matrix.LONGUEUR + 1) in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle -  (matrix.LONGUEUR + 1))]
                        daleks.positionOccupe.remove(doc.positionDocActuellle -  (matrix.LONGUEUR + 1))
                    matrix.array[doc.positionDocActuellle -  (matrix.LONGUEUR + 1)] = 0


            if (doc.positionDocActuellle - matrix.LONGUEUR) + 1 >= 0 and doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (matrix.LONGUEUR - 1)):
                    if doc.positionDocActuellle -  (matrix.LONGUEUR - 1) in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle -  (matrix.LONGUEUR - 1))]
                        daleks.positionOccupe.remove(doc.positionDocActuellle -  (matrix.LONGUEUR - 1))
                    matrix.array[doc.positionDocActuellle -  (matrix.LONGUEUR - 1)] = 0


            if (doc.positionDocActuellle + matrix.LONGUEUR) - 1 <= (matrix.LONGUEUR * matrix.LARGEUR) - 1 and doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (matrix.LONGUEUR - 1)):
                    if doc.positionDocActuellle +  (matrix.LONGUEUR - 1) in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle +  (matrix.LONGUEUR - 1))]
                        daleks.positionOccupe.remove(doc.positionDocActuellle +  (matrix.LONGUEUR - 1))
                    matrix.array[doc.positionDocActuellle +  (matrix.LONGUEUR - 1)] = 0
                    

            if (doc.positionDocActuellle + matrix.LONGUEUR) + 1 <= (matrix.LONGUEUR * matrix.LARGEUR) - 1 and doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (matrix.LONGUEUR + 1)):
                    if doc.positionDocActuellle +  (matrix.LONGUEUR + 1) in daleks.positionOccupe:
                        del daleks.positionOccupeAncienne[daleks.positionOccupe.index(doc.positionDocActuellle +  (matrix.LONGUEUR + 1))]
                        daleks.positionOccupe.remove(doc.positionDocActuellle +  (matrix.LONGUEUR + 1))
                    matrix.array[doc.positionDocActuellle +  (matrix.LONGUEUR + 1)] = 0
        

class Teleporteur:
    def __init__(self):
        pass
        #if 
    #methode pour teleportation mode de jeu Facile            
    def tpModeJeuF(self, matrix, daleks):
        
        condition = False
        i = 0
        positionTP = 0                        
        
        while i < len(daleks.positionOccupe):
            
            if condition == False:
                x = 0
                positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1) #generation position aleatoire pour TP
                condition = True
            
            if positionTP == daleks.positionOccupe[i]:                                          #si la position du TP est la meme que celle d'un 
                i = -1; condition = False; continue
            elif positionTP >= daleks.positionOccupe[i] - 2 and positionTP <= daleks.positionOccupe[i] + 2:                       #ne peut ni aller ni a droite ni a gauche
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] - matrix.LONGUEUR or positionTP == daleks.positionOccupe[i] - matrix.LONGUEUR * 2: #haut
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] + matrix.LONGUEUR or positionTP == daleks.positionOccupe[i] + matrix.LONGUEUR * 2: #bas
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] - (matrix.LONGUEUR + 1) or positionTP == daleks.positionOccupe[i] - (matrix.LONGUEUR + 1) * 2: #haut gauche
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] - (matrix.LONGUEUR - 1) or positionTP == daleks.positionOccupe[i] - (matrix.LONGUEUR - 1) * 2: #haut droite
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] + (matrix.LONGUEUR - 1) or positionTP == daleks.positionOccupe[i] + (matrix.LONGUEUR - 1) * 2: #bas gauche
                i = -1; condition = False; continue
            elif positionTP == daleks.positionOccupe[i] + (matrix.LONGUEUR + 1) or positionTP == daleks.positionOccupe[i] + (matrix.LONGUEUR + 1) * 2: #bas droite
                i = -1; condition = False; continue
            else:
                i+=1
                
        return positionTP
                    
    #methode pour teleportaton mode de jeu moyen        
    def tpModeJeuM(self, matrix, daleks):
        while True:
            positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)

            for pOcc in daleks.positionOccupe:
                if positionTP == pOcc:
                    continue
                else:
                    return positionTP
    
    def tpModeJeuD(self, matrix):
        positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)
        return positionTP



# Cette classe va s'occuper de setter les postions de Docteur/daleks/TasDeFerailles recu par la classe Mouvement
class Positions: 
    

    def __init__(self):
        pass         
                

    def setDocPosition(self, matrix, doc):
        matrix.array[doc.positionDocAncienne] = 0
        matrix.array[doc.positionDocActuellle] = doc.VALEUR_DOC
        doc.positionDocAncienne = doc.positionDocActuellle


    def setDocPositionInitiale(self, matrix, doc):
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != doc.POSITION_DOC_INITIALE:
                matrix.array[i] = 0
            else:
                matrix.array[i] = Docteur.VALEUR_DOC


    def setDalekPosition(self, matrix): 
        for x in range(0, len(daleks.positionOccupe)):   
            matrix.array[daleks.positionOccupeAncienne[x]] = 0
            daleks.positionOccupeAncienne[x] = daleks.positionOccupe[x]
        for x in range(0, len(daleks.positionOccupe)): 
            matrix.array[daleks.positionOccupe[x]] = daleks.VALEUR_DALEKS


    def setTfPosition(self, matrix):
        for x in range(0, len(TasDeFeraille.positionTF)):      # on regarde toujours si il a des tas de feraille dans le tableau
            if 0 == len(TasDeFeraille.positionTF):
                break
            matrix.array[TasDeFeraille.positionTF[x]] = TasDeFeraille.VALEUR_TF
            
    def getPostionsDaleks(self, daleks):
        
        positionsComparaison = []
        for i in range(0, len(daleks.positionOccupe)):
            colomns = daleks.positionOccupe[i]
            ranges = 0
            tab = []
            
            while colomns >= matrix.LONGUEUR:
                colomns -= matrix.LONGUEUR
                ranges += 1
        
            tab.append(colomns)
            tab.append(ranges)
            positionsComparaison.append(tab)
        
        return positionsComparaison    
    
    def getPostionsDoc(self, doc):
        
        colomns = doc.positionDocActuellle
        ranges = 0
        positionsComparaison = []
        
        while colomns >= matrix.LONGUEUR:
            colomns -= matrix.LONGUEUR
            ranges += 1
    
        positionsComparaison.append(colomns)
        positionsComparaison.append(ranges)
        
        return positionsComparaison
    
    def prochainNiveau(self, daleks, n):
        if len(daleks.positionOccupe) == 0:
            n.niveau += 1
            return True
        else:
            return False


    
        
                
    
# Cette classe va s'occuper de bouger les characteres de jeu (Docteur/daleks/TasDeFerailles) dans la matrice si les conditions sont valides
class Mouvement:
    
    def __init__ (self):
        pass
    
    def moveDoc(self, matrix, doc, adj, n, menu):
        success = False
        
        if keyboard.is_pressed("space"):
            success = True 

        elif keyboard.is_pressed("T"):
            if menu.niveau == "1": # Facile
                doc.positionDocActuellle = tp.tpModeJeuF(matrix, daleks)
                if self.verifierCollisionDoc_Tf(tp.tpModeJeuF(matrix, daleks)):
                    success = True
            elif menu.niveau == "2": # Moyen
                doc.positionDocActuellle = tp.tpModeJeuM(matrix, daleks)
                if self.verifierCollisionDoc_Tf(tp.tpModeJeuF(matrix, daleks)):
                    success = True
            elif menu.niveau == "3": # Difficile
                doc.positionDocActuellle = tp.tpModeJeuD(matrix)
                if self.verifierCollisionDoc_Tf(tp.tpModeJeuF(matrix, daleks)):
                    success = True
                    
        elif keyboard.is_pressed("Z"):
            if nbZappeurs.nbZappeurs != 0:
                zappeur.zappeur(matrix, doc, daleks)
                success = True
                nbZappeurs.nbZappeurs -= 1
                
        elif keyboard.is_pressed("left arrow"): 
            if doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - 1):
                    doc.positionDocActuellle -= 1 
                    success = True         
        
        elif keyboard.is_pressed("right arrow"):
            if doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + 1):
                    doc.positionDocActuellle += 1
                    success = True   
                
        elif keyboard.is_pressed("up arrow"):
            if doc.positionDocActuellle - matrix.LONGUEUR >= 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle - matrix.LONGUEUR):
                    doc.positionDocActuellle -= matrix.LONGUEUR 
                    success = True       
                
        elif keyboard.is_pressed("down arrow"):
            if doc.positionDocActuellle + matrix.LONGUEUR <= (matrix.LONGUEUR * matrix.LARGEUR) - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle + matrix.LONGUEUR):
                    doc.positionDocActuellle += matrix.LONGUEUR
                    success = True  

        elif keyboard.is_pressed("Home"):
            if (doc.positionDocActuellle - matrix.LONGUEUR) - 1 >= 0 and doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (matrix.LONGUEUR + 1)):
                    doc.positionDocActuellle -=  matrix.LONGUEUR + 1
                    success = True  

        elif keyboard.is_pressed("Page_Up"):
            if (doc.positionDocActuellle - matrix.LONGUEUR) + 1 >= 0 and doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle -  (matrix.LONGUEUR - 1)):
                    doc.positionDocActuellle -=  matrix.LONGUEUR - 1
                    success = True 

        elif keyboard.is_pressed("End"):
            if (doc.positionDocActuellle + matrix.LONGUEUR) - 1 <= (matrix.LONGUEUR * matrix.LARGEUR) - 1 and doc.positionDocActuellle % matrix.LONGUEUR != 0:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (matrix.LONGUEUR - 1)):
                    doc.positionDocActuellle +=  matrix.LONGUEUR - 1
                    success = True 

        elif keyboard.is_pressed("Page_Down"):
            if (doc.positionDocActuellle + matrix.LONGUEUR) + 1 <= (matrix.LONGUEUR * matrix.LARGEUR) - 1 and doc.positionDocActuellle % matrix.LONGUEUR != matrix.LONGUEUR - 1:
                if mouvement.verifierCollisionDoc_Tf(doc.positionDocActuellle +  (matrix.LONGUEUR + 1)):
                    doc.positionDocActuellle +=  matrix.LONGUEUR + 1
                    success = True 
        
        
        if success == True:
            positions.setDocPosition(matrix, doc)
            os.system('cls')
            adj.afficherMatrix(matrix, nbZappeurs)
            time.sleep(1) 
            if mouvement.verifierCollisionDoc_Dalek(daleks):      # verifie si le docteur va sur le dalek
                matrix.gameOver = True
            mouvement.moveDalek(positions.getPostionsDaleks(daleks), positions.getPostionsDoc(doc))
            if mouvement.verifierCollisionDoc_Dalek(daleks):      # verifie si le dalek va sur le docteur
                matrix.gameOver = True

            #verifier si il y a des collisions
            mouvement.verifierCollisionDalek_Dalek(daleks)
            mouvement.verifierCollisionDalek_Tf(daleks)
            
            positions.setTfPosition(matrix)
            positions.setDalekPosition(matrix)  # code bug, erreur avec positionDalekAncienne 
            os.system('cls')
            adj.afficherMatrix(matrix, nbZappeurs)

            # prochain niveau
            if positions.prochainNiveau(daleks, n):
                nbZappeurs.nbZappeurs += 1
                matrix.LONGUEUR += 1
                matrix.LARGEUR += 1
                os.system('cls')
                doc.initialiserTout(matrix)
                matrix.initialiserTout(doc)
                daleks.initialiserTout(matrix, doc)
                for i in range(n.niveau - 1):
                    daleks.genererDaleks(matrix, doc)
                tf.initialiserTout()
                positions.setDalekPosition(matrix)
                positions.setTfPosition(matrix) 
                adj.afficherMatrix(matrix, nbZappeurs)
            
            time.sleep(0.2)      
            
            # cette methode est l'algorithme qui permet a chaque dalek de savoir dans quelle direction est le docteur
    def moveDalek(self, positionsDaleks, positionDoc):
        for i in range(0, len(daleks.positionOccupe)): # multiplie par niveau
            if positionsDaleks[i][0] == positionDoc[0]:
                if positionsDaleks[i][1] > positionDoc[1]:
                    daleks.positionOccupe[i] -= matrix.LONGUEUR     # en haut
                else:
                    daleks.positionOccupe[i] += matrix.LONGUEUR     # en bas
                    
            elif positionsDaleks[i][1] == positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    daleks.positionOccupe[i] -= 1                   # gauche
                else:
                    daleks.positionOccupe[i] += 1                   # droite
                    
            elif positionsDaleks[i][1] > positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    daleks.positionOccupe[i] -= matrix.LONGUEUR + 1 # en haut a gauche
                else:
                    daleks.positionOccupe[i] -= matrix.LONGUEUR - 1 # en haut a droite
                    
            elif positionsDaleks[i][1] < positionDoc[1]:
                if positionsDaleks[i][0] > positionDoc[0]:
                    daleks.positionOccupe[i] += matrix.LONGUEUR - 1 # en bas a gauche
                else:
                    daleks.positionOccupe[i] += matrix.LONGUEUR + 1 # en bas a droite
            
    def verifierCollisionDalek_Dalek(self, daleks):

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
                matrix.array[daleks.positionOccupeAncienne[i + 1]] = 0
                matrix.array[daleks.positionOccupeAncienne[i]] = 0
                daleks.positionOccupeAncienne.remove(daleks.positionOccupeAncienne[i + 1])
                daleks.positionOccupeAncienne.remove(daleks.positionOccupeAncienne[i])
                nbrDeDaleks =  len(daleks.positionOccupe) - 1
                point.nbrPointsCosmique += point.POINT_VALEUR * 2

                i = 0
                
            else:
                i +=1

    def verifierCollisionDalek_Tf(self, daleks):

        nbrDeTf = len(tf.positionTF)
        nbrDeDaleks = len(daleks.positionOccupe)

        for i in range(0, nbrDeTf):
            x = 0
            while x < nbrDeDaleks:
                if daleks.positionOccupe[x] == tf.positionTF[i]:
                    daleks.positionOccupe.remove(daleks.positionOccupe[x])
                    matrix.array[daleks.positionOccupeAncienne[x]] = 0
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



    def verifierCollisionDoc_Dalek(self, daleks):
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


menu = VueMenu()
sortie = 'n'
allerMenu = ''    

# Objets de Controleur
mouvement = Mouvement()
positions = Positions()
tp = Teleporteur()

# Objets de Modele
matrix = Matrix()
doc = Docteur()
daleks = Daleks()
tf = TasDeFeraille()
point = Pointage()
zappeur = Zappeur()
nbZappeurs = NbZappeurs()

# Generer des positions aleatoires pour les daleks 

positions.setDalekPosition(matrix)
# positions.setTfPosition(matrix)



# Objets de VueJeu
adj = AireDeJeu()
adj.afficherMatrix(matrix, nbZappeurs)
n = Niveau()
data = list()
i = 0

    

#afficher le menu avec le choix: Soit jouer ou voir score
#si jouer: entre nom ect...
#si voir score: afficher liste trié
#si perd -> affiche score puis proposer rejouer ou quitter

while menu.choix != '1' and menu.choix != '2' and menu.choix != '3':
    menu.afficherMenu()

#Teleportage si utilisateur veut l'utiliser:
#a utiliser avec la classe teleporteur
#Si il a fait le choix de jouer
while sortie != 'y':
    if menu.choix == '1':

        matrix.LONGUEUR = 9
        matrix.LARGEUR = 6
        doc.initialiserTout(matrix)
        matrix.initialiserTout(doc)
        daleks.initialiserTout(matrix, doc)
        point.initialiserTout()
        tf.initialiserTout()
        positions.setDalekPosition(matrix)
        positions.setTfPosition(matrix)
        menu.demanderNomEtNiveau()
        
        if menu.niveau == '1':#facile
            print("facile")
            #transporte docteur sur une case vide  ayant au moins deux cases de distance des daleks le plus proche
        elif menu.niveau == '2':#normal
            print("normale")
            #  idem mais on ne vérifie pas la proximité de daleks 
        elif menu.niveau == '3':#difficile
            print("difficile")
            #téléportage est complètement aléatoire et donc on peut atterrir sur un daleks

        os.system('cls')
        adj.afficherMatrix(matrix, nbZappeurs)

        while matrix.gameOver == False:
            mouvement.moveDoc(matrix, doc, adj, n, menu)
        print('Game Over')

        if matrix.gameOver:
        #ecrire les infos dans le fichier csv QUAND LA PARTIE EST TERMINEE
            nomJoueur = menu.nom
            data.append('Prenom : ' + str(nomJoueur) + ', Point : ' + str(point.nbrPointsCosmique))
            fichier = open("liste.csv",'a')
            obj = csv.writer(fichier)
            
            ligne = data[i]
            obj.writerow({ligne})
            fichier.close()
            i+=1

        #puis afficher les score
            with open("liste.csv",'r') as f:
                    obj = csv.reader(f)
                    for ligne in obj:
                        print(ligne)
           
            allerMenu = input("Appuyez sur enter pour revenir au menu")
            menu.afficherMenu()

    elif menu.choix == '2':
        #affiche fichier.csv
        with open("liste.csv",'r') as f:
        # Créer un objet csv à partir du fichier
            obj = csv.reader(f)
            for ligne in obj:
                print(ligne)
        allerMenu = input("Appuyez sur enter pour revenir au menu")
        os.system('cls')
        menu.afficherMenu()
    
    elif menu.choix == '3':
        os.system('cls')
        print('Merci! le programme est terminé')
        sortie = 'y'
        
        