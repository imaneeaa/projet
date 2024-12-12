import random
if POST and 'grille' in POST :
    REQUEST_VARS['longueur_l'] = int(POST['longueur'][0])
    REQUEST_VARS['largeur_l'] = int(POST['largeur'][0])
    print(REQUEST_VARS['longueur_l'])
    print(REQUEST_VARS['largeur_l'])
    REQUEST_VARS['longueur_aleatoire'] = random.randint(0, REQUEST_VARS['longueur_l']-1)
    REQUEST_VARS['largeur_aleatoire'] = random.randint(0, REQUEST_VARS['largeur_l']-1)
    REQUEST_VARS['nb_cases'] = REQUEST_VARS['longueur_l']*REQUEST_VARS['largeur_l']
    nb_cibles_min = int(0.1 * REQUEST_VARS['nb_cases'])
    nb_cibles_max = int(0.2 * REQUEST_VARS['nb_cases'])
    REQUEST_VARS['nb_cibles'] = random.randint(nb_cibles_min, nb_cibles_max)
    print("Nombre de cases cibles voulu :", REQUEST_VARS['nb_cibles'])
    REQUEST_VARS['grille'] = [[0 for _ in range(REQUEST_VARS['longueur_l'])] for _ in range(REQUEST_VARS['largeur_l'])]
    
    print("Grille initialisée :")
    for ligne in REQUEST_VARS['grille']:
        print(ligne)
    
    REQUEST_VARS['grille'][REQUEST_VARS['largeur_aleatoire']][REQUEST_VARS['longueur_aleatoire']] = 1 ;
    print("Grille avec 1 case cible ;")
    for ligne in REQUEST_VARS['grille']:
        print(ligne)
        
    liste_direction = [(1,0),(-1,0),(0,1),(0,-1)]
    nbcibleactuel = 1
    
    while nbcibleactuel < REQUEST_VARS['nb_cibles']:
        random.shuffle(liste_direction)
        for dx,dy in liste_direction:
            x = REQUEST_VARS['largeur_aleatoire'] + dx
            y = REQUEST_VARS['longueur_aleatoire'] + dy
            if 0 <= x < REQUEST_VARS['largeur_l'] and 0 <= y < REQUEST_VARS['longueur_l'] and REQUEST_VARS['grille'][x][y] == 0:
                REQUEST_VARS['grille'][x][y] = 1
                REQUEST_VARS['largeur_aleatoire'],REQUEST_VARS['longueur_aleatoire'] = x,y
                nbcibleactuel = nbcibleactuel + 1
                break
        
        else:
            trouver = False
            while not trouver:
                REQUEST_VARS['newlargeur_aleatoire'] = random.randint(0, REQUEST_VARS['largeur_l']-1)
                REQUEST_VARS['newlongueur_aleatoire'] = random.randint(0, REQUEST_VARS['longueur_l']-1)
                if REQUEST_VARS['grille'][REQUEST_VARS['newlargeur_aleatoire']][REQUEST_VARS['newlongueur_aleatoire']]==0:
                    REQUEST_VARS['largeur_aleatoire'],REQUEST_VARS['longueur_aleatoire'] = REQUEST_VARS['newlargeur_aleatoire'], REQUEST_VARS['newlongueur_aleatoire']
                    trouver = True
                    
    print("Grille avec toutes les cases cibles :")
    for ligne in REQUEST_VARS['grille']:
        print(ligne)
                    
                
    
    
    