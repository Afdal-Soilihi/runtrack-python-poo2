class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  # Nouvel attribut ajouté, initialisé par défaut à True

    # Assesseurs
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def est_disponible(self):
        return self.__disponible

    # Mutateurs
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():
            print("Emprunt du livre en cours...")
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            print("Rendu du livre en cours...")
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté, impossible de le rendre.")

    # Afficher les attributs
    def afficher_livre(self):
        print(f"Titre: {self.__titre}")
        print(f"Auteur: {self.__auteur}")
        print(f"Nombre de pages: {self.__nb_pages}")
        print(f"Disponible: {self.__disponible}")


# Exemple d'utilisation
livre1 = Livre("Harry Potter", "J.K. Rowling", 500)
livre1.afficher_livre()

# Emprunter le livre
livre1.emprunter()
livre1.afficher_livre()

# Rendre le livre
livre1.rendre()
livre1.afficher_livre()