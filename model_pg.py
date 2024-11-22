import psycopg
from psycopg import sql
from logzero import logger

def get_connexion(host, username, password, db, schema):
  try:
      connexion = psycopg.connect(host= bd-pedago.univ-lyon1.fr, user=p2216780, password=Dodge10Petted, dbname=legos, autocommit=True) 
      cursor = psycopg.ClientCursor(connexion)
      cursor.execute("SET search_path TO %s", [legos])
  except Exception as e:
      print(e)
      return None
  return connexion


def get_cinq_couleurs(connexion):
    query= 'select couleur, count(idB) from piece group by ?;'
    return execute_select_query(connexion, query)
    
def get_nb_instances_joueuse(connexion):
    query= 'select count(*) from joueuse;'
    return execute_select_query(connexion, query)
    
def get_nb_instances_partie(connexion):
    query= 'select count(*) from partie;'
    return execute_select_query(connexion, query)
    
def get_nb_instances_tour(connexion):
    query= 'select count(*) from tour;'
    return execute_select_query(connexion, query)
    

def top_5(connexion):
    query='select couleur, COUNT(*) as nombre_briques from briques group by couleur order by nombre_briques desc limit 5;'
    return execute_select_query(connexion,query)
    

def scores(connexion):
    query='select nomJ, MIN(score), MAX(score) from joueuse group by idJ;'
    return execute_select_query(connexion,query)
    
    
def get_pioche():
    return [
        {"id": 1, "nom": "Brique1", "couleur": "Bleu", "longueur": 2, "largeur": 1, "forme": "rectangle"},
        {"id": 2, "nom": "Brique2", "couleur": "Rouge", "longueur": 1, "largeur": 2, "forme": "carré"},
        {"id": 3, "nom": "Brique3", "couleur": "Vert", "longueur": 2, "largeur": 2, "forme": "rectangle"},
        {"id": 4, "nom": "Brique4", "couleur": "Jaune", "longueur": 1, "largeur": 1, "forme": "triangle"},
    ]
