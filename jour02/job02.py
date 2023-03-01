class Livre:
    
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")
    
livre = Livre("Les Misérables", "Victor Hugo", 1488)

print("Auteur :", livre.get_auteur())
print("Titre :", livre.get_titre())
print("Nombre de pages : ", livre.get_nb_pages())

livre.set_titre("Les Trois Mousquetaires")
livre.set_auteur("Alexandre Dumas")
livre.set_nb_pages(800)

print("Titre modifié : ", livre.get_titre())
print("Auteur modifié : ", livre.get_auteur())
print("Nombre de pages modifié : ", livre.get_nb_pages())

livre.set_nb_pages(-50)

print("Nombre de pages:", livre.get_nb_pages())