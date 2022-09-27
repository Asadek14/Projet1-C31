from mimetypes import init
from pydoc import Doc, doc
import random
from turtle import position
import csv


#créer et initialiser le docteur
class Docteur:
    nbZappeur = 1
    VALEUR_DOC = 1
    POSITION_DOC_INITIALE = 26

    def __init__(self):
        
        self.positionDocActuellle = self.POSITION_DOC_INITIALE
        self.positionDocAncienne = self.positionDocActuellle

    def initialiserTout(self, matrix):
        self.POSITION_DOC_INITIALE = int((matrix.LONGUEUR * matrix.LARGEUR - 1) / 2)
        self.positionDocActuellle = self.POSITION_DOC_INITIALE
        self.positionDocAncienne = self.positionDocActuellle
      
        
        
class Matrix:
    
    gameOver = False
    LONGUEUR = 9
    LARGEUR = 6
    array = list()

    # le constructeur
    def __init__(self):
          
        # Creer et initializer une liste de taille 6 x 8 a zero
        
        
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != Docteur.POSITION_DOC_INITIALE:
                self.array.append(0)
            else:
                self.array.append(Docteur.VALEUR_DOC)

    def initialiserTout(self, doc):
        self.gameOver = False
        self.array.clear()
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i != doc.POSITION_DOC_INITIALE:
                self.array.append(0)
            else:
                self.array.append(Docteur.VALEUR_DOC)



class Daleks:

    VALEUR_DALEKS = 2
    positionOccupe = []
    positionOccupeAncienne = [0,0,0,0,0]    # est-ce utilisé?
    compteur = 1

    def __init__(self):
        pass

    # generateur de positions aléatoires pour les daleks
    def genererDaleks(self, matrix, doc):

        i = 0

        while i < 5:      # 5 daleks * valeur du niveau
            positionDalek = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) - 1)

            # verifier si la position est la position initiale du docteur
            if positionDalek == doc.POSITION_DOC_INITIALE:
                continue

            # verifier si la position est deja occupee
            existe = positionDalek in self.positionOccupe
            if existe:
                continue

            self.positionOccupe.append(positionDalek)
            # self.positionOccupeAncienne.append(positionDalek)
            # Controleur.Postions.setDalekPosition(Controleur.matrix, Controleur.daleks)
            i += 1

        i = 0
        while i < 5:
            self.positionOccupeAncienne.append(0)
            i+=1


    def initialiserTout(self, matrix, doc):

        self.positionOccupe.clear()
        self.positionOccupeAncienne.clear()

        self.positionOccupe = []
        self.positionOccupeAncienne = [0,0,0,0,0]    # est-ce utilisé?

        i = 0

        while i < 5:      # 5 daleks * valeur du niveau
            positionDalek = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) - 1)

            # verifier si la position est la position initiale du docteur
            if positionDalek == doc.POSITION_DOC_INITIALE:
                continue

            # verifier si la position est deja occupee
            existe = positionDalek in self.positionOccupe
            if existe:
                continue

            self.positionOccupe.append(positionDalek)
            # self.positionOccupeAncienne.append(positionDalek)
            # Controleur.Postions.setDalekPosition(Controleur.matrix, Controleur.daleks)
            i += 1

        self.compteur = 1



# class Daleks:

#     VALEUR_DALEKS = 2
#     positionOccupe = [1, 2, 3, 56, 58]
#     positionOccupeAncienne = [1, 2, 3, 56, 58]    # est-ce utilisé?
#     compteur = 1

#     def __init__(self):
#         pass
class TasDeFeraille:

    VALEUR_TF = 3
    positionTF = []

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

class Niveau:
    
    def __init__(self):
        self.niveau = 1
        
class NbZappeurs:
    
    def __init__(self):
        self.nbZappeurs = 1