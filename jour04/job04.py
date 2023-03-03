class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle1 = Rectangle(10, 5)
print(f"L'aire est de {rectangle1.aire()}")