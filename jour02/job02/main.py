class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Assesseurs
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

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

    # Afficher les attributs
    def afficher_livre(self):
        print(f"Titre: {self.__titre}")
        print(f"Auteur: {self.__auteur}")
        print(f"Nombre de pages: {self.__nb_pages}")
    
    # Exemple d'utilisation
livre1 = Livre("Harry Potter", "J.K. Rowling", 500)
livre1.afficher_livre()

# Modifier le titre
livre1.set_titre("Le Seigneur des Anneaux")
livre1.afficher_livre()

# Modifier le nombre de pages
livre1.set_nb_pages(700)
livre1.afficher_livre()

# Tentative de définir un nombre de pages négatif (affiche un message d'erreur)
livre1.set_nb_pages(-50)
livre1.afficher_livre()