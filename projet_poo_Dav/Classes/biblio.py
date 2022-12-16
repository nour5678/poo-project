from datetime import datetime
from livre import Livre
#CLASSE BIBLIO    
class Bibliothhèque :

    listLivres = list[Livre]
    def __init__(self, id, nom : str, lieu : str, ouverture : datetime, fermeture : datetime):
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.horaires_ouverture = {
            "ouverture" : ouverture,
            "fermeture" : fermeture
        }

    ##setters
    