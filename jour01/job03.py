class Operation:
    def __init__(self, nombre1=8, nombre2=10):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print("Le resultat est : ", result)

operation = Operation()
operation.addition()