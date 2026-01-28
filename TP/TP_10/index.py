import json
import os

# Classe Etudiant
class Etudiant:
    def __init__(self, matricule, nom, prenom, filiere):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.filiere = filiere
        self.notes = []
    
    def ajouter_note(self, matiere, note):
        if 0 <= note <= 20:
            self.notes.append({"matiere": matiere, "note": note})
            return True
        return False
    
    def calculer_moyenne(self):
        if not self.notes:
            return 0
        return round(sum(n["note"] for n in self.notes) / len(self.notes), 2)
    
    def obtenir_mention(self):
        moy = self.calculer_moyenne()
        if moy < 10: return "Ajourné"
        elif moy < 12: return "Passable"
        elif moy < 14: return "Assez bien"
        elif moy < 16: return "Bien"
        else: return "Très bien"

# Classe Gestion
class GestionEtudiants:
    def __init__(self, fichier="etudiants.json"):
        self.fichier = fichier
        self.etudiants = []
        self.charger()
    
    def charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    e = Etudiant(d["matricule"], d["nom"], d["prenom"], d["filiere"])
                    e.notes = d.get("notes", [])
                    self.etudiants.append(e)
    
    def sauvegarder(self):
        with open(self.fichier, 'w', encoding='utf-8') as f:
            data = [{"matricule": e.matricule, "nom": e.nom, "prenom": e.prenom, 
                     "filiere": e.filiere, "notes": e.notes} for e in self.etudiants]
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        self.sauvegarder()
        print("✓ Étudiant ajouté")
    
    def rechercher(self, matricule):
        for e in self.etudiants:
            if e.matricule == matricule:
                return e
        return None
    
    def afficher_tous(self):
        print("\n" + "="*70)
        for e in self.etudiants:
            print(f"{e.matricule} - {e.nom} {e.prenom} ({e.filiere}) - Moy: {e.calculer_moyenne()}")
        print("="*70)
    
    def statistiques(self):
        moyennes = [e.calculer_moyenne() for e in self.etudiants if e.notes]
        if moyennes:
            print(f"\nNombre d'étudiants : {len(self.etudiants)}")
            print(f"Moyenne générale : {sum(moyennes)/len(moyennes):.2f}")
            print(f"Admis : {sum(1 for m in moyennes if m >= 10)}")

# Menu
def menu():
    gestion = GestionEtudiants()
    
    while True:
        print("\n1. Ajouter étudiant")
        print("2. Ajouter note")
        print("3. Rechercher")
        print("4. Afficher tous")
        print("5. Statistiques")
        print("6. Quitter")
        
        choix = input("\nChoix : ")
        
        if choix == "1":
            mat = input("Matricule : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            filiere = input("Filière : ")
            gestion.ajouter_etudiant(Etudiant(mat, nom, prenom, filiere))
        
        elif choix == "2":
            mat = input("Matricule : ")
            e = gestion.rechercher(mat)
            if e:
                matiere = input("Matière : ")
                note = float(input("Note : "))
                if e.ajouter_note(matiere, note):
                    gestion.sauvegarder()
                    print("✓ Note ajoutée")
        
        elif choix == "3":
            mat = input("Matricule : ")
            e = gestion.rechercher(mat)
            if e:
                print(f"\n{e.nom} {e.prenom} - {e.filiere}")
                print(f"Moyenne : {e.calculer_moyenne()} - {e.obtenir_mention()}")
        
        elif choix == "4":
            gestion.afficher_tous()
        
        elif choix == "5":
            gestion.statistiques()
        
        elif choix == "6":
            break

if __name__ == "__main__":
    menu()