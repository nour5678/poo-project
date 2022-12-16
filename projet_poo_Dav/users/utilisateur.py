from datetime import datetime
import yaml
import itertools
from Classes.biblio import Bibliothhèque
from Classes.reservation import Reservation
from Classes.reservation import Livres 

          

class Utilisateur :

    list_livre = list[Livres]
    list_reservations = list[Reservation]
    # id
    id= itertools.count() # une fonction qui à chaque fois génère un ID 
    #Constructeur
    def __init__(self, nom : str, birth : datetime, stat : str):
        self.nom = nom
        self.naiss = birth
        self.statut = stat
        self.date_enr = datetime.today()
        self.id= next(Utilisateur.id) # next est une fonction qui récupère l'id de la prochaine iterration


    
    #######Méthodes######
    def _emprunter(self, book): #ajouter un conteneur pour la classe Utilisateur
        if book in self.listLivres and len(book) <= 5:
            self.list_livre.append(book)
        else:
            raise Exception("Vous pouvez emprunter un ou plusieurs livres et jusqu'à cinq maximum par emprunt")
        #penser à la gestion des rendez-vous
        #penser à supprimer ce livre de la bibliothèque
    
    def _retourner(self, book):
        if book in self.listLivres and len(book) <= 5:
            self.listLivres.remove(book)
    
    def _se_connecter(): #voir code Bastien 
        #verifier si l'utilisateur est inscrit / parcourir la base de données utilisateur
        pass
    
    def s_inscrire(self):
        #on recupere le fichier yaml
        file = open("config/utlisateurs.yaml")
        cfg = yaml.load(file, Loader=yaml.Loader)
        print(cfg)
    
    def _rechercher():
        pass
    
    def _proposition():
        pass
        #comment gérer les réservations? On réserve pour aller sur place ou pour pour emprunter
        
