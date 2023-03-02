class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.numero_compte = numero_compte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print("Information du compte :")
        print(f"Numéro de compte : {self.numero_compte}")
        print(f"Titulaire : {self.prenom} {self.nom}")
        print(f"Solde : {self.solde} euros")

    def afficherSolde(self):
        print(f"Le solde du compte est de {self.solde} euros")

    def versement(self, montant):
        self.solde += montant
        print(f"{montant} euros ont été ajoutés au compte")
        self.afficherSolde()

    def retrait(self, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Vous n'avez pas suffisamment d'argent sur votre compte pour effectuer cette opération")
            return
        self.solde -= montant
        print(f"{montant} euros ont été retirés du compte")
        self.afficherSolde()

    def agios(self):
        if self.solde < 0:
            frais = self.solde * 0.1
            self.solde += frais
            print(f"Des frais d'agios de {frais} euros ont été appliqués")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Vous n'avez pas suffisamment de fond sur votre compte pour effectuer cette opération")
            return
        self.solde -= montant
        compte_destinataire.solde += montant
        print(f"Le virement de {montant} euros a été effectué vers le compte de {compte_destinataire.nom} {compte_destinataire.prenom}")
        self.afficherSolde()


compte1 = CompteBancaire("789637608", "Dupont", "Jean", 1000)
compte1.afficher()
compte1.versement(500)
compte1.retrait(200)

compte2 = CompteBancaire("797664008",  "Dupont", "Marie", -500, True)
compte2.agios()
compte1.virement(compte2, 300)