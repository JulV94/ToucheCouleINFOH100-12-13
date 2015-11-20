#!/usr/bin/python3

# -*- coding: utf-8 -*-

# gère le chargement des données pour le touché-coulé

import basicsFunc as b
import os
import formatInfos

#sentences
def loadSentences(fileName) :
    """
    Charge les phrases d'un fichier dans une liste.
    
    Arguments:
    - filename (str) : Chemin du fichier à ouvrir
    
    Retour:
    (list) Liste contenant les phrases
    
    Exemple:
    >>> loadSentences("file.txt")
    ["phrase1", "phrase2", "phrase3"]
    """
    f=open(fileName)
    database=[]
    for line in f :
        database.append(line)
    f.close()
    return database

def createDic() :
    """
    Crée un dictionnaire avec les différents types de phrases.
    
    Arguments:
    Aucun
    
    Retour
    (dict) dictionnaire dont chaque entrée est une liste contenant les phrases d'un type
    
    Exemple:
    >>> createDic()
    {"T":["phraseT1", "phraseT2"], "S":["phraseS1", "phraseS2"], "E":["phraseE1", "phraseE2"], "M":["phraseM1", "phraseM2"]}
    """
    dic={}
    appPath=os.path.split(os.path.abspath(__file__))[0]
    dic["T"]=loadSentences(appPath+"/data/sentences/touchedFile.dat")
    dic["S"]=loadSentences(appPath+"/data/sentences/sunkFile.dat")
    dic["M"]=loadSentences(appPath+"/data/sentences/missedFile.dat")
    dic["E"]=loadSentences(appPath+"/data/sentences/alreadyPlayedFile.dat")
    
    return dic

def say(dic, status) :
    """
    Retourne au hasard une phrase de dic du type status.
    
    Arguments:
    - dic (dict) : dictionnaire d'où on pioche le phrase
    - status (str) : Type de phrase
    
    Retour
    (str) Phrase tirée au hasard
    
    Exemple:
    >>> say({"T":["phraseT1", "phraseT2"], "S":["phraseS1", "phraseS2"], "E":["phraseE1", "phraseE2"], "M":["phraseM1", "phraseM2"]}, "M")
    "phraseM2"
    """
    return b.returnShuffled(dic[status])[0]

#shipsPack
def isValidShipsPack(filename) :
    """
    Vérifie que le fichier de chemin filename est un fichier de pack de bateaux.
    
    Arguments:
    - filename (str) : chemin du fichier à analyser
    
    Retour:
    (bool) True si chaque ligne est bien de la forme : str int int
    
    Exemple:
    file1:
    bateau 1 4
    rafiot 1 2
    
    file2:
    bateau 1 4
    rafiot erreur ?
    
    >>> isValidShipsPack("file1")
    True
    >>> isValidShipsPack("file2")
    False
    """
    try :
        f=open(filename)
        for item in f :
            line=item.split()
            if not(line[1].isdigit() and line[2].isdigit()) :
                return False
        return True
    except IndexError:
        return False
        
def shipsPackFiles() :
    """
    Liste tout les fichiers de pack de bateaux.
    
    Arguments:
    Aucun
    
    Retour:
    (list) liste contenant le nom des fichiers qui sont des packs de bateaux
    
    Exemple:
    >>> shipsPackFiles()
    ["pack1.fleet", "pack2.fleet", "pack3.fleet"]
    """
    files=[]
    os.chdir(os.path.split(os.path.abspath(__file__))[0]+"/data/shipsPacks/")
    for filename in os.listdir() :
        if filename.endswith(".fleet") and isValidShipsPack(os.path.abspath(filename)) :
            files.append(filename)
    return files

def saveChosenPack(packPath) :
    """
    Sauvegarde le chemin du fichier de pack de bateaux packPath.
    
    Arguments:
    - (str) : chemin du pack à sauvegarder
    
    Retour:
    Aucun
    
    Exemple:
    >>> saveChosenPack("/home/user/games/T_C/data/shipsPacks/pack.fleet")
    Pack pack.fleet sélectionné.
    selectedShipsPack.dat:
    /home/user/games/T_C/data/shipsPacks/pack.fleet
    """
    f=open(os.path.split(os.path.abspath(__file__))[0]+"/selectedShipsPack.dat", 'w')
    f.write(packPath)
    f.close()
    print("Pack "+os.path.split(packPath)[1]+" sélectionné.")

def selectedShipsPack() :
    """
    Retourne le chemin du pack sélectionné.
    
    Arguments:
    Aucun
    
    Retour:
    (str) chemin vers le fichier sélectionné
    
    Exemple:
    selectedShipsPack.dat:
    /home/user/games/T_C/data/shipsPacks/pack.fleet
    
    >>> selectedShipsPack()
    "/home/user/games/T_C/data/shipsPacks/pack.fleet"
    """
    f=open(os.path.split(os.path.abspath(__file__))[0]+"/selectedShipsPack.dat")
    res=f.readline()
    f.close()
    return res
    

def menuPacks() :
    """
    Affiche le menu de choix de pack de bateaux et sélectionne un pack si l'utilisateur le choisi.
    
    Arguments:
    Aucun
    
    Retour:
    Aucun
    
    Exemple:
    >>> menPacks()
       __                   __     _                          __ _  
      / /_____  __  _______/ /_  _//        _________  __  __/ ///  
     / __/ __ \/ / / / ___/ __ \/ _ \ ____ / ___/ __ \/ / / / / _ \ 
    / /_/ /_/ / /_/ / /__/ / / /  __//___// /__/ /_/ / /_/ / /  __/ 
    \__/\____/\__,_/\___/_/ /_/\___/      \___/\____/\__,_/_/\___/  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Packs de bateaux disponibles :

                1. aviation.fleet
                2. commerce.fleet
                3. flotte_française_1786.fleet
                4. plaisance.fleet
                5. navires_standard.fleet
                6. manager_énergétique.fleet
                ->
    """
    try :
        formatInfos.printTitle()
        print("\033[1mPacks de bateaux disponibles :\033[0m\n")
        packs=shipsPackFiles()
        for i in range(len(packs)) :
            print("            "+str(i+1)+". "+packs[i])
        choice=formatInfos.inputChoice(packs)
        saveChosenPack(os.path.abspath(packs[choice-1]))
    except (KeyboardInterrupt, EOFError):
        pass

def createShipsList(f) :
    """
    Crée la liste contenant les bateaux.
    
    Arguments
    - (_io.TextIOWrapper) : objet fichier en lecture du pack de bateaux
    
    Retour:
    (list) Liste contenant les bateaux
    
    Exemple:
    >>> f=open("file.fleet")
    >>> createShipsList(f)
    [["porte-avions", None, None, 5, 5],["cuirassé", None, None, 4, 4],["croiseur", None, None, 3, 3], ["sous-marin", None, None, 3, 3], ["destroyer", None, None, 2, 2]]
    """
    database=[]
    for line in f :
        item=line.split()
        for i in range(int(item[1])) :
            database.append([item[0], None, None, int(item[2]), int(item[2])]) # [nom, TuplePosition, direction, longueur, vie]
    return database

def loadShips() :
    """
    Fonction chargeant les bateaux, si impossible d'ouvrir le fichier, un set de bateaux par défaut est retourné.
    
    Arguments:
    Aucun
    
    Retour:
    (list) liste des bateaux
    
    Exemple:
    >>> loadShips()
    [["porte-avions", None, None, 5, 5],["cuirassé", None, None, 4, 4],["croiseur", None, None, 3, 3], ["sous-marin", None, None, 3, 3], ["destroyer", None, None, 2, 2]]
    """
    try :
        f = open(selectedShipsPack())
    except IOError:
        database=[["porte-avions", None, None, 5, 5],["cuirassé", None, None, 4, 4],["croiseur", None, None, 3, 3], ["sous-marin", None, None, 3, 3], ["destroyer", None, None, 2, 2]]
    else :
        database=createShipsList(f)
        f.close()
    finally :
        return database

# shipsPacksCreator
def addShipClass() :
    """
    Retourne la ligne de fichier correspondant à un type de bateau.
    
    Arguments:
    Aucun
    
    Retour:
    (str) Ligne de fichier corresondant à un type de bateau
    
    Exemple:
    >>> addShipClass()
    Entrez le nom de votre navire :bateau
    Quel est la longueur de votre bateau? 4
    Combien de bateau voulez-vous? 2
    bateau 2 4
    """
    name=input("Entrez le nom de votre navire :")
    length=formatInfos.inputInt("Quel est la longueur de votre "+name+"? ")
    quantity=formatInfos.inputInt("Combien de "+name+" voulez-vous? ")
    return name+" "+str(quantity)+" "+str(length)+"\n"

def createPack(filename) :
    """
    Fonction créant un pack de bateaux.
    
    Arguments:
    
    - (str) : nom du fichier qui sera créé
    
    Retour:
    Aucun
    
    Exemple:
    >>> createPack("myPack")
    Entrez le nom de votre navire :bateau
    Quel est la longueur de votre bateau? 4
    Combien de bateau voulez-vous? 2
    Voulez-vous ajouter un autre type de navire? (O/N) :O
    Entrez le nom de votre navire :rafiot
    Quel est la longueur de votre rafiot? 2
    Combien de rafiot voulez-vous? 3
    Voulez-vous ajouter un autre type de navire? (O/N) :N
    myPack.fleet:
    bateau 2 4
    rafiot 3 2
    """
    f=open(os.path.split(os.path.abspath(__file__))[0]+"/data/shipsPacks/"+filename+".fleet", 'w')
    choice="o"
    while choice.lower() in ["o", "oui"] :
        f.write(addShipClass())
        choice=input("Voulez-vous ajouter un autre type de navire? (O/N) :")
    f.close()
    

def packsCreator() :
    """
    Fonction principale du créateur de packs de bateaux.
    
    Arguments:
    Aucun
    
    Retour:
    Aucun
    
    Exemple:
    >>> packsCreator()
       __                   __     _                          __ _  
      / /_____  __  _______/ /_  _//        _________  __  __/ ///  
     / __/ __ \/ / / / ___/ __ \/ _ \ ____ / ___/ __ \/ / / / / _ \ 
    / /_/ /_/ / /_/ / /__/ / / /  __//___// /__/ /_/ / /_/ / /  __/ 
    \__/\____/\__,_/\___/_/ /_/\___/      \___/\____/\__,_/_/\___/  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Bienvenue dans le créateur de packs de bateaux

    Entrez le nom de votre pack :myPack
    Entrez le nom de votre navire :bateau
    Quel est la longueur de votre bateau? 4
    Combien de bateau voulez-vous? 2
    Voulez-vous ajouter un autre type de navire? (O/N) :o
    Entrez le nom de votre navire :rafiot
    Quel est la longueur de votre rafiot? 2
    Combien de rafiot voulez-vous? 3
    Voulez-vous ajouter un autre type de navire? (O/N) :n
    myPack
    Pack myPack.fleet sélectionné.
    """
    formatInfos.printTitle()
    print("\033[1mBienvenue dans le créateur de packs de bateaux\033[0m\n")
    filename=input("Entrez le nom de votre pack :")
    createPack(filename)
    print(filename)
    saveChosenPack(os.path.split(os.path.abspath(__file__))[0]+"/data/shipsPacks/"+filename+".fleet")
    
