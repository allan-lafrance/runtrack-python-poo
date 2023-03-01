class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def viellir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = nom


animal = Animal()
print("L'age de mon animal est : ", animal.age, "ans")


animal.viellir()
print("Il est maintenant âgé de : ", animal.age, "ans")


animal.nommer("Luna")
print("L'animal se nomme : ", animal.nom)