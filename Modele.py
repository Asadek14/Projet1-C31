from pydoc import Doc
import random


 # créer et initialiser le docteur
class Docteur:

    POSITION_DOC_INITIALE = 12
    VALEUR_DOC = 1
    positionDocActuellle = 12
    positionDocAncienne = positionDocActuellle
      
        
        
class Matrix:
    
    LONGUEUR = 10
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
                
                
                
class Daleks:

    VALEUR_DALEKS = 2
    positionOccupe = []

    def __init__(self):
        pass

    # generateur de positions aléatoires pour les daleks
    def genererDaleks(self):

        i = 0

        while i < 5:      # 5 daleks * valeur du niveau
            positionDalek = random.randint(0, (Matrix.LARGEUR * Matrix.LONGUEUR) - 1)

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