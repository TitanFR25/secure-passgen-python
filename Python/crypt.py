from cryptography.fernet import Fernet
import os

# Fonction pour générer une clé et la sauvegarder dans un fichier
def generateKey():
    key = Fernet.generate_key()

    # Générer le fichier dans le dossier du script
    dir_path = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(dir_path, "secret.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

# Fonction pour charger une clé existante
def loadKey():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(dir_path, "secret.key")
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
    questionPassCrypt = input("Voulez-vous chiffrer votre mot de passe ? oui/non (Recommandé) : ")

    # Stocker la réponse dans une variable
    reponsePassCrypt = questionPassCrypt

    if reponsePassCrypt.lower() == "oui":
        try:
            print("🔐 Cryptage en cours...")
            dir_path = os.path.dirname(os.path.abspath(__file__))
            key_path = os.path.join(dir_path, "secret.key")

            # Vérifier si la clé existe, sinon la générer
            if not os.path.exists(key_path):
                generateKey()

            # Charger la clé
            key = loadKey()

            # Chiffrer le mot de passe avec la clé
            mot_de_passe_chiffre = cryptPassword(motDePasseFinal, key)
            print("✅ Cryptage terminé")
            return mot_de_passe_chiffre, True

        except Exception as e:
            print("❌ Erreur lors du cryptage :", e)
            exit()
    else:
        # Retourner le mot de passe en clair et un indicateur de non-chiffrement
        return motDePasseFinal, False