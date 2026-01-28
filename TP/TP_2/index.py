# calcul de la moyenne
def calcul_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme = somme + note
    moyenne = somme / len(liste_notes)
    return moyenne

# determination de la mention
def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Bien"
    else:
        return "Très bien"

# teste avec plusieur liste de note
notes1 = [8, 9, 10]
notes2 = [11, 12, 10]
notes3 = [14, 15, 16]

moy1 = calcul_moyenne(notes1)
print("Moyenne :", moy1, "-", mention(moy1))

moy2 = calcul_moyenne(notes2)
print("Moyenne :", moy2, "-", mention(moy2))

moy3 = calcul_moyenne(notes3)
print("Moyenne :", moy3, "-", mention(moy3))
