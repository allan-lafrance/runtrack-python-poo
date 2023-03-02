class Ville:
    def __init__(self, nom, nb_habitants):
        self.nom = nom
        self.nb_habitants = nb_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.nb_habitants += 1

ville_paris = Ville("Paris", 1000000)
print("Population de la ville de Paris:", ville_paris.nb_habitants)

ville_marseille = Ville("Marseille", 861635)
print("Population de la ville de Marseille:", ville_marseille.nb_habitants)


john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()


print("Mise a jour de la population de la ville de Paris:", ville_paris.nb_habitants)
print("Mise a jour de la population de la ville de Marseille:", ville_marseille.nb_habitants)