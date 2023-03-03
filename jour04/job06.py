class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}, Année : {self.annee}, Prix : {self.prix}")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")
    
    def demarrer(self):
        print("La voiture démarre pas !")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")
    
    def demarrer(self):
        print("La moto démarre !")

voiture1 = Voiture("Renault", 2020, 10000)
voiture1.informationsVehicule()
voiture1.demarrer()


moto1 = Moto("kawasaki", 2021, 12000)
moto1.informationsVehicule()
moto1.demarrer()
