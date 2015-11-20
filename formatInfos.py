#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Contient les fonctions de formatage et d'affichage des données entrées

from math import log, sqrt
from os import popen
import basicsFunc as b

# Les inputs
def inputInt(text) :
    """
    Demande à l'utilisateur d'entrer un entier positif.
    
    Arguments:
    - text (str) : Texte affiché lors de la requête à l'utilisateur.
    
    Retour:
    (int) Entier positif entré par l'utilisateur.
    
    Exemple:
    >>> n=inputInt("Entrez un entier positif : ")
    Entrez un entier positif : Salut, ça va ?
    Ce n'est pas un entier positif
    Entrez un entier positif : 42
    >>> print(n)
    42
    """
    res=input(text)
    while not(res.isdigit()) :
        print("Ce n'est pas un entier positif")
        res=input(text)
    return int(res)

def inputChoice(dic) :
    """
    Demande à l'utilisateur de choisir une clé d'un dictionaire (dic).
    
    Arguments:
    - dic (dict) : Dictionnaire des choix possibles pour l'utilisateur.
    
    Retour:
    (int) Entier positif, clé du dictionnaire correspondant au choix de l'utilisateur.
    
    Exemple:
    >>> dic={1:"Choix1", 2:"Choix2", 3:"Choix3"}
    >>> x=inputChoice(dic)
                -> 5
    Les choix possibles sont 1, 2, 3
                -> 3
    >>> print(x)
    3
    """
    res=inputInt("            -> ")
    options=list(range(1, len(dic)+1))
    while not(res in options) :
        print("Les choix possibles sont "+str(options)[1:len(str(options))-1])
        res=inputInt("            -> ")
    return res

def isValidMinSize(size, ships) : # Vérifie si la grille est de taille suffisante pour accueillir tous les bateaux.
    """
    Vérifie si la taille (size) de la grille est suffisante pour accueillir tous les bateaux (ships).
    
    Arguments:
    - size (int) : Longueur d'un côté de la grille.
    - ships (list) : Liste des bateaux choisis de l'utilisateur.
    
    Retour:
    (bool) True si la grille peut contenir tous les bateaux, False sinon.
    
    Exemple:
    >>> bateaux=[["porte-avions", None, None, 5,5],["porte-avions", None, None, 5,5],["porte-avions", None, None, 5,5],["cuirassé", None, None, 4,4],["croiseur", None, None, 3,3]]
    >>> isValidMinSize(4, bateaux)
    False
    >>> isValidMinSize(5, bateaux)
    True
    >>> bateaux2=[["boat", None, None, 2,2],["boat", None, None, 2,2],["boat", None, None, 2,2]]
    >>> isValidMinSize(2, bateaux2)
    False
    >>> isValidMinSize(3, bateaux2)
    True
    """
    sumLen=maxLen=0
    for ship in ships :
        sumLen+=ship[3]
        if(ship[3]>maxLen) :
            maxLen=ship[3]
    return(size >= max(maxLen,int(1+sqrt(sumLen))))

def inputSizeGrid(ships) :
    """
    Demande à l'utilisateur d'entrer une taille de grille capable d'accueillir la flotte entière (ships),
    mais également affichable dans le terminal.
    
    Arguments:
    - ships (list) : Liste des bateaux de l'utilisateur.
    
    Retour:
    (int) Taille de grille viable.
    
    Exemple:
    >>> bateaux=[["boat", None, None, 2,2],["boat", None, None, 2,2],["boat", None, None, 2,2]]
    >>> n=inputSizeGrid(bateaux)
    Entrez la taille de la grille voulue :2
    Grille trop petite pour placer votre flotte
    Entrez la taille de la grille voulue :120
    Terminal trop petit pour afficher les grilles, essayez de l'agrandir
    Entrez la taille de la grille voulue :10
    >>> print(n)
    10
    """
    res=inputInt("Entrez la taille de la grille voulue :")
    while not(isValidMinSize(res, ships) and 6*res+9 <= int(popen('stty size', 'r').read().split()[1])) :
        if 6*res+9 <= int(popen('stty size', 'r').read().split()[1]) :
            print("Grille trop petite pour placer votre flotte")
        else :
            print("Terminal trop petit pour afficher les grilles, essayez de l'agrandir")
        res=inputInt("Entrez la taille de la grille voulue :")
    return res

def validInput() :
    """
    Demande à l'utilisateur d'entrer des coordonnées viables de la forme lettre-chiffre.
    Cycle tant que l'entrée n'est pas satisfaisante.
    
    Arguments:
    aucun
    
    Retour:
    (str) Coordonnées lettre-chiffre viables.
    
    Exemple:
    >>> x=validInput()
    Entrez la case :Hein???
    Coordonnée invalide
    Entrez la case :06
    Coordonnée invalide
    Entrez la case :B8
    >>> print(x)
    B8
    """
    coord = str(input("Entrez la case :"))
    while not(b.isValidCoordInput(coord)) :
        print("Coordonnée invalide")
        coord = str(input("Entrez la case :"))
    return coord

def inputCoord(grid) :
    """
    Demande à l'utilisateur d'entrer des coordonnées viables de la forme chiffre-lettre,
    à l'intérieur d'une grille donnée. Cycle tant que l'entrée n'est pas satisfaisante.
    
    Arguments:
    - grid (list) : Grille de jeu de l'utilisateur.
    
    Retour:
    (tup) Coordonnées viables de la forme (ligne, colonne) traduite par la fonction coordToPos.
    
    Exemple:
    >>> grille=[[[None, None], [None, None]], [[None, None], [None, None]]]
    >>> x=inputCoord(grille)
    Entrez la case :B3
    Coordonnée hors de la grille
    Entrez la case :lol
    Coordonnée invalide
    Entrez la case :A2
    >>> print(x)
    (0, 1)
    """
    pos=b.coordToPos(validInput())
    while not(0<=pos[0]<len(grid) and 0<=pos[1]<len(grid)) :
        print("Coordonnée hors de la grille")
        pos=b.coordToPos(validInput())
    return pos

def inputDirection() :
    """
    Demande à l'utilisateur d'entrer une direction viable,
    cycle tant que l'entrée n'est pas satisfaisante.
    
    Arguments:
    aucun
    
    Retour:
    (str) Direction viable. "NORTH", "SOUTH", "WEST", ou "EAST" en fonction du choix du joueur.
    
    Exemple:
    >>> x=inputDirection()
    Entrez la direction :NaüORD
    Direction entrée inexistante
    Entrez la direction :hAuT
    >>> print(x)
    NORTH
    """
    direction=str(input("Entrez la direction :"))
    while direction.upper() not in ["NORD", "SUD", "OUEST", "EST", "N", "S", "O", "E", "HAUT", "BAS", "GAUCHE", "DROITE", "H", "B", "G", "D", "W"] :
        print("Direction entrée inexistante")
        direction=str(input("Entrez la direction :"))
    return b.inputToDirection(direction.upper())

def inputPosShip(ship, grid) :
    """
    Demande à l'utilisateur d'entrer une position pour le bateau (ship) sur une grille (grid).
    Cycle tant que le bateau n'est pas correctement placé.
    
    Arguments:
    - ship (list) : Un bateau de l'utilisateur.
    - grid (list) : Grille de jeu.
    
    Retour:
    (tup) Position viable pour un bateau ship de la forme (ligne, colonne).
    
    Exemple:
    >>> bateau=["canot", None, None, 2, 2]
    >>> grille=[[[None, None], [None, None]], [[None, None], [None, None]]]
    >>> x=inputPosShip(bateau, grille)
    Entrez la case :A3
    Coordonnée hors de la grille
    Entrez la case :A1
    >>> print(x)
    (0, 0)
    """
    pos=inputCoord(grid)
    while b.validShipDirections(pos, ship, grid) == [] :
        print("Position invalide pour", ship[0])
        pos=inputCoord(grid)
    return pos

def inputDirectionShip(pos, ship, grid) :
    """
    Demande à l'utilisateur d'entrer une direction valide pour un bateau (ship) placé
    en son extrémité de position (pos), sur une grille (grid) donnée.
    
    Arguments:
    - pos (tup) : Position de l'extrémité d'un bateau (ship).
    - ship (list) : Un bateau de l'utilisateur.
    - grid (list) : Grille de jeu.
    
    Retour:
    (str) Direction viable pour le bateau (ship). "NORTH", "SOUTH", "WEST", ou "EAST" en fonction du choix du joueur.
    
    Exemple:
    >>> bateau=["canot", None, None, 2, 2]
    >>> grille=[[[None, None], [None, None]], [[None, None], [None, None]]]
    >>> x=inputDirectionShip((0,0),bateau,grille)
    Entrez la direction :g
    Direction invalide pour canot
    Entrez la direction :d
    >>> print(x)
    EAST
    """
    direction=inputDirection()
    while direction not in b.validShipDirections(pos, ship, grid) :
        print("Direction invalide pour", ship[0])
        direction=inputDirection()
    return direction


# Les prints
def remainingShipsToPlace(ships, grid) :
    """
    renvoie un string contenant les bateaux restant à placer.
    
    Arguments:
    - ships (list) : liste contenant tout les bateaux
    - grid (list) : grille sur laquelle on place les bateaux
    
    Retour:
    (str) string des bateaux restannt à placer
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "EAST", 2, 2], None], [["destroyer", (0,0), "EAST", 2, 2], None]], [[None, None], [None, None]]]
    >>> ships
    [["destroyer", (0,0), "EAST, 2, 2], ["sous-marin", None, None, 3, 3]]
    >>> remainingShipsToPlace(ships, grid)
    "sous-marin (3)"
    """
    remainingShips=[]
    for ship in ships :
        if not(b.isItemInGrid(ship, grid)) :
            remainingShips.append(ship[0]+" ("+str(ship[3])+")")
    return ", ".join(remainingShips)

def printTitle() :
    """
    Affiche un titre colorisé du jeu Touché-Coulé dans le terminal.
    NB: Dégage préalablement le terminal de son contenu.
    
    Arguments:
    aucun
    
    Retour:
    aucun
    
    Exemple:
    >>> printTitle()
    <Après effacement du contenu du terminal>
       __                   __     _                          __ _  
      / /_____  __  _______/ /_  _//        _________  __  __/ ///  
     / __/ __ \/ / / / ___/ __ \/ _ \ ____ / ___/ __ \/ / / / / _ \ 
    / /_/ /_/ / /_/ / /__/ / / /  __//___// /__/ /_/ / /_/ / /  __/ 
    \__/\____/\__,_/\___/_/ /_/\___/      \___/\____/\__,_/_/\___/  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    <En couleur>
    """
    print("\x1b[1J")
    print("""\033[1;40;93m   __                   __     _    \033[91m                      __ _  \033[0m
\033[1;40;93m  / /_____  __  _______/ /_  _//    \033[91m    _________  __  __/ ///  \033[0m
\033[1;40;93m / __/ __ \/ / / / ___/ __ \/ _ \ __\033[91m__ / ___/ __ \/ / / / / _ \ \033[0m
\033[1;40;93m/ /_/ /_/ / /_/ / /__/ / / /  __//_\033[91m__// /__/ /_/ / /_/ / /  __/ \033[0m
\033[1;40;93m\__/\____/\__,_/\___/_/ /_/\___/   \033[91m   \___/\____/\__,_/_/\___/  \033[0m
\033[1;34;40m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m
""")

def printRules() :
    """
    Affiche les règles en couleur du jeu Touché-Coulé dans le terminal.
    
    Arguments:
    aucun
    
    Retour:
    aucun
    
    Exemple:
    >>> printRules()
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
    <En couleur et partiellement souligné>
    """
    print("""\x1b[1J\033[1;40m**************************************************************\033[0m
\033[1;40m*                  RÈGLES DU TOUCHÉ-COULÉ :                  *\033[0m
\033[1;40m*                  ~~~~~~~~~~~~~~~~~~~~~~~~                  *\033[0m
\033[40m*                                                            *\033[0m
\033[40m*     Le but du jeu est de couler les navires ennemis        *\033[0m
\033[40m* avant que votre adversaire n'élimine votre flotte.         *\033[0m
\033[40m*                                                            *\033[0m
\033[1;40m* 1) \033[4mPlacement de votre flotte :\033[0;40m                             *\033[0m
\033[40m*     Avant la partie, placez vos navires sur la grille      *\033[0m
\033[40m* de manière stratégique.                                    *\033[0m
\033[40m* Pour placer un bateau, entrez la position de son extrémité *\033[0m
\033[40m* et la direction vers laquelle s'étend votre navire.        *\033[0m
\033[40m* Les directions possibles sont Nord, Sud, Ouest, Est.       *\033[0m
\033[40m*                                                            *\033[0m
\033[1;40m* 2) \033[4mDéroulement du jeu :\033[0;40m                                    *\033[0m
\033[40m*     Tirez ensuite à tour de rôle sur la grille             *\033[0m
\033[40m* de votre adversaire à l'aide de coordonnées du type        *\033[0m
\033[40m* lettre-chiffre désignant la case visée (ex : B5, C2, F8).  *\033[0m
\033[40m* Si vous touchez ou coulez un navire, vous pouvez rejouer.  *\033[0m
\033[40m*                                                            *\033[0m
\033[1;40m* 3) \033[4mFin du jeu :\033[0;40m                                            *\033[0m
\033[40m*     Le premier à éliminer entièrement la flotte            *\033[0m
\033[40m* de son adversaire remporte la victoire!                    *\033[0m
\033[40m*                                                            *\033[0m
\033[1;40m*     Bon amusement !!!                                      *\033[0m
\033[40m*                                                            *\033[0m
\033[40m**************************************************************\033[0m""")

def numToLetter(n):
    """
    Retourne les lettres, en base 26, correspondant à l'entier (n).
    
    Arguments:
    - n (int) : Nombre entier quelconque.
    
    Retour:
    (str) Lettres correspondantes en base 26.
    
    Exemples:
    >>> numToLetter(0)
    'A'
    >>> numToLetter(25)
    'Z'
    >>> numToLetter(26)
    'BA'
    >>> numToLetter(789)
    'BEJ'
    >>> numToLetter(123456789)
    'KKEEKB'
    """
    letters, rest, i = "", n, log(n)//log(26) if(n!=0) else 0 
    while i>=0 :
        n=rest
        rest=rest%(26**i)
        letters+=chr(65+int((n-rest)/(26**i)))
        i-=1
    return letters

def colorSquare(ls, square, defaultBackground):
    """
    Retourne les caractères d'affichage (square) d'une case (ls) de la grille de jeu
    sur un fond de couleur indicée (defaultBackground).
    
    Arguments:
    - ls (list) : Élément de la grille de jeu, [Bateau ou None, État de la case ("T" ou "M") ou None].
    - square (str) : Couple de caractère à afficher au centre de la case.
    - defaultBackground (str) : Indice de couleur de fond.
    
    Retour:
    (str) Affichage de la case considérée.
    
    Exemple:
    >>> case=[["bateau",(2,3),"SOUTH",3,1],"T"]
    >>> affichage="Bateau sur l'eau"
    >>> fond="44"
    >>> colorSquare(ls, sq, bkg)
    '\x1b[0;44m|\x1b[4;30;103mBateau sur l'eau'
    """
    background=""
    if(ls[0]!=None and ls[1]!=None):
        if(ls[1]=="T" and ls[0][4]!=0):
            background=";30;103"
        elif(ls[0][4]==0):
            background=";30;101"
    elif ls[1]=="M" :
        background=";30;104"
    return "\033[0;"+defaultBackground+"m|\033[4"+background+"m"+square

def displaySquare(ls):
    """
    Retourne les caractères à afficher correspondant à une case d'une grille,
    en tenant compte du bateau éventuellement présent et de son état.
    
    Arguments:
    - ls (list) : Élément de la grille de jeu, [Bateau ou None, État de la case ("T" ou "M") ou None].
    
    Retour:
    (str) Affichage de la case considérée, tenant compte du bateau éventuellement présent, et son état.
    
    Exemple:
    >>> case=[["bateau",(2,3),"SOUTH",3,1],"T"]
    >>> displaySquare(case)
    '\x1b[0;44m|\x1b[4;30;103mba'
    """
    if(ls[0]==None):
        res="  "
    else:
        res=ls[0][0][:2]
    return colorSquare(ls, res, "44")

def printFirstLines(size):
    """
    Affiche les deux premières lignes de la juxtaposition des deux grilles.
    Il s'agit uniquement ici du nom des grilles, et le numéro des colonnes.
    
    Arguments:
    - size (int) : Longueur d'un côté d'une grille.
    
    Retour:
    aucun
    
    Exemple:
    >>> printFirstLines(10)
    Secteur adverse                   | Votre secteur
    __|1  2  3  4  5  6  7  8  9  10  | __|1  2  3  4  5  6  7  8  9  10 
    <Partiellement souligné>
    """
    print("\033[1mSecteur adverse\033[0m"+" "*(3*size-11)+"| \033[1mVotre secteur\033[0m")
    num="\033[4m"
    for i in range(1,1+size):
        num+=str(i)+(3-len(str(i)))*" "
    print("__|"+num+"\033[0m | __|"+num+"\033[0m")

def printTwoGrids(hiddenGrid, grid):
    """
    Affiche simultanément et en vis-à-vis les deux grilles de jeu.
    La grille secrète du bot à gauche, la grille du joueur à droite.
    
    Arguments:
    - hiddenGrid (list) : Grille secrète du bot.
    - grid (list) : Grille du joueur
    
    Retour:
    aucun
    
    Exemple:
    >>> import basicsFunc as b
    >>> grille=b.createEmptyGrid(5)
    >>> grilleSecrète=b.createEmptyGrid(5)
    >>> printTwoGrids(grilleSecrète, grille)
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |  |  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    <En couleur et partiellement souligné>
    """
    printFirstLines(len(hiddenGrid[0]))
    for i in range(len(grid)):
        lineLetter = numToLetter(i)
        line = "\033[4m"+lineLetter+(2-len(lineLetter))*" "+"\033[0m"
        for j in range(len(hiddenGrid[0])):
            line+=colorSquare(hiddenGrid[i][j], "  ", "100")
        line+="\033[0;100m|\033[0m | \033[4m"+lineLetter+(2-len(lineLetter))*" "+"\033[0m"
        for j in range(len(grid[0])):
            line+=displaySquare(grid[i][j])
        print(line+"\033[0;44m|\033[0m")

def printGrid(grid) :
    """
    Affiche une grille complète avec les bateaux, sans rien masquer.
    
    Arguments:
    - grid (list) : Grille à afficher complètement.
    
    Retour:
    aucun
    
    Exemple:
    >>> import basicsFunc as b
    >>> grille=b.createEmptyGrid(5)
    >>> printGrid(grille)
    __|1  2  3  4  5  
    A |  |  |  |  |  |
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    <En couleur et partiellement souligné>
    """
    num="\033[4m"
    for i in range(1,1+len(grid[0])):
        num+=str(i)+(3-len(str(i)))*" "
    print("__|"+num+"\033[0m")
    for i in range(len(grid)):
        lineLetter = numToLetter(i)
        line = "\033[4m"+lineLetter+(2-len(lineLetter))*" "+"\033[0m"
        for j in range(len(grid[0])):
            line+=displaySquare(grid[i][j])
        print(line+"\033[0;44m|\033[0m")
