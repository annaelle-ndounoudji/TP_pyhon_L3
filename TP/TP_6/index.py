# Programme de division avec gestion des erreurs

try:
    # Demander le premier nombre
    a = float(input("Entrez le premier nombre : "))

    # Demander le deuxième nombre
    b = float(input("Entrez le deuxième nombre : "))

    # Calcul de la division
    resultat = a / b

    # Afficher le résultat
    print("Résultat :", resultat)

except ZeroDivisionError:
    # Erreur si on divise par zéro
    print("Erreur : impossible de diviser par zéro.")

except ValueError:
    # Erreur si l'utilisateur n'entre pas un nombre
    print("Erreur : veuillez entrer uniquement des nombres.")

finally:
    # Message affiché dans tous les cas
    print("Programme terminé.")
