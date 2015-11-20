#!/usr/bin/python3
#-*-coding:utf-8 -*

# Bot python pour jouer au touché-coulé.

from random import randrange
import basicsFunc as b

def genCoord(grid):
    """
    Génère une coordonnée aléatoire non déjà jouée.
    
    Arguments:
    - grid (list) : grille de l'adversaire
    
    Retour:
    (tuple) coordonnée générée
    
    Exemple:
    >>> genCoord(grid)
    (2,5)
    """
    coord=(randrange(0,len(grid)),randrange(0,len(grid[0])))
    while grid[coord[0]][coord[1]][1] != None :
        coord=(randrange(0,len(grid)),randrange(0,len(grid[0])))
    return coord
    
def nearGenCoord(grid) :
    """
    Retourne la case à gauche de la case générée au hasard, ou à droite si c'est la case la plus à gauche qui est tirée.
    
    Arguments:
    - grid (list) : grille de l'adversaire
    
    Retour:
    (tuple) coordonnée générée
    
    Exemple:
    >>> nearGenCoord(grid)
    (2,4)
    """
    pos=genCoord(grid)
    if pos[1] != 0 :
        return (pos[0], pos[1]-1)
    else :
        return (pos[0], pos[1]+1)

def validDirection(pos, grid): # Génère la liste des directions randomisées de tir viables d'une position sur une grille.
    """
    Retourne au hasard une liste des directions possible pour la position pos sur la grille grid.
    
    Arguments:
    - pos (tuple) : tuple de position (ligne, colonne)
    - grid (list) : grille
    
    Retour:
    (list) directions possible mélagées ("EAST" ou "WEST" ou "SOUTH" ou "NORTH")
    
    Exemple:
    >>> grid
    [[[None, None], [None, None]], [[None, None], [None, None]]]
    >>> validDirection((0, 0), grid)
    ["SOUTH","EAST"]
    """
    directions=[]
    if pos[1]<len(grid)-1 and grid[pos[0]][pos[1]+1][1]==None :
        directions.append("EAST")
    if pos[1]>0 and grid[pos[0]][pos[1]-1][1]==None :
        directions.append("WEST")
    if pos[0]<len(grid)-1 and grid[pos[0]+1][pos[1]][1]==None :
        directions.append("SOUTH")
    if pos[0]>0 and grid[pos[0]-1][pos[1]][1]==None :
        directions.append("NORTH")
    return b.returnShuffled(directions)

def findDamaged(grid):
    """
    Retourne, si possible, la position d'une case touchée où il y a possibilité de tirer à coté sinon renvoie une case aléatoire.
    
    Arguments:
    - grid (list) : grille
    
    Retour:
    (tuple) position d'une case touchée ou si impossible, une case aléatoire
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "EAST", 2, 1], "T"], [["destroyer", (0,0), "EAST", 2, 1], None]], [[None, None], [None, None]]]
    >>> findDamaged(grid)
    (0,0)
    """
    coordList = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j][1]=="T" and grid[i][j][0][4]!=0 and validDirection((i, j), grid) != []): # Si la case a été touchée, que la vie est != 0 et qu'il y a un tir possible en adjacent
                coordList.append((i, j))
    return b.returnShuffled(coordList)[0] if(coordList != []) else nearGenCoord(grid)

def aimNear(pos, grid):
    """
    Retourne une position adjacente jouable à une position pos sur une grille grid donnée.
    
    Arguments:
    - pos (tuple) : tuple de position
    - grid (list) : grille
    
    Retour:
    (tuple) position jouable et adjacente à pos
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "EAST", 2, 1], "T"], [["destroyer", (0,0), "EAST", 2, 1], None]], [[None, None], [None, None]]]
    >>> aimNear((0,0), grid)
    (0,1)
    """
    direction=validDirection(pos, grid)[0]
    if(direction=="EAST"):
        res=(pos[0], pos[1]+1)
    elif(direction=="WEST"):
        res=(pos[0], pos[1]-1)
    elif(direction=="SOUTH"):
        res=(pos[0]+1, pos[1])
    else :
        res=(pos[0]-1, pos[1])
    return res

# Placement des bateaux
def placeShip(ship, grid) :
    """
    Retourne une position et une direction possible pour un bateau ship sur une grille grid.
    
    Arguments:
    - ship (list) : liste représentant un bateau
    - grid (list) : grille
    
    Retour:
    (tuple) tuple de la forme ((ligne, colonne), direction) pour le placement d'un bateau
    
    Exemple:
    >>> grid
    [[[None, None], [None, None], [[None, None], [None, None]]]
    >>> placeShip(ship, grid)
    ((0, 0), "SOUTH")
    """
    pos=genCoord(grid)
    directions=b.validShipDirections(pos, ship, grid)
    while directions == [] :
        pos=genCoord(grid)
        directions=b.validShipDirections(pos, ship, grid)
    return (pos, directions[0])

# Demande de tir
def askBot(grid):
    """
    retourne la position d'un choix de tir du bot.
    
    Arguments:
    - grid (list) : grille du joueur adverse
    
    Retour:
    (tuple) tuple de position (ligne, colonne)
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "EAST", 2, 1], "T"], [["destroyer", (0,0), "EAST", 2, 1], None]], [[None, None], [None, None]]]
    >>> askBot(grid)
    (1,0)
    """
    posNear=findDamaged(grid)
    return aimNear(posNear, grid)
