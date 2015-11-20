#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Contient les fonctions de base du touché-coulé

from random import shuffle

def returnShuffled(ls) :
    """
    Retourne la liste mélangée.
    
    Arguments:
    - ls (list) : Liste à mélanger
    
    Retour:
    (list) Liste mélangée
    
    Exemple:
    >>> returnShuffled([1,2,3,4])
    [2,4,1,3]
    """
    shuffle(ls)
    return ls

def createEmptyGrid(size) :
    """
    Retourne une grille de taille size vide.
    
    Arguments:
    - size (int) : Taille de la grille
    
    Retour:
    (list) Grille vide
    
    Exemple:
    >>> createEmptyGrid(2)
    [[[None, None],[None, None]],[[None, None],[None, None]]]
    """
    grid=[]
    for i in range(size) :
        grid.append([])
        for j in range(size) :
            grid[i].append([None, None])
    return grid

def isValidCoordInput(coord) :
    """
    Vérifie si coord comprend au moins une lettre et un chiffre.
    
    Arguments:
    - coord (str) : Coordonnée sous forme lettre-chiffere (A1, B6, ...)
    
    Retour:
    (bool) True si comprend minimum une lettre et un chiffre.
    
    Exemple:
    >>> isValidCoordInput("A3")
    True
    >>> isValidCoordInput("56")
    False
    """
    hasLetter=hasNumber=False
    for char in coord :
        if char.isalpha() :
            hasLetter=True
        if char.isdigit() :
            hasNumber=True
    return hasLetter and hasNumber

def letterCoordToNum(letters) :
    """
    Retourne la valeur en base 10 d'un nombre écrit en lettre (base 26) A=0, B=1, ...,Z=25, BA=26, etc.
    
    Arguments:
    - letters (str) : chaine de caractères à transformer en base 10
    
    Retour:
    (int) valeur en base 10 du str entré
    
    Exemple:
    >>> letterCoordToNum("BC")
    28
    """
    res=0
    letters=letters[::-1].upper()
    for i in range(len(letters)) :
        res+=(ord(letters[i])-65)*26**i
    return res

def coordToPos(coord) :
    """
    Retourne une coordonnée entrée par l'utilisateur sous forme d'une position sur la grille.
    
    Arguments:
    - coord (str) : coordonnée utilisateur de la forme ("B7")
    
    Retour:
    (tuple) Tuple de position (ligne, colonne)
    
    Exemple:
    >>> coordToPos("C5")
    (2, 4)
    """
    letters=numbers=""
    for i in coord :
        if i.isalpha() :
            letters+=i
        if i.isdigit() :
            numbers+=i
    return (letterCoordToNum(letters), int(numbers)-1)

def setPosition(position, ship) :
    """
    Assigne la position au bateau ship.
    
    Arguments:
    - position (tuple) : Tuple de position (ligne,colonne)
    - ship (list) : Liste du bateau auquel on assigne la position
    
    Retour:
    Aucun
    
    Exemple:
    >>> ship
    ["destroyer", None, None, 2, 2]
    >>> setPosition((1,3), ship)
    >>> ship
    ["destroyer", (1,3), None, 2, 2]
    """
    ship[1]=position    

def setDirection(direction, ship) : # Directions possibles : NORTH, EAST, SOUTH, WEST
    """
    Assigne la direction au bateau ship.
    
    Arguments:
    - direction (str) : direction (ex: "NORTH", "SOUTH", "EAST", "WEST")
    - ship (list) : Liste du bateau auquel on assigne la direction
    
    Retour:
    Aucun
    
    Exemple:
    >>> ship
    ["destroyer", (1,3), None, 2, 2]
    >>> setDirection("EAST", ship)
    >>> ship
    ["destroyer", (1,3), "EAST", 2, 2]
    """
    ship[2]=direction
    
def setShipVertical(ship, grid) :
    """
    Place le bateau ship verticalement sur la grille grid.
    
    Arguments:
    - ship (list) : liste représentant le bateau
    - grid (list) : grille sur laquelle on place le bateau
    
    Retour:
    Aucun
    
    Exemple:
    >>> ship
    ["destroyer", (0,0), "SOUTH", 2, 2]
    >>> grid
    [[[None, None],[None, None]],[[None, None],[None, None]]]
    >>> setShipVertical(ship, grid)
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[None, None]],[[["destroyer", (0,0), "SOUTH", 2, 2], None],[None, None]]]
    """
    if ship[2] == "NORTH" :
        for i in range(ship[1][0], ship[1][0]-ship[3], -1) :
            grid[i][ship[1][1]]=[ship, None]
    else :
        for i in range(ship[1][0], ship[1][0]+ship[3]) :
            grid[i][ship[1][1]]=[ship, None]

def setShipHorizontal(ship, grid) :
    """
    Place le bateau ship horizontalement sur la grille grid.
    
    Arguments:
    - ship (list) : liste représentant le bateau
    - grid (list) : grille sur laquelle on place le bateau
    
    Retour:
    Aucun
    
    Exemple:
    >>> ship
    ["destroyer", (0,0), "EAST", 2, 2]
    >>> grid
    [[[None, None],[None, None]],[[None, None],[None, None]]]
    >>> setShipHorizontal(ship, grid)
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]]
    """
    if ship[2] == "WEST" :
        for i in range(ship[1][1], ship[1][1]-ship[3], -1) :
            grid[ship[1][0]][i]=[ship, None]
    else :
        for i in range(ship[1][1], ship[1][1]+ship[3]) :
            grid[ship[1][0]][i]=[ship, None]
    
def setShipOnGrid(ship, grid) : # Coordonnée fixe l'arrière du bateau
    """
    Place un bateau ship sur la grille grid.
    
    Arguments:
    - ship (list) : liste représentant le bateau
    - grid (list) : grille sur laquelle on place le bateau
    
    Retour:
    Aucun
    
    Exemple:
    >>> ship
    ["destroyer", (0,0), "EAST", 2, 2]
    >>> grid
    [[[None, None],[None, None]],[[None, None],[None, None]]]
    >>> setShipOnGrid(ship, grid)
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]]
    """
    if ship[2] == "NORTH" or ship[2] == "SOUTH" :
        setShipVertical(ship, grid)
    else :
        setShipHorizontal(ship, grid)

def fireResult(pos, ships, grid) :
    """
    Retourne le résultat d'un tir sur la position pos de la grille grid.
    
    Arguments:
    - pos (tuple) : tuple de position (ligne, colonne)
    - ships (list) : liste contenant les bateaux
    - grid (list) : grille sue laquelle on tire
    
    Retour:
    (str) Résultat du tir ("S"=coulé, "T"=touché, "M"=manqué, "E"=déjà joué)
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]]
    >>> ships
    [["destroyer", (0,0), "SOUTH", 2, 2]]
    >>> fireResult((1,1), ships, grid)
    "M"
    """
    if grid[pos[0]][pos[1]][1] == None :
        if grid[pos[0]][pos[1]][0] in ships :
            if grid[pos[0]][pos[1]][0][4] == 1 : # si coulé (vie sera diminuée de 1 par après)
                return "S"
            else :
                return "T"
        else :
            return "M"
    else :
        return "E"

def updateGrid(pos, ships, grid) :
    """
    Met à jour la grille suite à un tir sur la position pos.
    
    Arguments:
    - pos (tuple) : tuple de position (ligne, colonne)
    - ships (list) : liste contenant les bateaux
    - grid (list) : grille sue laquelle on tire
    
    Retour:
    Aucun
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]]
    >>> ships
    [["destroyer", (0,0), "SOUTH", 2, 2]]
    >>> updateGrid((1,1), ships, grid)
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, "M"]]
    """
    if grid[pos[0]][pos[1]][0] in ships :
        grid[pos[0]][pos[1]][1]="T"
        grid[pos[0]][pos[1]][0][4]-=1
    else :
        grid[pos[0]][pos[1]][1]="M"

def isValidNorth(pos, length, grid) :
    """
    Vérifie si sur la grille grid, il y a bien length cases vides dans la direction Nord depuis la position pos.
    
    Arguments:
    - pos (tuple) : tuple de direction (ligne, colonne)
    - length (int) : longueur sur laquelle il faut vérifier que c'est vide
    - grid (list) : grille
    
    Retour:
    (bool) True si c'est possible, False sinon
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]
    >>> isValidNorth((1,1), 2, grid)
    False
    >>> isValidNorth((1,1), 1, grid)
    True
    """
    for i in range(pos[0], pos[0]-length, -1) :
        if grid[i][pos[1]][0] != None or i<0 :
            return False
    return True

def isValidSouth(pos, length, grid) :
    """
    Vérifie si sur la grille grid, il y a bien length cases vides dans la direction Sud depuis la position pos.
    
    Arguments:
    - pos (tuple) : tuple de direction (ligne, colonne)
    - length (int) : longueur sur laquelle il faut vérifier que c'est vide
    - grid (list) : grille
    
    Retour:
    (bool) True si c'est possible, False sinon
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]
    >>> isValidSouth((1,1), 2, grid)
    False
    >>> isValidSouth((1,1), 1, grid)
    True
    """
    try :
        for i in range(pos[0], pos[0]+length) :
            if grid[i][pos[1]][0] != None :
                return False
    except IndexError:
        return False
    return True

def isValidWest(pos, length, grid) :
    """
    Vérifie si sur la grille grid, il y a bien length cases vides dans la direction Ouest depuis la position pos.
    
    Arguments:
    - pos (tuple) : tuple de direction (ligne, colonne)
    - length (int) : longueur sur laquelle il faut vérifier que c'est vide
    - grid (list) : grille
    
    Retour:
    (bool) True si c'est possible, False sinon
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]
    >>> isValidWest((1,1), 2, grid)
    True
    >>> isValidNorth((0,1), 2, grid)
    False
    """
    for i in range(pos[1], pos[1]-length, -1) :
        if grid[pos[0]][i][0] != None or i<0 :
            return False
    return True

def isValidEast(pos, length, grid) :
    """
    Vérifie si sur la grille grid, il y a bien length cases vides dans la direction Est depuis la position pos.
    
    Arguments:
    - pos (tuple) : tuple de direction (ligne, colonne)
    - length (int) : longueur sur laquelle il faut vérifier que c'est vide
    - grid (list) : grille
    
    Retour:
    (bool) True si c'est possible, False sinon
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "SOUTH", 2, 2], None],[["destroyer", (0,0), "SOUTH", 2, 2], None]],[[None, None],[None, None]]
    >>> isValidEast((0,0), 2, grid)
    False
    >>> isValidEast((1,0), 2, grid)
    True
    """
    try :
        for i in range(pos[1], pos[1]+length) :
            if grid[pos[0]][i][0] != None :
                return False
    except IndexError:
        return False
    return True

def validShipDirections(pos, ship, grid) :
    """
    retourne la liste mélangée des directions valides pour le bateau ship sur la grille grid à la position pos.
    
    Arguments:
    - pos (tuple) : tuple de direction (ligne, colonne)
    - ship (list) : liste représentant le bateau à placer
    - grid (list) : grille
    
    Retour:
    (list) Liste mélangée des direction possibles pour le bateau sur la grille à la position donnée
    
    Exemple:
    >>> grid
    [[[None, None],[None, None]],[[None, None],[None, None]]
    >>> ship
    ["destroyer", (0,0), None, 2, 2]
    >>> validShipDirections((0,0), ship, grid)
    ["SOUTH","EAST"]
    """
    res=[]
    if isValidNorth(pos, ship[3], grid) :
        res.append("NORTH")
    if isValidSouth(pos, ship[3], grid) :
        res.append("SOUTH")
    if isValidWest(pos, ship[3], grid) :
        res.append("WEST")
    if isValidEast(pos, ship[3], grid) :
        res.append("EAST")
    return returnShuffled(res)

def inputToDirection(direction) :
    """
    Transforme une entrée de direction utilisateur en une direction valide.
    
    Arguments:
    - direction (str) : direction à transformer (ex: NORD, B, GAUCHE, G, ...)
    
    Retour:
    (str) Direction valide ("NORTH", "EAST", "WEST", "SOUTH")
    
    Exemple:
    >>> inputToDirection("GAUCHE")
    "WEST"
    """
    if direction in ["NORD", "N", "H", "HAUT"] :
        res="NORTH"
    elif direction in ["SUD", "S", "B", "BAS"] :
        res="SOUTH"
    elif direction in ["OUEST", "O", "G", "GAUCHE", "W"] :
        res="WEST"
    else :
        res="EAST"
    return res

def isItemInGrid(item, grid) :
    """
    Vérifie si un objet se touve dans une des cases de la grille.
    
    Arguments:
    - item (list) : objet à rechercher; notez qu'il pourrait être d'un autre type que list
    - grid (list) : grille dans laquelle la recherche s'effectue
    
    Retour:
    (bool) True si l'objet apparait danns la grille, False sinon
    
    Exemple:
    >>> grid
    [[[["destroyer", (0,0), "EAST", 2, 2], None], [["destroyer", (0,0), "EAST", 2, 2], None]], [[None, None], [None, None]]]
    >>> isItemInGrid(["destroyer", (0,0), "EAST", 2, 2], grid)
    True
    >>> isItemInGrid(["destroyer", (1,0), "NORTH", 2, 2], grid)
    False
    """
    for line in grid :
        for square in line :
            if square[0] is item :
                return True
    return False
