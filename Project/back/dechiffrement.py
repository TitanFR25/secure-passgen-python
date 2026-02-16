from cryptography.fernet import Fernet
from Project.back.chiffrement import loadKey
import time

# Fonction pour déchiffrer le mot de passe reçu
def fichierPassDecrypt(passwordCrypt: str) -> str:
    try:
        print("🔄 Déchiffrement en cours...")
        time.sleep(2)

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