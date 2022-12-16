from utilisateur import Utilisateur
import itertools

class Admin(Utilisateur):
    id= itertools.count()
    def __init__(self,nom,birth): # super fonction qui fait appel au constructeur de la classe mere; on a fait appel à la fonction init 
        super().__init__(self,nom,birth)
        stat="admin"
        self.id= next(Admin.id)
    



