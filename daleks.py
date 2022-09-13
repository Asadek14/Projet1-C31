import random
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