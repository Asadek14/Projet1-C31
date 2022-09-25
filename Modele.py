from mimetypes import init
from pydoc import Doc
import random
from turtle import position
import csv


 # créer et initialiser le docteur
class Docteur:

    POSITION_DOC_INITIALE = 24
    VALEUR_DOC = 1

    def __init__(self):
        self.positionDocActuellle = self.POSITION_DOC_INITIALE
        self.positionDocAncienne = self.positionDocActuellle

    def initialiserTout(self):
        self.positionDocActuellle = 24
        self.positionDocAncienne = self.positionDocActuellle
      
        
        
class Matrix:
    
    gameOver = False
    LONGUEUR = 11
    LARGEUR = 7
    array = list()

    # le constructeur
    def __init__(self):
          
        # Creer et initializer une liste de taille 6 x 8 a zero
        
        
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != Docteur.POSITION_DOC_INITIALE:
                self.array.append(0)
            else:
                self.array.append(Docteur.VALEUR_DOC)

    def initialiserTout(self):
        self.gameOver = False
        self.array.clear()
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != Docteur.POSITION_DOC_INITIALE:
                self.array.append(0)
            else:
                self.array.append(Docteur.VALEUR_DOC)

                
                
                
# class Daleks:

#     VALEUR_DALEKS = 2
#     positionOccupe = []
#     positionOccupeAncienne = [0,0,0,0,0]    # est-ce utilisé?
#     compteur = 1

#     def __init__(self):
#         pass

#     # generateur de positions aléatoires pour les daleks
#     def genererDaleks(self):

#         i = 0

#         while i < 5:      # 5 daleks * valeur du niveau
#             positionDalek = random.randint(0, (Matrix.LARGEUR * Matrix.LONGUEUR) - 1)

#             # verifier si la position est la position initiale du docteur
#             if positionDalek == Docteur.POSITION_DOC_INITIALE:
#                 continue

#             # verifier si la position est deja occupee
#             existe = positionDalek in self.positionOccupe
#             if existe:
#                 continue

#             self.positionOccupe.append(positionDalek)
#             # self.positionOccupeAncienne.append(positionDalek)
#             # Controleur.Postions.setDalekPosition(Controleur.matrix, Controleur.daleks)
#             print(self.positionOccupe[i])
#             i += 1


class Daleks:

    VALEUR_DALEKS = 2
    positionOccupe = [1, 2, 3, 56, 58]
    positionOccupeAncienne = [1, 2, 3, 56, 58]    # est-ce utilisé?
    compteur = 1

    def __init__(self):
        pass

    def initialiserTout(self):

        self.positionOccupe.clear()
        self.positionOccupeAncienne.clear()

        self.positionOccupe = [1, 2, 3, 56, 58]
        self.positionOccupeAncienne = [1, 2, 3, 56, 58]    # est-ce utilisé?
        self.compteur = 1



class TasDeFeraille:

    VALEUR_TF = 3
    positionTF = [35]

    def __init__(self):
        pass

    def initialiserTout(self):
        self.positionTF.clear()


class Pointage:
    nbrPointsCosmique = 0
    POINT_VALEUR = 5
    def __init__(self):
        pass

    def initialiserTout(self):
        self.nbrPointsCosmique = 0

 
# class AfficherScore:
#      with open("C:\\Users\\eloya\\OneDrive\\Cours_5e_session\\Genie_Logiciel_I\\Projet1-C31\\liste.csv",'r') as f:
#             # Créer un objet csv à partir du fichier
#                 obj = csv.reader(f)

#                 for ligne in obj:
#                     print(ligne)