# 1. Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase : ")

# Mettre la phrase en minuscules pour simplifier les comparaisons
phrase_min = phrase.lower()

# 2. Compter le nombre de mots
mots = phrase_min.split()      
nb_mots = len(mots)            

print("Nombre de mots :", nb_mots)

# 3. Trouver le mot le plus long
mot_long = ""                  

for mot in mots:               
    if len(mot) > len(mot_long):
        mot_long = mot         

print("Mot le plus long :", mot_long)

# 4. Vérifier si la phrase est un palindrome
phrase_sans_espace = phrase_min.replace(" ", "")

# On inverse la phrase
phrase_inverse = phrase_sans_espace[::-1]

if phrase_sans_espace == phrase_inverse:
    print("La phrase est un palindrome")
else:
    print("La phrase n'est pas un palindrome")
