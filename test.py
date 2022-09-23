if keyboard.is_pressed("T"): #si on appuie la touche T
                    if self.modeJeu == "F": # Facile
                        doc.positionDocActuellle = tp.tpModeJeuF(); success = True
                    elif self.modeJeu == "M": # Moyen
                        doc.positionDocActuellle = tp.tpModeJeuM(); success = True
                    elif self.modeJeu == "D": # Difficile
                        doc.positionDocActuellle = tp.tpModeJeuD(); success = True
                        

def tpModeJeuF(self):
        while True:
            positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1) #generation position aleatoire pour TP

            for pOcc in daleks.positionOccupe:#for pour passer dans toutes les positions des daleks selon le niveau (5, 10, 15, etc)
                if positionTP == daleks.positionOccupe:#si la position du TP est la meme que celle occupé par un dalek, refaire la generation position aléatoire
                    continue
                elif positionTP != daleks.positionOccupe[-2] or daleks.positionOccupe[+2] or daleks.positionOccupe[-(matrix.LONGUEUR * 2)] or daleks.positionOccupe[+(matrix.LONGUEUR * 2)] :#si la position est a une distance d'au moins deux cases, retourner la position
                    continue
                else:
                    return positionTP
            break
    #methode pour teleportaton mode de jeu moyen        
    def tpModeJeuM(self):
        while True:
            positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)

            for pOcc in daleks.positionOccupe:
                if positionTP == pOcc:
                    continue
                else:
                    return positionTP
        #break
    #methode pour teleportation mode de jeu difficile        
    def tpModeJeuD(self):
        positionTP = random.randint(0, (matrix.LARGEUR * matrix.LONGUEUR) -1)
        return positionTP