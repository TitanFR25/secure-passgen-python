from chiffrement import filePath
import time

chemin = filePath("Mes données.txt")

# Fonction pour récupérer le mot de passe
def recupererLeMotDePasse():
    try:
        print("🔄 Récuperation du mot de passe...")
        time.sleep(1)
        # Ouvrir le fichier
        with open(chemin, "r") as f:

            # Lire les lignes
            lignes = f.readlines()

            # Lire les lignes jusqu'à trouver une ligne qui commence par "Mot de passe :"
            for ligne in reversed(lignes):
                if ligne.startswith("Mot de passe : "):
                    password = ligne.replace("Mot de passe : ", "").strip()
                    print("✅ Récuperation du mot de passe terminé")
                    return password      
    # Si on ne trouve pas le fichier, afficher une erreur
    except FileNotFoundError:
        print("❌ Fichier introuvable")
        exit()
        return None
    
#Fonction pour remplacer le mot de passe
def remplacerPass(passwordByte):
    try:
        #Ouvir le fichier
        with open(chemin, "r") as f:
            print("🔄 Remplacement en cours..")
            time.sleep(0.8)
            # Lire les lignes
            lignes = f.readlines()

            # Passer le mot de passe chiffré de l'état bytes -> str et le stocker dans une variable
            mot_de_passe_str = passwordByte.decode() if isinstance(passwordByte , bytes) else passwordByte

            if lignes:
                # Remplacer la première ligne par la nouvelle ligne Mot de passe
                lignes[0] = f"Mot de passe : {mot_de_passe_str}\n"
            else:
                # Si fichier vide, on ajoute la ligne mot de passe
                lignes = [f"Mot de passe : {mot_de_passe_str}\n"]
            
            #écrire la ligne
            with open(chemin, "w") as f:
                f.writelines(lignes)

            print("✅ Première ligne remplacée par le mot de passe chiffré.")
    except Exception as e:
        print("Erreur lors de la récuperation : ", e)
        exit()
        return