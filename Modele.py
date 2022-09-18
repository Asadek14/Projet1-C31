from pydoc import Doc
import random


 # créer et initialiser le docteur
class Docteur:

    POSITION_DOC_INITIALE = 12
    VALEUR_DOC = 1

    def __init__(self):
      self.positionDocActuellle = 12
      self.positionDocAncienne = self.positionDocActuellle
      
        
        
class Matrix:
    
    LONGUEUR = 5
    LARGEUR = 5

    # le constructeur
    def __init__(self):
          
        # Creer et initializer une liste de taille 6 x 8 a zero
        self.matrix = list()
        
        for i in range(0, self.LONGUEUR * self.LARGEUR):
            if i == Docteur.POSITION_DOC_INITIALE:
                self.matrix.append(Docteur.VALEUR_DOC)
            else:
                self.matrix.append(0)
                
                
                
class Daleks:

    VALEUR_DALEKS = 2
    positionOccupe = []

    def __init__(self):
        pass

    # generateur de positions aléatoires pour les daleks
    def genererDaleks(self):

        i = 0

        while i < 5:      # 5 daleks * valeur du niveau
            positionDalek = random.randint(0, Matrix.LARGEUR * Matrix.LONGUEUR)

            # verifier si la position est la position initiale du docteur
            if positionDalek == Docteur.POSITION_DOC_INITIALE:
                continue

            # verifier si la position est deja occupee
            existe = positionDalek in self.positionOccupe
            if existe:
                continue

            self.positionOccupe.append(positionDalek)
            # Controleur.Postions.setDalekPosition(Controleur.matrix, Controleur.daleks)
            print(self.positionOccupe[i])
            i += 1

    def positionerDaleks(self, matrix):
        for x in range(0, 5):
            matrix.matrix[Daleks.positionOccupe[x]] = Daleks.VALEUR_DALEKS
