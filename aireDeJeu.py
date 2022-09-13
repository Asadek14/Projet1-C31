from docteur import Docteur 
# Creer et initializer une liste de taille 6 x 8 a zero
class Matrix:

    # les variables statiques de la classe
    longueur = 6
    largeur = 8

    # le constructeur
    def __init__(self):

        self.matrix = list()
        for i in range(0, self.longueur * self.largeur):
            if i == Docteur.positionDocteur:
                self.matrix.append(Docteur.docteur)
            else:
                self.matrix.append(0)

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


matrix = Matrix() # creer une vairable matrice

aire = AireDeJeu() # afficher cette variable
aire.afficherMatrix(matrix)
