from datetime import datetime 
from biblio import Bibliothhèque
from Classes.reservation import Reservation
from users.utilisateur import Utilisateur


#CLASSE LIVRE
class Livre : 
    def __init__(self, id :int, title : str, author, edi : str, genre, biblio:Bibliothhèque, user : Utilisateur):
        self.id = id(self)
        self.titre = title
        self.auteurs = []
        self.edition = edi
        self.date_enregistrement = datetime.ctime
        self.genre = []
        self.biblio = biblio
        self.user = None

    
