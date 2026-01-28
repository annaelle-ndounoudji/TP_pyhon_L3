# Programme de Division Sécurisé

## Description
Programme qui effectue une division entre deux nombres avec gestion complète des erreurs.

## Comment l'utiliser
```bash
python division.py
```

## Exemples d'utilisation

### Cas normal
```
Entrez le premier nombre : 10
Entrez le deuxième nombre : 2
Résultat : 5.0
Programme terminé.
```

### Division par zéro
```
Entrez le premier nombre : 10
Entrez le deuxième nombre : 0
Erreur : impossible de diviser par zéro.
Programme terminé.
```

### Entrée invalide
```
Entrez le premier nombre : abc
Erreur : veuillez entrer uniquement des nombres.
Programme terminé.
```

## Gestion des erreurs
- **ZeroDivisionError** : détecte la division par zéro
- **ValueError** : détecte les entrées non numériques
- **finally** : affiche un message de fin dans tous les cas

## Concepts Python
- Bloc `try/except` pour gérer les exceptions
- Conversion avec `float()` pour accepter les décimales