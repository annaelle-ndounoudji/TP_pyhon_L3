# Fonction de tri à bulles
def tri_a_bulles(liste):
    n = len(liste)                
    for i in range(n):           
        for j in range(0, n - 1):   
            if liste[j] > liste[j + 1]:
                # échanger les deux valeurs
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Fonction de recherche linéaire
def recherche_lineaire(liste, valeur):
    for i in range(len(liste)):     
        if liste[i] == valeur:      
            return i                
    return -1                       

import time   # module pour mesurer le temps

# Liste de test
liste = [5, 3, 8, 1, 9, 2]

# --- TRI À BULLES ---
debut = time.time()               
tri_a_bulles(liste.copy())
fin = time.time()                  
print("Temps tri à bulles :", fin - debut)

# --- TRI PYTHON ---
debut = time.time()
sorted(liste)
fin = time.time()
print("Temps tri Python :", fin - debut)
