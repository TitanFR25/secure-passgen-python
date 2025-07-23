import os
from cryptography.fernet import Fernet

# Déclarer les variables qui vont mener chaque fichier créé dans le dossier Python
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "Mes Données.txt")

# Fonction qui va créer un fichier complet
def creerFichierFull(password, saveAppli, saveIdentif):
    try:
        # Passer le mot de passe chiffré de l'état bytes -> str
        print("🔄 Adaptation du Chiffrement pour le fichier...")
        if isinstance(password, bytes):
            newPassword = password.decode()
        else:
            newPassword = password
        with open(file_path, "a") as f:
            f.write(f"Mot de passe : {newPassword}\n")
            f.write(f"Application : {saveAppli}\n")
            f.write(f"Identifiant : {saveIdentif}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        print("❌ Erreur d'adaptation :", e)
        exit()

# Fonction pour créer un fichier moyen
def creerFichierMedium(password, saveAppli):
    try:
        # Passer le mot de passe chiffré de l'état bytes -> str
        print("🔄 Adaptation du Chiffrement pour le fichier...")
        if isinstance(password, bytes):
            newPassword = password.decode()
        else:
            newPassword = password
        with open(file_path, "a") as f:
            f.write(f"Mot de passe : {newPassword}\n")
            f.write(f"Application : {saveAppli}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        print("❌ Erreur d'adaptation :", e)
        exit()

# Fonction pour créer un fichier simple
def creerFichierPetit(password):
    try:
        # Passer le mot de passe chiffré de l'état bytes -> str
        print("🔄 Adaptation du Chiffrement pour le fichier...")
        if isinstance(password, bytes):
            newPassword = password.decode()
        else:
            newPassword = password
        with open(file_path, "a") as f:
            f.write(f"Mot de passe : {newPassword}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        print("❌ Erreur d'adaptation :", e)
        exit()

# Fonction pour récupérer le mot de passe
def recupererLeMotDePasse():
    try:
        # Ouvrir le fichier
        with open(file_path, "r") as f:

            # Lire les lignes
            lignes = f.readlines()

            # Lire les lignes jusqu'à trouver une ligne qui commence par "Mot de passe :"
            for ligne in reversed(lignes):
                if ligne.startswith("Mot de passe : "):
                    password = ligne.replace("Mot de passe : ", "").strip()
                    return password      
    # Si on ne trouve pas le fichier, afficher une erreur
    except FileNotFoundError:
        print("❌ Fichier introuvable")
        exit()
        return None

# Fonction pour sauvegarder les données
def savePassword(mot_de_passe_original, mot_de_passe_crypt, est_chiffre):

    # Stocker les mots de passe reçus
    sauvegardePassChiffre = mot_de_passe_crypt
    sauvegardePass = mot_de_passe_original

    print("🔄 Détection du Chiffrement...")

    # Sélectionner le bon mot de passe à afficher et enregistrer
    mot_de_passe_final = sauvegardePassChiffre if est_chiffre else sauvegardePass

    # Affichage dynamique du mot de passe selon qu'il soit chiffré ou non
    if est_chiffre:
        print("✅ Chiffrement détecté")
        print("🔐 Votre mot de passe chiffré :", mot_de_passe_final)
    else:
        print("❌ Cryptage non détecté")
        
    # Demander à l'utilisateur s'il souhaite enregistrer son mot de passe
    questionSauvegardePass = input("💾 Voulez-vous enregistrer votre mot de passe ? (oui/non) ").strip().lower()

    # Si l'utilisateur accepte, demander d'autres informations potentielles
    if questionSauvegardePass == "oui":

        # Demander s'il souhaite enregistrer le nom de l'application associée
        questionSauvegardeAppli = input("📱 Voulez-vous également enregistrer le nom de l'application liée ? (oui/non) ").strip().lower()

        if questionSauvegardeAppli == "oui":

            # Demander le nom de l'application
            sauvegardeAppli = input("➡️  Entrez le nom de l'application : ").strip()

            # Demander si l'utilisateur veut enregistrer son identifiant lié à l'application
            questionSauvegardeIdentif = input("👤 Voulez-vous enregistrer l'identifiant lié à l'application (pseudo, email, etc.) ? (oui/non) ").strip().lower()

            if questionSauvegardeIdentif == "oui":
                # Demander l'identifiant
                SauvegardeIdentif = input("➡️  Entrez votre identifiant : ").strip()

                # Créer et appeler la fonction du fichier (Mot de passe, Application, Identifiant)
                try:
                    print("💾 Sauvegarde en cours...")
                    creerFichierFull(mot_de_passe_final, sauvegardeAppli, SauvegardeIdentif)
                    print("✅ Sauvegarde terminée")
                except Exception as e:
                    print("❌ Erreur lors de la sauvegarde :", e)
            else:
                # Créer et appeler la fonction du fichier (Mot de passe, Application)
                try:
                    print("💾 Sauvegarde en cours...")
                    creerFichierMedium(mot_de_passe_final, sauvegardeAppli)
                    print("✅ Sauvegarde terminée") 
                except Exception as e:
                    print("❌ Erreur lors de la sauvegarde :", e)     
        else:
            # Créer et appeler la fonction du fichier (Mot de passe uniquement)
            try:
                print("💾 Sauvegarde en cours...")
                creerFichierPetit(mot_de_passe_final)
                print("✅ Sauvegarde terminée") 
            except Exception as e:
                print("❌ Erreur lors de la sauvegarde :", e)   
    else:
        print("❌ Mot de passe non sauvegardé")
        exit()
