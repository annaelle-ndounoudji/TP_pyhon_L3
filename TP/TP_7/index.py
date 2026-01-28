# Création de la classe Etudiant
class Etudiant:

    # Méthode spéciale appelée lors de la création d'un étudiant
    def __init__(self, nom, matricule, notes):
        self.nom = nom              
        self.matricule = matricule  
        self.notes = notes          

    # Méthode pour calculer la moyenne
    def calculer_moyenne(self):
        total = 0                  
        for note in self.notes:     
            total = total + note
        moyenne = total / len(self.notes)
        return moyenne             

    # Méthode pour afficher les informations de l'étudiant
    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Matricule :", self.matricule)
        print("Notes :", self.notes)
        print("Moyenne :", self.calculer_moyenne())
