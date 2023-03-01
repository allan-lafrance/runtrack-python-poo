class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50
        
    def get_marque(self):
        return self.__marque
        
    def set_marque(self, marque):
        self.__marque = marque
        
    def get_modele(self):
        return self.__modele
        
    def set_modele(self, modele):
        self.__modele = modele
        
    def get_annee(self):
        return self.__annee
        
    def set_annee(self, annee):
        self.__annee = annee
        
    def get_km(self):
        return self.__km
        
    def set_km(self, km):
        self.__km = km
        
    def est_en_marche(self):
        return self.__en_marche
        
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Le réservoir est presque vide")
        
    def arreter(self):
        self.__en_marche = False
        
    def __verifier_plein(self):
        return self.__reservoir > 5
    
car = Voiture('Toyota', 'Hilux', 1998, 600000)

print('Marque :', car.get_marque())
print('Modèle :', car.get_modele())
print('Année :', car.get_annee())
print('nombre de kilomètres au compteur :', car.get_km())