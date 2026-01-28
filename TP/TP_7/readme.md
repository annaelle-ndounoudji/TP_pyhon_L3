# Gestion d'Étudiants avec POO

## Description
Programme orienté objet qui gère des étudiants avec leurs informations et calcule automatiquement leur moyenne.

## Structure de la classe Etudiant

### Attributs
- `nom` : nom de l'étudiant
- `matricule` : numéro d'identification
- `notes` : liste des notes

### Méthodes
- `calculer_moyenne()` : calcule la moyenne des notes
- `afficher_infos()` : affiche toutes les informations

## Exemple d'utilisation
```python
# Créer un étudiant
etudiant1 = Etudiant("Alice", "2024001", [12, 15, 14, 13])

# Afficher ses informations
etudiant1.afficher_infos()

# Obtenir uniquement la moyenne
moyenne = etudiant1.calculer_moyenne()
print("Moyenne :", moyenne)
```

## Résultat
```
Nom : Alice
Matricule : 2024001
Notes : [12, 15, 14, 13]
Moyenne : 13.5
```

## Concepts Python
- Programmation orientée objet (POO)
- Classes et objets
- Méthode `__init__` (constructeur)
- Attributs et méthodes d'instance