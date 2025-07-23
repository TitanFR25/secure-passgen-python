from cryptography.fernet import Fernet
import os

# Charger une clé existante
def loadKey():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(dir_path, "secret.key")
    return open(key_path, "rb").read()

# Fonction pour déchiffrer le mot de passe reçu
def fichierPassDecrypt(passwordCrypt: str) -> str:
    try:
        print("🔄 Déchiffrement en cours...")

        # Charger la clé existante
        key = loadKey()

        # Stocker la clé dans une variable Fernet
        fernet = Fernet(key)
        
        # Encoder en bytes car Fernet.decrypt attend un type bytes
        passwordDecrypt = fernet.decrypt(passwordCrypt.encode())
        print("✅ Déchiffrement terminé")
        return passwordDecrypt.decode()
    except Exception as e:
        print("❌ Erreur lors du déchiffrement :", e)
        exit()
