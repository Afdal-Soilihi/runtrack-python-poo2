class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats commandés
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        # Vérifier si le plat est déjà dans la commande
        if nom_plat in self.__plats_commandes:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")
        else:
            # Ajouter le plat au dictionnaire avec le prix et le statut
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        print("Commande annulée.")

    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {details_plat['prix']} € ({details_plat['statut']})")
        total = self.calculer_total()
        print(f"Total à payer : {total} €")

    def calculer_tva(self, taux_tva=0.20):
        total = self.calculer_total()
        tva = total * taux_tva
        return tva

# Exemple d'utilisation de la classe Commande
commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Pizza", 10.99)
commande1.ajouter_plat("Salade", 5.99)
commande1.afficher_commande()
