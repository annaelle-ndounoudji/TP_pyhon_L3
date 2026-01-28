10
12
14
9
15

# 1. Ouvrir le fichier notes.txt en mode lecture (r)
fichier = open("notes.txt", "r")

total = 0         
compteur = 0       

# 2. Lire chaque ligne du fichier
for ligne in fichier:
    note = float(ligne)     
    total = total + note    
    compteur = compteur + 1

fichier.close()    

# Calculer la moyenne
moyenne = total / compteur

# 3. Ouvrir le fichier resultat.txt en mode écriture (w)
resultat = open("resultat.txt", "w")

# Écrire la moyenne dans le fichier
resultat.write("Moyenne de la classe : " + str(moyenne))

resultat.close()   # fermer le fichier après écriture

# Afficher un message à l'écran
print("La moyenne a été enregistrée dans resultat.txt")
