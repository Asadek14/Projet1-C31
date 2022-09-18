from Modele import Matrix

class AireDeJeu: 
# adj pour 'aire de jeu'
    def __init__(self):
        self.ligne = Matrix.LONGUEUR

    def afficherMatrix(self, matrix):
        self.matriceDuJeu = matrix
        for i in range(0, Matrix.LONGUEUR * Matrix.LONGUEUR):
            # a chaque 8 valeur change de ligne
            if i % self.ligne == 0:
                print('\n')
            print(self.matriceDuJeu.matrix[i], end = ' ')
            
        print("\n")

#class VueMenu
class VueMenu:
    def show() :
        print("Jeu des Daleks")
        print("\n")
        print("Inserer nom :")
        print("Choisir mode de jeu pour commencer")
        print("1 - Facile \n")
        print("2 - Moyen\n")
        print("3 - Difficile")
        print("pointage record:")
