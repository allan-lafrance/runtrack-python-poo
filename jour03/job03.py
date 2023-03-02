class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
        
class ListeDeTaches:
    def __init__(self):
        self.taches = []
        
    def ajouterTache(self, tache):
        self.taches.append(tache)
        
    def supprimerTache(self, tache):
        self.taches.remove(tache)
        
    def marquerCommeFinie(self, tache):
        tache.statut = "terminé"
        
    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.titre} - {tache.description} - {tache.statut}")
        
    def filterListe(self, statut):
        taches_filtrees = []
        for tache in self.taches:
            if tache.statut == statut:
                taches_filtrees.append(tache)
        return taches_filtrees

tache1 = Tache("Faire les courses.", "Acheter du coca, des Doowap et un chargeur.")
tache2 = Tache("commande Amazon", "commander support de casque.")
tache3 = Tache("RDV banque", "Aller a la banque pour la CB.")
tache4 = Tache("Apprendre Python", "Suivre un cours en ligne pour apprendre Python.")

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
liste_taches.ajouterTache(tache4)

liste_taches.afficherListe()

taches_a_faire = liste_taches.filterListe("à faire")
print("Taches à faire : ")
for tache in taches_a_faire:
    print(tache.titre, tache.description, tache.statut)

liste_taches.marquerCommeFinie(tache2)
liste_taches.supprimerTache(tache3)
liste_taches.afficherListe()