# Analyse de Données RH - Salaires par Département

## Description
Programme d'analyse de données RH qui calcule le salaire moyen par département à partir d'un fichier CSV d'employés.

## Fonctionnalités
1. **Lecture CSV** : importe les données des employés
2. **Calcul statistique** : calcule le salaire moyen par département
3. **Génération de rapport** : crée un fichier texte avec les résultats

## Structure des fichiers

### Fichier d'entrée : `employes.csv`
```csv
nom,prenom,departement,salaire
Dupont,Jean,IT,45000
Martin,Sophie,RH,38000
```

### Fichier de sortie : `rapport_salaires.txt`
Rapport formaté avec les moyennes par département.

## Installation et utilisation

### Prérequis
- Python 3.x
- Module `csv` (inclus par défaut)

### Exécution
```bash
python analyse_rh.py
```

## Exemple de résultat
```
✓ 7 employés chargés
✓ Analyse de 3 départements
✓ Rapport généré : rapport_salaires.txt

==================================================
RÉSULTATS
==================================================
IT                   : 48000.00 €
RH                   : 36500.00 €
Finance              : 51500.00 €
```

## Compétences Python utilisées
- Module `csv` pour la lecture de fichiers
- Dictionnaires pour structurer les données
- Gestion des fichiers avec `open()`
- Gestion des exceptions `try/except`
- Formatage de chaînes avec f-strings
- Encodage UTF-8 pour les caractères spéciaux

## Structure du code

### Fonctions principales
- `lire_employes()` : lecture et parsing du CSV
- `calculer_moyenne_par_dept()` : calculs statistiques
- `generer_rapport()` : création du fichier de sortie

## Personnalisation
Modifiez `employes.csv` avec vos propres données en respectant le format :
- nom, prenom, departement, salaire

## Gestion des erreurs
- Vérification de l'existence du fichier
- Gestion des erreurs de lecture/écriture
- Messages d'erreur explicites