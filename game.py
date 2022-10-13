""" Programme qui effectue le jeu du Morpion """
from player import Joueur
import os

class Morpion:
    
    def __init__(self):
        """Constructeur

        Args:
            tableau (list(list())): tableau sur lequel le jeu se déroulera
            playerO (str): 
        """
        self.tableau = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        
        
    def afficher_tableau(self):
        os.system('cls')
        print('\n')
        print("\t"*5 + "##############################################################################\n")
        print("\t"*5 + "############################## Le jeu du Morpion #############################\n")
        print("\t"*5 + "##############################################################################\n\n")
        for i in range(len(self.tableau)):
            print("\t"*9, end="")
            for j in range(len(self.tableau)):
                if j == 2:
                    print(self.tableau[i][j], end=" ")
                else:
                    print(" " + self.tableau[i][j], end=" ")
                    
                if j != len(self.tableau)-1:
                    print (" | ", end=" ", sep=" ")
            if i != len(self.tableau)-1:
                print ("\n" + "\t"*9 + "-"*4 + "+" + "-"*6 + "+" + "-"*4)
        print("\n")
    
    
    def saisieValide(self):
        nombre = int(input(">>>> "))
        while nombre < 1 or nombre > 9:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Entrez un nombre compris entre 1 et 9 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            nombre = int(input(">>>> "))
            
        return nombre
    
    
    
    def testTableau(self, joueur):
        # Tests des différentes possibilités de gagner le jeu
        
        """ Vérifier la 1ère ligne """
        for i in range(0, 3):
            getScore = []
            for j in range(0, 3):
                if self.tableau[i][j] == joueur:
                    getScore.append((self.tableau[i][j]))
            if len(getScore) == 3:
                return joueur
        
        """ Vérifier la 1ère colonne """
        for i in range(0, 3):
            getScore = []
            for j in range(0, 3):
                if self.tableau[j][i] == joueur:
                    getScore.append((self.tableau[j][i]))
            if len(getScore) == 3:
                return joueur
        
        """ Vérifier les diagonales 1 et 2 """
        getScore = []
        for i in range(0, 3):
            if self.tableau[i][i] == joueur:
                getScore.append((self.tableau[i][i]))
            if len(getScore) == 3:
                return joueur
        
        getScore = []
        for i in range(0, 3):
            if self.tableau[2-i][i] == joueur:
                getScore.append((self.tableau[2-i][i]))
            if len(getScore) == 3:
                return joueur
        
        """ On teste s'il y a encore des emplacements du tableau à compléter """
        c = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tableau[i][j] != " ":
                    c += 1
        if c == 9:
            if len(getScore) == 3:
                return joueur
            return True
        return False
            
        
        
    def tourJoueur(self, joueur):
        p = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        print(f">>>> Tour du joueur {joueur}. Entrez un nombre de 1 à 9.")
        
        position = self.saisieValide()
        
        for i in p:
            if i == position:
                if self.tableau[p[i][0]][p[i][1]] == ' ':
                    self.tableau[p[i][0]][p[i][1]] = joueur
                else:
                    print("\n\n--------------------- Attention:  Zone déjà occupée. Choisissez un emplacement non occupé ---------------------\n\n")
                    self.tourJoueur(joueur)
        self.afficher_tableau()
    
                
    
    
    def tictactoe(self):
        self.afficher_tableau()
        endOfGame= False
        
        while endOfGame is False:
            j1 = Joueur.joueur1
            self.tourJoueur(j1)
            res = self.testTableau(j1)
            if res == j1:
                print("\n\n\n" + "\t"*5 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n")
                print("\t"*5 + "+++++++++++++++++++++++++++++++++++ Le joueur {} a gagné +++++++++++++++++++++++++++++++\n".format(j1))
                print("\t"*5 + "++++++++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n\n")
                break
            elif res == True:
                print("################################## Match nul!!! ##################################")
            
            
            j2 = Joueur.joueur2
            self.tourJoueur(j2)
            res = self.testTableau(j2)
            if res == j2:
                print("\n\n\n" + "\t"*5 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n")
                print("\t"*5 + "+++++++++++++++++++++++++++++++++++ Le joueur {} a gagné +++++++++++++++++++++++++++++\n".format(j2))
                print("\t"*5 + "++++++++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n\n")
                break
            elif res == True:
                print("\n\n################################## Match nul!!! ##################################")
    
    


m = Morpion()
# m.afficher_tableau()
m.tictactoe()

