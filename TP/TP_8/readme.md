# Algorithmes de Tri et Recherche

## Description
Programme qui implémente des algorithmes classiques (tri à bulles et recherche linéaire) et compare les performances.

## Algorithmes implémentés

### Tri à bulles
Algorithme simple qui compare les éléments adjacents et les échange si nécessaire.

### Recherche linéaire
Parcourt la liste élément par élément jusqu'à trouver la valeur recherchée.

## Comment l'utiliser
```python
# Trier une liste
liste = [5, 3, 8, 1, 9, 2]
liste_triee = tri_a_bulles(liste)
print(liste_triee)  # [1, 2, 3, 5, 8, 9]

# Rechercher un élément
position = recherche_lineaire(liste, 8)
print(position)  # 2 (index de la valeur 8)
```

## Comparaison de performances

Le programme compare le tri à bulles avec le tri natif de Python :
```
Temps tri à bulles : 0.000012
Temps tri Python : 0.000003
```

Le tri Python est beaucoup plus rapide car optimisé en C.

## Exécution
```bash
python algorithmes.py
```

## Concepts Python
- Algorithmes de tri et recherche
- Mesure de performance avec `time`
- Copie de liste avec `copy()`
- Fonction `sorted()` native