# Calculateur de Moyenne et Mention

## Description
Programme qui calcule la moyenne de notes et détermine la mention correspondante.

## Comment l'utiliser
```bash
python notes.py
```

## Mentions
- **Ajourné** : moyenne < 10
- **Passable** : moyenne entre 10 et 12
- **Assez bien** : moyenne entre 12 et 14
- **Très bien** : moyenne ≥ 14

## Exemple de résultat
```
Moyenne : 9.0 - Ajourné
Moyenne : 11.0 - Passable
Moyenne : 15.0 - Très bien
```

## Fonctions
- `calcul_moyenne()` : calcule la moyenne d'une liste de notes
- `mention()` : retourne la mention selon la moyenne

