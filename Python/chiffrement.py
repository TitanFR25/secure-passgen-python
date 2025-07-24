from cryptography.fernet import Fernet
import os

#fonction pour définir le chemin du dossier
def dir_path():
    return os.path.dirname(os.path.abspath(__file__))

# Fonction pour générer une clé et la sauvegarder dans un fichier
def generateKey():
    key = Fernet.generate_key()

    # Générer le fichier dans le dossier du script
    dir_path()
    key_path = os.path.join(dir_path(), "secret.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

# Fonction pour charger une clé existante
def loadKey():
    dir_path()
    key_path = os.path.join(dir_path(), "secret.key")
    return open(key_path, "rb").read()

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
            dir_path()
            key_path = os.path.join(dir_path(), "secret.key")

            # Vérifier si la clé existe, sinon la générer
            if not os.path.exists(key_path):
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