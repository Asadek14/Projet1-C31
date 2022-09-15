import random

 # créer et initialiser le docteur
class Docteur:

    def __init__(self):
        self.positionDocActuellle = 12
        self.positionDocAncienne = self.positionDocActuellle
        self.positionDocInitiale = 12
        self.valeurDoc = 1
        

#     # variables statiques  
#     valeurDocteur = 1
#     positionDocteur = 17
    
        
#     def setDocteurMatrix(self):
#         self.matrix.setDocteurMatrix()




# matrix = aireDeJeu.Matrix() # creer une vairable matrice
# aire = aireDeJeu.AireDeJeu() # afficher cette variable
# aire.afficherMatrix(matrix)

# doc = Docteur()

# aire.afficherMatrix(matrix)



#from aireDeJeu import Matrix

class Daleks:

  # generateur de positions aléatoires pour les daleks
  i = 0
  # positionsOccupe = [0]

  while i < 5:
    positionDalek = random.randint(0, 47)
    # positionsOccupe[i] += positionDalek

    # verifier si la position est deja occupee 
    # x = 0  
    # while x < 5:
    #   if positionDalek == positionsOccupe[x]:
    #     break
    #0, Matrix.longueur * Matrix.largeur
    print(positionDalek)
    i += 1
