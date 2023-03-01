class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def studentInfo(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("id =", self.__num_etudiant)
        print("Niveau =", self.__level)

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Erreur: Le nombre de crédits doit être supérieur à zéro.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Tres bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

john_doe = Student("Doe", "John", 145)
john_doe.add_credits(30)
john_doe.add_credits(35)
john_doe.add_credits(45)
john_doe.studentInfo()