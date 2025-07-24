from cryptography.fernet import Fernet
import os
import time

#Fonction pour définir le chemin des fichier
def filePath(nom_fichier):
    #Dossier python
    base_dir = os.path.dirname(os.path.abspath(__file__))

    #Remonter d'un cran (../) et aller dans le dossier Fichier
    dossier_fichier = os.path.abspath(os.path.join(base_dir, ".." , "Fichier"))

    #Définir le chemin du fichier en fonction de l'entension
    if nom_fichier.endswith(".key"):
        dossier_cible = os.path.join(dossier_fichier, "SecretFile")
    elif nom_fichier.endswith(".txt"):
        dossier_cible = os.path.join(dossier_fichier, "TextFile")
    else:
        exit()
        raise ValueError("Extension non pris en charge.")
    
    #Créer les dossier si ils existent pas
    os.makedirs(dossier_cible, exist_ok=True)
        
    #Retourne le chemin complet du fichier
    return os.path.join(dossier_cible, nom_fichier)

# Fonction pour générer une clé et la sauvegarder dans un fichier
def generateKey():
    key = Fernet.generate_key()

    # Générer le fichier dans le dossier du script
    chemin = filePath("secret.key")
    with open(chemin, "wb") as key_file:
        key_file.write(key)
    return key

# Fonction pour charger une clé existante
def loadKey():
    chemin = filePath("secret.key")
    return open(chemin, "rb").read()

# Fonction pour chiffrer un mot de passe
def cryptPassword(password: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(password.encode())

# Fonction qui demande à l'utilisateur s'il souhaite chiffrer son mot de passe
def cryptPass(mot_de_passe_final):
    # Stocker le mot de passe généré dans une variable
    motDePasseFinal = mot_de_passe_final

    # Demander à l'utilisateur s'il souhaite chiffrer son mot de passe
    questionPassCrypt = input("Voulez-vous chiffrer votre mot de passe ? oui/non (Recommandé) : ").strip().lower()

    #Si l'utilisateur dit oui alors on chiffre sinon on passe a la sauvegarde
    if questionPassCrypt == "oui":
        try:
            print("🔐 Chiffrement en cours...")
            time.sleep(0.5)
            chemin = filePath("secret.key")

            # Vérifier si la clé existe, sinon la générer
            if not os.path.exists(chemin):
                print("Clé non trouvée géneration en cours...")
                time.sleep(0.3)
                generateKey()

            # Charger la clé
            key = loadKey()

            # Chiffrer le mot de passe avec la clé
            mot_de_passe_chiffre = cryptPassword(motDePasseFinal, key)
            print("✅ Chiffrement terminé")
            return mot_de_passe_chiffre, True

        except Exception as e:
            print("❌ Erreur lors du Chiffrement :", e)
            exit()
    else:
        # Retourner le mot de passe en clair et un indicateur de non-chiffrement
        return motDePasseFinal, False