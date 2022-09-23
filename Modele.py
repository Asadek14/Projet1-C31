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


class Zappeur:
    pass

#enregistrer tous les points accumules par niveau
#-------------------------------------------------
#class EnregistrerPointage:

#recuperer le nom du joueur qui est dans VueJeu
#recuperer le niveau du joueur qui est dans VueJeu
#recuperer les points gagne par le joueur

#Une fois que j'ai les 3 infos, les écrire dans le fichier CSV

