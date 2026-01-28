import csv

# 1. Lire le fichier CSV d'employés
def lire_employes(fichier):
    """Lit le fichier CSV et retourne la liste des employés"""
    employes = []
    with open(fichier, 'r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            employes.append(ligne)
    return employes

# 2. Calculer le salaire moyen par département
def calculer_moyenne_par_dept(employes):
    """Calcule le salaire moyen pour chaque département"""
    departements = {}
    
    for employe in employes:
        dept = employe['departement']
        salaire = float(employe['salaire'])
        
        if dept not in departements:
            departements[dept] = {'total': 0, 'nombre': 0}
        
        departements[dept]['total'] += salaire
        departements[dept]['nombre'] += 1
    
    # Calculer les moyennes
    moyennes = {}
    for dept, data in departements.items():
        moyennes[dept] = data['total'] / data['nombre']
    
    return moyennes

# 3. Générer un rapport textuel
def generer_rapport(moyennes, fichier_sortie):
    """Crée un rapport textuel avec les résultats"""
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write("=" * 50 + "\n")
        f.write("RAPPORT D'ANALYSE DES SALAIRES PAR DÉPARTEMENT\n")
        f.write("=" * 50 + "\n\n")
        
        for dept, moyenne in moyennes.items():
            f.write(f"Département : {dept}\n")
            f.write(f"Salaire moyen : {moyenne:.2f} €\n")
            f.write("-" * 50 + "\n")
        
        f.write("\nRapport généré avec succès.\n")

# Programme principal
if __name__ == "__main__":
    try:
        # Étape 1 : Lire les données
        employes = lire_employes('employes.csv')
        print(f" {len(employes)} employés chargés")
        
        # Étape 2 : Calculer les moyennes
        moyennes = calculer_moyenne_par_dept(employes)
        print(f" Analyse de {len(moyennes)} départements")
        
        # Étape 3 : Générer le rapport
        generer_rapport(moyennes, 'rapport_salaires.txt')
        print(" Rapport généré : rapport_salaires.txt")
        
        # Affichage à l'écran
        print("\n" + "=" * 50)
        print("RÉSULTATS")
        print("=" * 50)
        for dept, moyenne in moyennes.items():
            print(f"{dept:20} : {moyenne:8.2f} €")
            
    except FileNotFoundError:
        print(" Erreur : fichier employes.csv introuvable")
    except Exception as e:
        print(f" Erreur : {e}")