# Programme Python - Âge et Nombres Pairs

## Description

Ce programme simple en Python effectue deux tâches :
1. Détermine si l'utilisateur est mineur ou majeur selon son âge
2. Affiche tous les nombres pairs de 1 à 100

## Prérequis

- Python 3.x installé sur votre machine

## Utilisation

### Exécution du programme
```bash
python script.py
```

### Fonctionnement

1. Le programme demande votre nom
2. Le programme demande votre âge
3. Il affiche si vous êtes mineur (< 18 ans) ou majeur (≥ 18 ans)
4. Il affiche ensuite tous les nombres pairs de 1 à 100

### Exemple d'exécution
```
Ton nom : Marie
Ton âge : 20
Tu es majeur
Nombres pairs de 1 à 100 :
2
4
6
8
...
100
```

## Structure du code

- **Saisie utilisateur** : Récupération du nom et de l'âge
- **Condition** : Vérification de la majorité avec `if/else`
- **Boucle** : Parcours des nombres de 1 à 100 avec `for`
- **Test de parité** : Utilisation de l'opérateur modulo `%` pour identifier les nombres pairs

## Concepts Python illustrés

- `input()` : Saisie utilisateur
- `int()` : Conversion de type
- `if/else` : Structures conditionnelles
- `for` : Boucles
- `range()` : Génération de séquences
- Opérateur modulo `%` : Test de divisibilité
