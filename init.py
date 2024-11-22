"""
Ficher initialisation (eg, constantes chargées au démarrage dans la session)
"""

from datetime import datetime
from os import path

SESSION['NOM'] = "Lego Game"
SESSION['BASELINE'] = "Amusez-vous !"
SESSION['CURRENT_YEAR'] = datetime.now().year
SESSION['DIR_HISTORIQUE'] = path.join(SESSION['DIRECTORY'], "historiques")
SESSION['HISTORIQUE'] = dict()
