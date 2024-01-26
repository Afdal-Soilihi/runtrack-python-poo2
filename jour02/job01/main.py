class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle
rectangle = Rectangle(10, 5)
print("Longueur:", rectangle.get_longueur())
print("Largeur:", rectangle.get_largeur())

# Modification des valeurs
rectangle.set_longueur(15)
rectangle.set_largeur(8)
print("Nouvelle longueur:", rectangle.get_longueur())
print("Nouvelle largeur:", rectangle.get_largeur())
