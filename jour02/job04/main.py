class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Numéro d'étudiant: {self.__numero_etudiant}")
        print(f"Niveau: {self.student_eval()}")

# Création d'un étudiant
john_doe = Student("John", "Doe", 145)
john_doe.add_credits(30)
john_doe.add_credits(40)
john_doe.add_credits(25)
print("Total de crédits de John Doe:", john_doe.student_info())
