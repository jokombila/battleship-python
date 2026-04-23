
"""
Jeu de Bataille Navale - Version 3

Auteurs : Maha Bouslimani et Kombila Jamelia 

"""


import random

# Constantes du jeu
TAILLE_GRILLE = 10
EAU = 0
BARQUE = 1
TORPILLEUR = 2
SOUS_MARIN = 3
CROISEUR = 4
PORTE_AVION = 5
TOUCHE = 11
COULE = 7
MANQUE = 8

SYMBOLS = {
    EAU: ' ',
    BARQUE: 'B',
    TORPILLEUR: 'T',
    SOUS_MARIN: 'S',
    CROISEUR: 'C',
    PORTE_AVION: 'P',
    TOUCHE: '+',
    COULE: 'x',
    MANQUE: '*'
}


FLOTTE = {
    'Barque': BARQUE,
    'Torpilleur': TORPILLEUR,
    'Sous-marin': SOUS_MARIN,
    'Croiseur': CROISEUR,
    'Porte-avion': PORTE_AVION   
}


TAILLES_BATEAUX = {
    BARQUE: 1,
    TORPILLEUR: 2,
    SOUS_MARIN: 3,
    CROISEUR: 4,
    PORTE_AVION: 5
}



def initialiser_grille(grille):
    """ 
        Cree la grille et l’initialise avec des 0.
    """
    for i in range(TAILLE_GRILLE):
        ligne = [EAU] * TAILLE_GRILLE
        grille.append(ligne)
 
    

def afficher_grille(grille):
    """ 
        Affiche la grille avec les solutions
    """
    print("\n")
    # pour afficher les numeros des colonnes
    colonnes = "   "
    for i in range(1, TAILLE_GRILLE + 1):
        colonnes += str(i) + " " 
    print(colonnes) # affiche les numeros en colonnes
    # pour afficher une ligne de separation
    separation = "  " + "-" * (TAILLE_GRILLE * 2 + 1)
    print(separation)

    for index, contenu_lgn in enumerate(grille):      
        ligne = chr(ord('A') + index) + " |"        
        for j in contenu_lgn:
            if j - TOUCHE in SYMBOLS:
               ligne += SYMBOLS[TOUCHE] + "|"  
            else:  # Sinon, on affiche le symbole correspondant
                ligne += SYMBOLS[j] + "|"
        print(ligne)
        print(separation)
    
        
def construire_grille_ordinateur(grille):
    """ 
        Construit et retourne la grille de l'ordinateur 
    """
    lignes_grille = []
    print("\nBataille navale : \n")
    colonnes = "   "
    for i in range(1, TAILLE_GRILLE + 1):
        colonnes += str(i) + " " 
    lignes_grille.append(colonnes)

    separation = "  " + "-" * (TAILLE_GRILLE * 2 + 1)
    lignes_grille.append(separation)

    for index, contenu_lgn in enumerate(grille):
        ligne = chr(ord('A') + index) + " |"
        for j in contenu_lgn:
                if j - TOUCHE in SYMBOLS:
                    ligne += SYMBOLS[TOUCHE] + "|" 
                elif j in {EAU,MANQUE,COULE}:
                    ligne += SYMBOLS[j] + "|"
                else:
                    ligne+=" |"
        lignes_grille.append(ligne) 
        lignes_grille.append(separation)
    
    return lignes_grille



def construire_grille_joueur(grille): 
    """ 
        Construit et retourne la grille du joueur
    """
    lignes_grille = []
    colonnes = "   "*11
    for i in range(1, TAILLE_GRILLE + 1):
        colonnes += str(i) + " " 
    lignes_grille.append(colonnes)
    
    separation = "   "*11 + "-" * (TAILLE_GRILLE * 2 + 1)
    lignes_grille.append(separation)

    for index, contenu_lgn in enumerate(grille):
        ligne = chr(ord('A') + index) + " |"
        for j in contenu_lgn:
            if j - TOUCHE in SYMBOLS:#la case est touche 
               ligne += SYMBOLS[TOUCHE] + "|"  # Affiche "+" pour les cases touchees
            else:  # Sinon, affiche le symbole correspondant
                ligne += SYMBOLS[j] + "|"
        ligne=" " * 31+ligne
        lignes_grille.append(ligne)
        lignes_grille.append(separation)
    return lignes_grille
        


def afficher_grilles_cote_a_cote(grille_o, grille_j):
    """ 
        Affiche la grille de l'ordinateur et du joueur 
    """
    lignes_ordinateur = construire_grille_ordinateur(grille_o)
    lignes_joueur = construire_grille_joueur(grille_j)
    for i in range(len(lignes_ordinateur)):
        print(lignes_ordinateur[i]+lignes_joueur[i])


def case_libre(grille, ligne, col, taille, orientation):
    """ 
        Verifie si les cases necessaires pour placer un bateau sont libres 
        dans la grille.
    """
    if orientation == 'H':
        # Verifier si toutes les cases sur la ligne sont libres
        for i in range(taille):
            if col + i >= TAILLE_GRILLE or grille[ligne][col + i] != EAU:
                return False
    else:  # orientation == 'V'
        # Verifier si toutes les cases sur la colonne sont libres
        for i in range(taille):
            if ligne + i >= TAILLE_GRILLE or grille[ligne + i][col] != EAU:
                return False
    return True


 
def placer_bateaux_joueur(grille): 
    """
        Prend la grille du joueur et place les bateaux 
    """
    for bateau in FLOTTE:  
        type_bateau = FLOTTE[bateau]
        taille=TAILLES_BATEAUX[type_bateau]
        place = False
        
        while not place:
            afficher_grille(grille)  
            
            print(f"\nPlacer votre {bateau} ({taille} case(s)): \n")
            ligne, col = coup(grille)
            
            if taille==1:    # pas besoin de demander l'orientation pour le bateau de taille 1 
                grille[ligne][col] = type_bateau 
                place = True # Placement reussi
                
            else : 
                orientation = input("Horizontale (H) / verticale (V) :").strip().upper()   
                while orientation not in {'H', 'V'}: 
                    orientation = input("\nOrientation invalide. Essayez encore (H/V) : ").strip().upper()
            
                if case_libre(grille, ligne, col, taille, orientation):
                    # Placer le bateau sur la grille
                    for i in range(taille):
                        if orientation == 'H':
                            grille[ligne][col + i] = type_bateau
                        else:  # orientation == 'V'
                            grille[ligne + i][col] = type_bateau
                    place = True
                else:
                    print("\nCertaines cases sont deja occupees ou hors des limites. Essayez encore.")
                    input("\nPour continuer, appuyez sur entree...")
                    
                    
                    
def placer_bateaux_ordinateur(grille):
    """
        Prend la grille de l’ordinateur et place les bateaux 
        dessus de maniere aleatoire.
    """
    # Parcourir chaque bateau de la flotte
    for bateau in FLOTTE:
        # Type du bateau 
        type_bateau = FLOTTE[bateau]
        # Taille du bateau 
        taille = TAILLES_BATEAUX[type_bateau]
        # Initialisation pour le placement
        place = False
        
        # Essaye de placer le bateau jusqu'a reussir
        while not place:
            
            if taille == 1: # Pour le type BARQUE pas besoin de choisir H ou V
                #  Choisir des coordonnees aleatoires 
                ligne = random.randint(0, TAILLE_GRILLE - 1) 
                col = random.randint(0, TAILLE_GRILLE - 1) 
                
                # pas besoin de verifier si la case est libre puisque la grille est initalise avec de l'eau et on commence a placer le bateau de taille 1 
                grille[ligne][col] = type_bateau 
                place = True # Placement reussi
            else:
                # Choisir une orientation aleatoire
                orientation = random.choice(['H', 'V'])
            
                if orientation == 'H':
                    # Coordonnees aleatoires pour une orientation horizontale
                    ligne = random.randint(0, TAILLE_GRILLE - 1)
                    col = random.randint(0, TAILLE_GRILLE - taille)  

                    # Verifier si l'emplacement est libre
                    if case_libre(grille, ligne, col, taille, orientation):
                        # Placer le bateau
                        for i in range(taille):
                            grille[ligne][col + i] = type_bateau
                        place = True  # Placement reussi

                else:  # orientation == 'V'
                    # Coordonnees aleatoires pour une orientation verticale
                    ligne = random.randint(0, TAILLE_GRILLE - taille)
                    col = random.randint(0, TAILLE_GRILLE - 1)

                    # Verifier si l'emplacement est libre
                    if case_libre(grille, ligne, col, taille, orientation):
                        # Placer le bateau
                        for i in range(taille):
                            grille[ligne + i][col] = type_bateau
                        place = True  # Placement reussi

  


def jouer_joueur(grille, i, j):
    """ 
        Permet a l’utilisateur de jouer dans la grille de l’ordinateur et
        renvoie vrai si la partie est terminee, faux sinon.
    """
    if grille[i][j] == EAU:
        grille[i][j] = MANQUE
        print("\nManque")
        
    elif grille[i][j] in {BARQUE, TORPILLEUR, SOUS_MARIN, CROISEUR, PORTE_AVION}:
        type_bateau = grille[i][j]  # Identifier le type de bateau
        grille[i][j] +=TOUCHE  # Marquer la case comme touchee en ajoutant +11

        bateau_coule = True
        for m in range(TAILLE_GRILLE):
            for n in range(TAILLE_GRILLE):
                if grille[m][n] == type_bateau:
                    bateau_coule = False
            
        if bateau_coule:  # Si toutes les cases d'un bateau sont touchees
            print("\nTouche-coule")
            for m in range(TAILLE_GRILLE):
                for n in range(TAILLE_GRILLE):
                    if grille[m][n] == type_bateau + TOUCHE:
                        grille[m][n] = COULE  # Marquer toutes les cases comme COULE
        else:
            print("\nTouche")
    return flotte_coules(grille)



def tir_aleatoire(grille):
    """
        Effectue un tir aleatoire sur une case non encore ciblee
        et renvoie les coordonnees x et y du tir.
    
    """
    while True:
        x = random.randint(0, TAILLE_GRILLE - 1)
        y = random.randint(0, TAILLE_GRILLE - 1)
        if grille[x][y] in {EAU,BARQUE, TORPILLEUR, SOUS_MARIN, CROISEUR, PORTE_AVION}:
            return x, y




def tir_cible(grille, touches_recente, orientation):
    """ 
        Effectue un tir cible autour des cases touchees, en cherchant a determiner la direction du bateau.
    """
    if orientation :
         # Orientation connue, rechercher uniquement dans cette direction
         directions = [orientation, (-orientation[0], -orientation[1])]
    else:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        
    for x, y in touches_recente:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < TAILLE_GRILLE and 0 <= ny < TAILLE_GRILLE and grille[nx][ny] in {EAU, BARQUE, TORPILLEUR, SOUS_MARIN, CROISEUR, PORTE_AVION}:
                return nx, ny
    return tir_aleatoire(grille)  # Si aucune case n'est trouvee autour, tirer aleatoirement




def determiner_orientation(touches_recente):
    """Determine l'orientation du bateau base sur les cases touches recentes."""
    if len(touches_recente) >= 2:
        x1, y1 = touches_recente[0]
        x2, y2 = touches_recente[1]
        if x1 == x2:
            return (0, 1) if y2 > y1 else (0, -1)  
        else:
            return (1, 0) if x2 > x1 else (-1, 0)  
   



def jouer_ordinateur(grille, mode_ciblage, touches_recente):
    """ 
        Permet a l’ordinateur de jouer dans la grille du joueur et
        renvoie vrai si la partie est terminee, faux sinon
        ainsi que les touches recentes de l'ordinateur
    """
    
    
    if mode_ciblage: # Mode ciblage : viser une case autour des cases deja touchees
        orientation = determiner_orientation(touches_recente) 
        i, j = tir_cible(grille,touches_recente,orientation)
    else:
       # Mode recherche aleatoire : tirer sur une case libre au hasard
       i, j = tir_aleatoire(grille)
    
    print(f"\nL'ordinateur a joue en : {chr(i + ord('A'))}{j + 1}")
    
    if grille[i][j] == EAU:
        grille[i][j] = MANQUE

    elif grille[i][j] in {BARQUE, TORPILLEUR, SOUS_MARIN, CROISEUR, PORTE_AVION}:
        type_bateau = grille[i][j]
        grille[i][j] += TOUCHE
        touches_recente.append((i, j))  # Ajouter la case touchee aux recentes
        mode_ciblage = True
        # Verifier si le bateau est completement coule
        bateau_coule = True
        for m in range(TAILLE_GRILLE):
            for n in range(TAILLE_GRILLE):
                if grille[m][n] == type_bateau:
                    bateau_coule = False
                    
        if bateau_coule:
            for m in range(TAILLE_GRILLE):
                for n in range(TAILLE_GRILLE):
                    if grille[m][n] == type_bateau + TOUCHE:
                        grille[m][n] = COULE  # Marquer toutes les cases comme COULE
            touches_recente.clear()  # Si plus de cases à viser, effacer les touches récentes
            mode_ciblage = False  # Passer en mode recherche
    return flotte_coules(grille), touches_recente,mode_ciblage





def flotte_coules(grille):
    """ 
        Verifie si toute la flotte a coule et renvoie 
        True si toute le flotte a coule, False sinon.
    """
    for m in range(TAILLE_GRILLE):
        for n in range(TAILLE_GRILLE):
            if grille[m][n] in {BARQUE, TORPILLEUR, SOUS_MARIN, CROISEUR, PORTE_AVION}:
                return False  #Un bateau intact trouve, la flotte n'est pas coulee
    return True  # Aucun bateau intact trouve, tous sont coules


def coup(grille):
    """ 
        Permet a l’utilisateur de saisir son prochain tir et
        si le tir est correct, elle retourne les coordonnees de ce tir
    """
    
    case_valide=False
    # Demande a l'utilisateur de saisir une case jusqu'a obtenir une case valide
    while not case_valide:
        
        ligne_valide = False 
        # Demande a l'utilisateur de saisir une ligne jusqu'a obtenir une valeur valide
        while not ligne_valide:
            print("\nDans quelle case voulez-vous vous placez ?")
            ligne = input("Ligne (A-J) : ")  # Saisie de la ligne
            ligne = ligne.strip().upper()    # Supprime les espaces inutiles et convertit en majuscules

            # Verifier que la ligne est valide (exactement une lettre entre A et J)
            if len(ligne) == 1 and 'A' <= ligne <= 'J':
                ligne_valide = True
            else:
                print("Ligne invalide. Essayez encore.")
                
        # Convertir l'entree de la ligne en indice pour la grille
        ligne = ord(ligne) - ord('A')  # Convertit la lettre en indice (A=0, B=1, etc.)
        
        col_valide = False
        # Demande a l'utilisateur de saisir la colonne jusqu'a obtenir une valeur valide
        while not col_valide:
            col = input("Colonne (1-10) : ")  # Saisie de la colonne
            col = col.strip()                 # Supprime les espaces inutiles

            # Verifier que la colonne est un chiffre valide
            if col.isdigit() and 1 <= int(col) <= TAILLE_GRILLE:
                col_valide = True
            else:
                print("Colonne invalide. Essayez encore.")
        col = int(col) - 1  # Convertir la colonne en indice (1=0, 2=1, etc.)
        
        if grille[ligne][col] in {MANQUE,COULE} or grille[ligne][col]>TOUCHE:
            print("\nCette case a deja ete vise. Choisissez une autre case.") 
        else:
            case_valide=True
            
    return ligne, col



    
    
def attendre(grille):
    """
        Permet a l'utilisateur de choisir une action et renvoie True si
        l'utilisateur veut continuer de jouer, False sinon.
    """
    choix = input("\nPour continuer, appuyez sur entree (ou 'Q'= quitter, 'S'= afficher la solution)...").strip().upper() 
    if choix == 'Q':
        return False
    elif choix == 'S':
        print("\nSolution de la grille ordinateur: ")
        afficher_grille(grille)
        input("\nAppuyez sur entree pour continuer de jouer...")
    return True



def Jeu():
    """
        Permet le deroulement de la partie entre l'ordinateur et le joueur.
    """
    grille_joueur = []   
    grille_ordinateur = []
   
    # Initialiser les grilles pour le joueur et l'ordinateur
    initialiser_grille(grille_joueur)
    initialiser_grille(grille_ordinateur)
    
    
    placer_bateaux_ordinateur(grille_ordinateur)
    placer_bateaux_joueur(grille_joueur)
    
    rec_touch = [] #liste pour les touche recentes de l'ordinateur
    mode_ciblage = False  # Mode de ciblage de l'ordinateur
    
    tours = 0  # Compteur de tours
    partie_terminee = False  # Variable de controle de la partie
    
    # Boucle principale du jeu
    while not partie_terminee:
        afficher_grilles_cote_a_cote(grille_ordinateur, grille_joueur)
        
        # Obtenir les coordonnees du tir du joueur
        ligne, col = coup(grille_ordinateur)
    
        # Jouer le tir sur la grille de l'ordinateur
        partie_terminee=jouer_joueur(grille_ordinateur, ligne, col)
 
        ordi_gagne, rec_touch ,mode_ciblage= jouer_ordinateur(grille_joueur, mode_ciblage, rec_touch)

        if ordi_gagne:
            afficher_grilles_cote_a_cote(grille_ordinateur, grille_joueur)
            print("\nL'ordinateur a gagne avant vous !")
            return
        
        # Incrementer le compteur de tours
        tours += 1
        
        if not attendre(grille_ordinateur):  # Si l'utilisateur appuie sur 'Q'
           print("\nVous etes sortie du jeu")
           return  # Quitter la fonction Jeu et donc terminer le jeu
    
    #afficher la grille du joueur une derniere fois avant d'annoncer la victoire 
    afficher_grilles_cote_a_cote(grille_ordinateur, grille_joueur)
    print(f"\nFelicitations,vous avez coule tous les bateaux en {tours} tirs !")
        
######################## DEBUT DU JEU #####################################################

Jeu()