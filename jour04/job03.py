class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

#rectangle
rectangle1 = Rectangle(10, 5)
rectangle1.set_longueur(10)
rectangle1.set_largeur(5)

print("Périmètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())
print("Longueur du rectangle :", rectangle1.get_longueur())
print("Largeur du rectangle :", rectangle1.get_largeur())


#parallélépipède
parallelepiped1 = Parallelepipede(6, 5, 3)
parallelepiped1.set_hauteur(3)

print("Périmètre du parallélépipède :", parallelepiped1.perimetre())
print("Surface du parallélépipède :", parallelepiped1.surface())
print("Volume du parallélépipède :", parallelepiped1.volume())
print("Hauteur du parallélépipède :", parallelepiped1.get_hauteur())
