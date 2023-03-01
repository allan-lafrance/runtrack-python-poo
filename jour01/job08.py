class Cercle:
    
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print(f"le cercle a un rayon de : {self.rayon}")
    
    def circonference(self):
        return 2 * 3.14159 * self.rayon
    
    def aire(self):
        return 3.14159 * self.rayon**2
    
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print("la circonférence est de :", cercle1.circonference())
print("un diamètre de :", cercle1.diametre())
print("une aire de :", cercle1.aire())

cercle2.afficherInfos()
print("la circonférence est de :", cercle2.circonference())
print("un diamètre de :", cercle2.diametre())
print("une aire de :", cercle2.aire())