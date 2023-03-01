class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "status": "en cours"}

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]["status"] = "annulé"

    def terminer_commande(self):
        self.__statut_commande = "terminée"
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]["status"] = "terminé"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes:
            total += self.__plats_commandes[plat]["prix"]
        return total

    def afficher_commande(self):
        print(f"Commande numéro {self.__numero} - Statut : {self.__statut_commande}")
        for plat in self.__plats_commandes:
            print(f"{plat} ({self.__plats_commandes[plat]['prix']} EUR) - {self.__plats_commandes[plat]['status']}")
        total = self.__calculer_total()
        print(f"Total à payer : {total} EUR")

    def calculer_TVA(self, taux_TVA):
        total = self.__calculer_total()
        TVA = total * taux_TVA
        return TVA
    
commande = Commande(1)
commande.ajouter_plat("Pinte", 10)
commande.ajouter_plat("mauresque", 4)
commande.afficher_commande()
TVA = commande.calculer_TVA(0.2)
print(f"TVA à payer : {TVA} EUR")