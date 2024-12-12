from model.model_pg import get_random_briques
from model.model_pg import execute_select_query

if 'pioche_briques' not in REQUEST_VARS:
    REQUEST_VARS['pioche_briques'] = []
if 'selected_brique' not in REQUEST_VARS:
    REQUEST_VARS['selected_brique'] = None
    

if POST and 'selectionner_brique' in POST:
    selected_id = int(POST['id_brique'][0])
    connexion = SESSION['CONNEXION']
    
    selected_query = "SELECT idb, nomb, longueur, largeur, couleur FROM brique WHERE idb = %s"
    selected_brique = execute_select_query(connexion, selected_query, [selected_id])
    if selected_brique:
        REQUEST_VARS['selected_brique'] = selected_brique[0]
        
    
    idB_exclus = [b[0] for b in REQUEST_VARS['pioche_briques']]
    idB_exclus.append(selected_id)
    new_briques = get_random_briques(connexion, idB_exclus=idB_exclus)
    if new_briques:
        REQUEST_VARS['pioche_briques'] = new_briques
        
else:
    connexion = SESSION['CONNEXION']
    REQUEST_VARS['pioche_briques'] = get_random_briques(connexion)