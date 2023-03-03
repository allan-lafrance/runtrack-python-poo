class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f'Âge : {self.age}')

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere, age):
        self.matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")


eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.affichageAge()
professeur1 = Professeur("math", age=40)
professeur1.bonjour()
professeur1.enseigner()
