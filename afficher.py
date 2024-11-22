from model.model_pg import get_cinq_couleurs
cinq_couleur = get_cinq_couleurs(SESSION['CONNEXION'])
REQUEST_VARS['couleurs'] = cinq_couleurs


from model.model_pg import get_nb_instances_joueuse
nb_instances_joueuse = get_nb_instances_joueuse(SESSION['CONNEXION'])
RESQUEST_VARS['nb_instances_j'] = nb_instances_joueuse


from model.model_pg import get_nb_instances_partie
nb_instances_partie = get_nb_instances_partie(SESSION['CONNEXION'])
REQUEST_VARS['nb_instances_p'] = nb_instances_partie


from model.model_pg import get_nb_instances_tour
nb_instances_tour = get_nb_instances_tour(SESSION['CONNEXION'])
REQUEST_VARS['nb_instances_t'] = nb_instances_tour
