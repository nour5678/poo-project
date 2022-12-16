#CLASSE RESERVATION
from datetime import datetime
from users.utilisateur import Utilisateur

class Reservation :
    def __init__(self, id : int, jour, heure : datetime, occupe : bool, user: Utilisateur):
        self.id = id
        self.jour = jour
        self.heure = heure
        self.occupe = None
        self.utilisateur = user