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
    def afficherMenu(self) :
        print("Jeu des Daleks")
        print("\n")
        print("Inserer nom :")
        self.nom = input()
        #print(self.nom)
        print("Choisir mode de jeu pour commencer")#-> Va determiner le mode de teleportage
        print("1 - Facile \n")#si facile le teleporteur transporte docteur sur une case vide  ayant au moins deux cases de distance des Daleks le plus proche
        print("2 - Moyen\n")#  idem mais on ne vérifie pas la proximité de Daleks 
        print("3 - Difficile")#téléportage est complètement aléatoire et donc on peut atterrir sur un Dalek
        self.niveau = input("choix niveau: ")
        
