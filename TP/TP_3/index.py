# 1. Liste d'étudiants (chaque étudiant est un dictionnaire)
etudiants = [
    {"nom": "Alice", "age": 20, "moyenne": 12},
    {"nom": "Bob", "age": 19, "moyenne": 9},
    {"nom": "Clara", "age": 21, "moyenne": 14}
]

# 2. Afficher les étudiants admis (moyenne >= 10)
print("Étudiants admis :")

for etudiant in etudiants:             
    if etudiant["moyenne"] >= 10:       
        print(etudiant["nom"])           

# 3. Calculer la moyenne générale de la classe
total = 0                               

for etudiant in etudiants:              
    total = total + etudiant["moyenne"] 

moyenne_classe = total / len(etudiants) 

print("Moyenne générale de la classe :", moyenne_classe)
