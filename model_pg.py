import psycopg
from psycopg import sql
from logzero import logger

def execute_select_query(connexion, query, params=[]):
    """
    Méthode générique pour exécuter une requête SELECT (qui peut retourner plusieurs instances).
    Utilisée par des fonctions plus spécifiques.
    """
    with connexion.cursor() as cursor:
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result 
        except psycopg.Error as e:
            logger.error(e)
    return None
    
# Statistiques
def get_nb_instance_b(connexion):
    query = 'select count(*) from projet.brique;'
    return execute_select_query(connexion, query)
    
def get_nb_instance_j(connexion):
    query = 'select count(*) from projet.joueuse;'
    return execute_select_query(connexion, query)
    
def get_nb_instance_p(connexion):
    query = 'select count(*) from projet.partie;'
    return execute_select_query(connexion, query)
    
def top5(connexion):
    query = 'SELECT pcouleur, COUNT(*) AS nb_briques FROM projet.brique GROUP BY couleur ORDER BY nb_briques DESC LIMIT 5;'
    return execute_select_query(connexion,query)

import random

def get_random_briques(connexion, idB_exclus=[]):
    # Choisis aléatoirement 4 briques pas encore utilisées dont la longueur et/ou la largeur <=2 
    condition = ""
    if idB_exclus:
        condition = f"AND idb NOT IN ({','.join(map(str, idB_exclus))})"

    query = f"""
        SELECT idB, nomB, longueur, largeur, couleur 
        FROM brique 
        WHERE longueur <= 2 OR largeur <= 2 
        {condition}
        ORDER BY RANDOM()
        LIMIT 4;
    """
    return execute_select_query(connexion, query)






















