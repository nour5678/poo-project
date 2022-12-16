from users.utilisateur import Utilisateur
import pandas as pd


u = Utilisateur('david', "1998-03-26", 'tsgatsga')
u.s_inscrire()

book = pd.read_csv("/Users/daviddede/Downloads/catalogue-bdsl.csv", sep= ";")
print(book)