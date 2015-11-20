#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Main du Touché-Coulé

import game
import dataManagement as d
from formatInfos import inputChoice, printTitle, printRules
from sys import exit

def exitApp() :
    """
    Fonction qui envoie un message avant de quitter.
    
    Arguments:
    Aucun
    
    Retour:
    Aucun
    
    Exemple:
    >>> exitApp()
    Au revoir
    """
    print("            Au revoir")
    exit(0)

def menu() :
    """
    Menu du Touché-Coulé.
    Affiche le titre, les choix disponibles (Jouer, Règles, Choix du pack, Créateur de pack, Sortie).
    Laisse l'utilisateur choisir l'une de ces options.
    
    Arguments:
    aucun
    
    Retour:
    aucun
    
    Exemple:
    >>> menu()
       __                   __     _                          __ _  
      / /_____  __  _______/ /_  _//        _________  __  __/ ///  
     / __/ __ \/ / / / ___/ __ \/ _ \ ____ / ___/ __ \/ / / / / _ \ 
    / /_/ /_/ / /_/ / /__/ / / /  __//___// /__/ /_/ / /_/ / /  __/ 
    \__/\____/\__,_/\___/_/ /_/\___/      \___/\____/\__,_/_/\___/  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
                1. Jouer
                2. Afficher les règles
                3. Choix du pack de bateaux
                4. Créer votre pack de bateaux
                5. Quitter
                -> lol
    Ce n'est pas un entier positif
                -> -89
    Ce n'est pas un entier positif
                -> 42
    Les choix possibles sont 1, 2, 3, 4, 5
                -> 2
    
    **************************************************************
    *                  RÈGLES DU TOUCHÉ-COULÉ :                  *
    *                  ~~~~~~~~~~~~~~~~~~~~~~~~                  *
    *                                                            *
    *     Le but du jeu est de couler les navires ennemis        *
    * avant que votre adversaire n'élimine votre flotte.         *
    *                                                            *
    * 1) Placement de votre flotte :                             *
    *     Avant la partie, placez vos navires sur la grille      *
    * de manière stratégique.                                    *
    * Pour placer un bateau, entrez la position de son extrémité *
    * et la direction vers laquelle s'étend votre navire.        *
    * Les directions possibles sont Nord, Sud, Ouest, Est.       *
    *                                                            *
    * 2) Déroulement du jeu :                                    *
    *     Tirez ensuite à tour de rôle sur la grille             *
    * de votre adversaire à l'aide de coordonnées du type        *
    * lettre-chiffre désignant la case visée (ex : B5, C2, F8).  *
    * Si vous touchez ou coulez un navire, vous pouvez rejouer.  *
    *                                                            *
    * 3) Fin du jeu :                                            *
    *     Le premier à éliminer entièrement la flotte            *
    * de son adversaire remporte la victoire!                    *
    *                                                            *
    *     Bon amusement !!!                                      *
    *                                                            *
    **************************************************************
                                                                
    <En couleur, et avec ClearScreen>
    """
    printTitle()
    print("""            1. Jouer
            2. Afficher les règles
            3. Choisir un pack de bateaux
            4. Créer votre pack de bateaux
            5. Quitter""")
    options={1:game.game, 2:printRules, 3:d.menuPacks, 4:d.packsCreator, 5:exitApp}
    choice=inputChoice(options)
    options[choice]()

def execApp() :
    """
    Fonction principale ('MAIN') du jeu Touché-Coulé.
    Exécute en boucle menu() tant que l'utilisateur le souhaite.
    Quitte le menu dès que survient une erreur du type KeyboardInterrupt.
    
    Arguments:
    aucun
    
    Retour:
    aucun
    
    Exemple:
    >>> execApp()
       __                   __     _                          __ _  
      / /_____  __  _______/ /_  _//        _________  __  __/ ///  
     / __/ __ \/ / / / ___/ __ \/ _ \ ____ / ___/ __ \/ / / / / _ \ 
    / /_/ /_/ / /_/ / /__/ / / /  __//___// /__/ /_/ / /_/ / /  __/ 
    \__/\____/\__,_/\___/_/ /_/\___/      \___/\____/\__,_/_/\___/  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
                1. Jouer
                2. Afficher les règles
                3. Choix du pack de bateaux
                4. Créer votre pack de bateaux
                5. Quitter
                -> lol
    Ce n'est pas un entier positif
                -> 42
    Les choix possibles sont 1, 2, 3, 4, 5
                -> 1
    <Exécution du jeu>                                
    <En couleur, et avec ClearScreen>
    """
    try :
        restart=True
        while restart :
            menu()
            restart=str(input("Voulez-vous revenir au menu principal? (O/N) : ")).lower() in ["o", "oui"]
    except (KeyboardInterrupt, EOFError):
        print("\nAu revoir")

if __name__ == "__main__" :
    execApp()
