import math

class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * self.radius ** 2
cercle1 = Cercle(2)
print(f"L'aire du cercle est de {cercle1.aire()}")
    
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle1 = Rectangle(10, 5)
print(f"L'aire est de {rectangle1.aire()}")
