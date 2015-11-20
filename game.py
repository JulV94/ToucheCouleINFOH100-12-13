#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Jeu du Touché-Coulé

import basicsFunc as b
import bot
import formatInfos as f
import dataManagement as d
from time import sleep

CLR_SCR="\x1b[1J"

def playerPlaceShips(ships, grid) :
    """
    Laisse l'utilisateur placer sa flotte (ships) sur sa grille de jeu (grid).
    
    Arguments:
    - ships (list) : Liste des bateaux de l'utilisateur.
    - grid (list) : Grille de jeu de l'utilisateur.
    
    Retour:
    aucun
    
    Exemple:
    >>> from basicsFunc import createEmptyGrid
    >>> flotte=[["porte-avions",None,None,5,5],["cuirassé",None,None,4,4],["croiseur",None,None,2,2]]
    >>> grille=b.createEmptyGrid(5)
    >>> playerPlaceShips(flotte, grille)
    Bateaux à placer : 
    porte-avions (5), cuirassé (4), croiseur (3)

    Votre secteur
    __|1  2  3  4  5  
    A |  |  |  |  |  |
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    Placement de : porte-avions (5 cases)
    Entrez la case :A1
    Entrez la direction :d
    Bateaux à placer : 
    cuirassé (4), croiseur (3)

    Votre secteur
    __|1  2  3  4  5  
    A |po|po|po|po|po|
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    Placement de : cuirassé (4 cases)
    Entrez la case :E1
    Entrez la direction :h
    Bateaux à placer : 
    croiseur (3)

    Votre secteur
    __|1  2  3  4  5  
    A |po|po|po|po|po|
    B |cu|  |  |  |  |
    C |cu|  |  |  |  |
    D |cu|  |  |  |  |
    E |cu|  |  |  |  |
    Placement de : croiseur (3 cases)
    Entrez la case :C3
    Entrez la direction :d
    Placement terminé
    <En couleur, et avec ClearScreen>
    """
    for ship in ships :
        print(CLR_SCR+"\033[1mBateaux à placer : \033[0m\n"+f.remainingShipsToPlace(ships, grid)+"\n\n\033[1mVotre secteur\033[0m")
        f.printGrid(grid)
        print("Placement de :", ship[0], "("+str(ship[3])+" cases)")
        pos=f.inputPosShip(ship, grid)
        direction=f.inputDirectionShip(pos, ship, grid)
        b.setPosition(pos, ship)
        b.setDirection(direction, ship)
        b.setShipOnGrid(ship, grid)
    print(CLR_SCR+"Placement terminé")

def botPlaceShips(ships, grid) :
    """
    Place les navires (ships) du bot sur sa grille de jeu (grid).
    Utilise la fonction placeShip du bot.
    
    Arguments:
    - ships (list) : Liste des navires du bot.
    - grid (list) : Grille du bot.
    
    Retour:
    aucun
    
    Exemple:
    >>> from formatInfos import printGrid
    >>> flotte=[["bateau1",(None,None),None,3,3],["bateau2",(None,None),None,2,2],["bateau3",(None,None),None,1,1]]
    >>> grille = b.createEmptyGrid(5)
    >>> botPlaceShips(flotte, grille)
    >>> printGrid(grille)
    __|1  2  3  4  5  
    A |  |  |ba|  |  |
    B |  |  |ba|  |  |
    C |  |ba|  |  |  |
    D |  |ba|  |  |  |
    E |ba|ba|  |  |  |
    <En couleur>
    """
    for ship in ships :
        ans=bot.placeShip(ship, grid)
        b.setPosition(ans[0], ship)
        b.setDirection(ans[1], ship)
        b.setShipOnGrid(ship, grid)

def playerFire(botShips, botGrid, playerGrid, dic) :
    """
    Un seul tir de l'utilisateur.
    Affiche les deux grilles (botGrid & playerGrid) avec une phrase aléatoire provenant de (dic),
    et laisse le joueur choisir une coordonnée de tir pour viser les navires du bot (botShips).
    
    Arguments:
    - botShips (list) : Liste des navires du bot.
    - botGrid (list) : Grille du bot.
    - playerGrid (list) : Grille de l'utilisateur.
    - dic (dict) : Dictionnaire aléatoire des phrases de commentaire.
    
    Retour:
    aucun
    
    Exemple:
    <Initialisation de flotteBot, flotteJoueur, grilleBot, grilleJoueur, dic, etc.>
    >>> playerFire(flotteBot, grilleBot, grilleJoueur, dic)
    Secteur adverse                   | Votre secteur
    __|1  2  3  4  5  6  7  8  9  10  | __|1  2  3  4  5  6  7  8  9  10 
    A |  |  |  |  |  |  |  |  |  |  | | A |  |  |  |  |  |  |  |  |  |  |
    B |  |  |  |  |  |  |  |  |  |  | | B |  |  |  |  |  |  |ba|  |  |  |
    C |  |  |  |  |  |  |  |  |  |  | | C |  |  |  |  |  |  |ba|  |  |  |
    D |  |  |  |  |  |  |  |  |  |  | | D |  |ba|ba|  |  |  |  |  |  |  |
    E |  |  |  |  |  |  |  |  |  |  | | E |  |  |  |  |  |  |  |  |  |  |
    F |  |  |  |  |  |  |  |  |  |  | | F |  |  |  |  |  |ba|ba|ba|  |  |
    G |  |  |  |  |  |  |  |  |  |  | | G |  |  |  |  |  |  |  |  |  |  |
    H |  |  |  |  |  |  |  |  |  |  | | H |  |  |  |  |  |  |  |  |  |  |
    I |  |  |  |  |  |  |  |  |  |  | | I |  |  |  |  |  |  |  |  |  |  |
    J |  |  |  |  |  |  |  |  |  |  | | J |  |  |  |  |  |  |  |  |  |  |
    Entrez la case :DC5
    Coordonnée hors de la grille
    Entrez la case :quoi???
    Coordonnée invalide
    Entrez la case :F7
    <En couleur, et avec ClearScreen>
    """
    f.printTwoGrids(botGrid, playerGrid)
    pos=f.inputCoord(botGrid)
    res=b.fireResult(pos, botShips, botGrid)
    while res == "E" :
        print(d.say(dic, "E"))
        pos=f.inputCoord(botGrid)
        res=b.fireResult(pos, botShips, botGrid)
    b.updateGrid(pos, botShips, botGrid)
    return res

def playerTurn(botShips, botGrid, playerGrid, dic) :
    """
    Un tour de jeu de l'utilisateur.
    Affiche les deux grilles (botGrid & playerGrid) avec une phrase aléatoire provenant de (dic),
    et laisse le joueur choisir une coordonnée de tir pour viser les navires du bot (botShips).
    
    Arguments:
    - botShips (list) : Liste des navires du bot.
    - botGrid (list) : Grille du bot.
    - playerGrid (list) : Grille de l'utilisateur.
    - dic (dict) : Dictionnaire aléatoire des phrases de commentaire
    
    Retour:
    aucun
    
    Exemple:
    <Après initialisation de flotteBot, grilleBot, grilleJoueur, dic, etc.>
    >>> playerTurn(flotteBot, grilleBot, grilleJoueur, dic)
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    Entrez la case :D5
    Message du QG: 'Mais qu'attendez-vous pour les éliminer?'
    <En couleur, et avec ClearScreen>
    """
    res=playerFire(botShips, botGrid, playerGrid, dic)
    while not(areAllSunk(botShips)) and res != "M" :
        if res=="T" :
            print(CLR_SCR+d.say(dic, "T"))
        else :
            print(CLR_SCR+d.say(dic, "S"))
        res=playerFire(botShips, botGrid, playerGrid, dic)
    if res=="M" :
        print(CLR_SCR+d.say(dic, "M"))

def botFire(playerShips, playerGrid, botGrid) :
    """
    Un seul tir du bot. Ajourne la grille du joueur avec updateGrid.
    Affiche les deux grilles avec le nouveau tir du bot.
    
    Arguments:
    - playerShips (list) : Liste des navires de l'utilisateur.
    - playerGrid (list) : Grille de l'utilisateur.
    - botGrid (list) : Grille du bot.
    
    Retour:
    (str) Résultat du tir du bot : "M", "T", ou "S".
    
    Exemple:
    >>> from basicsFunc import createEmptyGrid
    >>> flotteJoueur=[["bateau1",(None,None),None,3,3],["bateau2",(None,None),None,2,2],["bateau3",(None,None),None,1,1]]
    >>> grilleJoueur=b.createEmptyGrid(5)
    >>> grilleBot=b.createEmptyGrid(5)
    >>> botPlaceShips(flotteBot, grilleBot)
    >>> botFire(flotteJoueur, grilleJoueur, grilleBot)
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |  |  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    'M'
    <En couleur, et avec ClearScreen>
    """
    pos=bot.askBot(playerGrid)
    res=b.fireResult(pos, playerShips, playerGrid)
    b.updateGrid(pos, playerShips, playerGrid)
    f.printTwoGrids(botGrid, playerGrid)
    return res

def botTurn(playerShips, playerGrid, botGrid) :
    """
    Un tour de jeu entier du bot.
    Affiche les deux grilles (botGrid & playerGrid)
    avec une phrase de commentaire en fonction du succès ou de l'.
    
    Arguments:
    - playerShips (list) : Liste des navires de l'utilisateur.
    - playerGrid (list) : Grille de l'utilisateur.
    - botGrid (list) : Grille du bot.
    
    Retour:
    aucun
    
    Exemple:
    >>> from basicsFunc import createEmptyGrid
    >>> flotteJoueur=[["bateau1",(None,None),None,3,3],["bateau2",(None,None),None,2,2],["bateau3",(None,None),None,1,1]]
    >>> grilleJoueur=b.createEmptyGrid(5)
    >>> grilleBot=b.createEmptyGrid(5)
    >>> botPlaceShips(flotteBot, grilleBot)
    >>> botTurn(flotteJoueur, grilleJoueur, grilleBot)
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |  |  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    L'adversaire vous a manqué
    <En couleur, et avec ClearScreen>
    """
    res=botFire(playerShips, playerGrid, botGrid)
    sleep(2.5)
    while not(areAllSunk(playerShips)) and res != "M" :
        if res=="T" :
            print(CLR_SCR+"L'un de vos bâtiments à été touché!")
        else :
            print(CLR_SCR+"L'un de vos bâtiments à été coulé!")
        res=botFire(playerShips, playerGrid, botGrid)
        sleep(2)
    if res=="M" :
        print(CLR_SCR+"L'adversaire vous a manqué!")

def areAllSunk(ships) :
    """
    Vérifie si les bateaux (ships) sont entièrement coulés ou pas.
    
    Arguments:
    - ships (list) : Liste de navires.
    
    Retour:
    (bool) True si les navires (ships) sont tous coulés, False sinon.
    
    Exemple:
    >>> areAllSunk([["bateau1",(None,None),None,3,0],["bateau2",(None,None),None,2,0],["bateau3",(None,None),None,1,1]])
    False
    >>> areAllSunk([["bateau1",(None,None),None,3,0],["bateau2",(None,None),None,2,0],["bateau3",(None,None),None,1,0]])
    True
    """
    for ship in ships :
        if ship[4] != 0 :
            return False
    return True

def gameResult(ships, botGrid, playerGrid) :
    """
    Affiche les deux grilles complètement visibles du bot et du joueur
    pour visualiser l'emplacement de chaque bateau en fin de partie.
    Affiche également le résultat de fin du jeu Touché-Coulé.
    
    Arguments:
    - ships (list) : Liste des navires du bot.
    - botGrid (list) : Grille du bot.
    - playerGrid (list) : Grille de l'utilisateur.
    
    Retour:
    aucun
    
    Exemple:
    >>> from basicsFunc import *
    >>> flotteBot=[["bateau1",(None,None),None,3,3],["bateau2",(None,None),None,2,2],["bateau3",(None,None),None,1,1]]
    >>> grilleJoueur=b.createEmptyGrid(5)
    >>> grilleBot=b.createEmptyGrid(5)
    >>> gameResult(flotteBot, grilleBot, grilleJoueur)
    Secteur adverse
    __|1  2  3  4  5  
    A |  |  |  |  |  |
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    Votre secteur
    __|1  2  3  4  5  
    A |  |  |  |  |  |
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    Vous avez perdu
    <En couleur, et avec ClearScreen>
    """
    print(CLR_SCR+"\033[1mSecteur adverse\033[0m")
    f.printGrid(botGrid)
    print("\033[1mVotre secteur\033[0m")
    f.printGrid(playerGrid)
    if areAllSunk(ships) :
        print("Vous avez gagné")
    else :
        print("Vous avez perdu")

def gameKernel(botShips, playerShips, botGrid, playerGrid, sentences) :
    """
    Noyau du jeu du Touché-Coulé : boucle principale du jeu.
    Cycle tour par tour tant que l'une des deux flottes (playerShips, botShips) n'est pas entièrement coulée.
    
    Arguments:
    - botShips (list) : Liste des navires du bot.
    - playerShips (list) : Liste des navires de l'utilisateur.
    - botGrid (list) : Grille du bot.
    - playerGrid (list) : Grille de l'utilisateur.
    - sentences (dict) : Dictionnaire aléatoire des phrases de commentaire.
    
    Retour:
    aucun    
    """
    while not(areAllSunk(playerShips) or areAllSunk(botShips)) :
        playerTurn(botShips, botGrid, playerGrid, sentences)
        if not(areAllSunk(botShips)) :
            botTurn(playerShips, playerGrid, botGrid)

def game() :
    """
    Jeu du Touché-Coulé.
    
    Arguments:
    aucun
    
    Retour:
    aucun
    
    Exemple:
    >>> game()
    Entrez la taille de la grille voulue :5
    Votre secteur
    __|1  2  3  4  5  
    A |  |  |  |  |  |
    B |  |  |  |  |  |
    C |  |  |  |  |  |
    D |  |  |  |  |  |
    E |  |  |  |  |  |
    Placement de : bouée-de-sauvetage (1 cases)
    Entrez la case :D2
    Entrez la direction :n
    Placement terminé
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    Entrez la case :D5
    Message du QG: 'Mais qu'attendez-vous pour les éliminer?'
    
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    L'adversaire vous a manqué
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    Entrez la case :C2
    Nous les aurons bien un jour!
    
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    L'adversaire vous a manqué
    Secteur adverse    | Votre secteur
    __|1  2  3  4  5   | __|1  2  3  4  5  
    A |  |  |  |  |  | | A |  |  |  |  |  |
    B |  |  |  |  |  | | B |  |  |  |  |  |
    C |  |  |  |  |  | | C |  |  |  |  |  |
    D |  |  |  |  |  | | D |  |bo|  |  |  |
    E |  |  |  |  |  | | E |  |  |  |  |  |
    Entrez la case :
    Partie interrompue
    <En couleur, et avec ClearScreen>
    """
    try :
        playerShips, botShips = d.loadShips(), d.loadShips()
        sentences, size = d.createDic(), f.inputSizeGrid(playerShips)
        playerGrid, botGrid = b.createEmptyGrid(size), b.createEmptyGrid(size)
        botPlaceShips(botShips, botGrid)
        playerPlaceShips(playerShips, playerGrid)
        gameKernel(botShips, playerShips, botGrid, playerGrid, sentences)
        gameResult(botShips, botGrid, playerGrid)
    except (KeyboardInterrupt, EOFError):
        print("\nPartie interrompue")
