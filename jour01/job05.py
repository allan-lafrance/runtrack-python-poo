class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont: {self.x}, {self.y}")

    def afficherX(self):
        print(f"La valeur du point x est : {self.x}")

    def afficherY(self): 
        print(f"La valeur du point y est : {self.y}")

    def changerX(self, newX):
        self.x = newX

    def changerY(self, newY):
        self.y = newY


p = Point(3, 5)
p.afficherLesPoints()
p.afficherX()
p.afficherY()
p.changerX(1)
p.changerY(15)
p.afficherLesPoints()