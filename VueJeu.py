from Modele import Daleks, Matrix
import csv
import os

class AireDeJeu: 
# adj pour 'aire de jeu'
    def __init__(self):
        pass

    def afficherMatrix(self, matrix):
        self.ligne = matrix.LONGUEUR
        for i in range(0, matrix.LONGUEUR * matrix.LARGEUR):
            # a chaque 8 valeur change de ligne
            if i % self.ligne == 0:
                if i != 0:
                    print('\033[0;37;40m\n')

            if matrix.array[i] == 1:
                print('\033[0;37;46m  ', end = '\033[0;37;40m ') #Docteur = Cyan
            elif matrix.array[i] == 2:
                print('\033[0;37;41m  ', end = '\033[0;37;40m ') #Daleks = Rouge
            elif matrix.array[i] == 3:
                print('\033[0;37;43m  ', end = '\033[0;37;40m ') #Tas de feraille = jaune
            else:
                print('\033[0;37;47m  ', end = '\033[0;37;40m ')
            
        print('\n')
        print('Docteur:', '\033[0;37;46m  ', end = '\033[0;37;40m ')
        print('  Daleks:', '\033[0;37;41m  ', end = '\033[0;37;40m ')
        print('  Tas de ferraille:', '\033[0;37;43m  ', end = '\033[0;37;40m ')
        
        print('\n')
        print('Mouvement docteur: \033[0;33;40m\u2190 \u2191 \u2192 \u2193 \u2196 \u2197 \u2198 \u2199' , end = '\033[0;37;40m ')
        print("  Téléporteur:", "\033[0;33;40m'T'", end = "\033[0;37;40m ")
        print("  Zappeur:", "\033[0;33;40m'Z'", end = "\033[0;37;40m ")   
        print("  Passer son tour:", "\033[0;33;40m'Spacebar'", end = "\033[0;37;40m ")   
        print("\n")

#class VueMenu
class VueMenu:
    
    choix = ""
    nom = ""
    niveau = ""
    
    def __init__(self):
        pass
        
    
    def afficherMenu(self) :
        
        os.system('cls')
        print("Jeu des Daleks")
        print("\n")
        print("1/ Jouer")
        print("\n")
        print("2/ Voir score")
        self.choix = input("Quel est votre choix?")

    def demanderNomEtNiveau(self): 
        # if self.choix == '1':
            self.nom = input("Nom du joueur:")
            print("Choisir mode de jeu pour commencer")     #-> Va determiner le mode de teleportage
            print("1 - Facile \n")                          #si facile le teleporteur transporte docteur sur une case vide  ayant au moins deux cases de distance des Daleks le plus proche
            print("2 - Moyen\n")                            #idem mais on ne vérifie pas la proximité de Daleks 
            print("3 - Difficile")                          #téléportage est complètement aléatoire et donc on peut atterrir sur un Dalek
            self.niveau = input("choix niveau: ")

        # elif self.choix == '2':
        #     #affiche fichier.csv
        #     with open("C:\\Users\\eloya\\OneDrive\\Cours_5e_session\\Genie_Logiciel_I\\Projet1-C31\\liste.csv",'r') as f:
        #     # Créer un objet csv à partir du fichier
        #         obj = csv.reader(f)
        #         for ligne in obj:
        #             print(ligne)
            

        # elif self.choix == '3':
        #     os.system('cls')
        #     print("Au revoir")
    

       
        