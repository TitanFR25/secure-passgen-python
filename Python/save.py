import os
from chiffrement import filePath

# Déclarer les variables qui vont mener chaque fichier créé dans le dossier Python
chemin = filePath("Mes données.txt")

# Fonction qui va écrire l'identifiant
def FichierIdentif(saveIdentif):
    try:
        with open(chemin, "a") as f:
            f.write(f"Identifiant : {saveIdentif}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        exit()

# Fonction pour écrire le nom de l'appli
def FichierAppli(saveAppli):
    try:
        with open(chemin, "a") as f:
            f.write(f"Application : {saveAppli}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        exit()

# Fonction pour créer un fichier simple et écrire le mot de passe
def FichierMotDePasse(password):
    try:
        # Passer le mot de passe chiffré de l'état bytes -> str
        print("🔄 Adaptation du Chiffrement pour le fichier...")
        if isinstance(password, bytes):
            newPassword = password.decode()
        else:
            newPassword = password

        #Créer un fichier .txt et écrire le mot de passe
        with open(chemin, "a") as f:
            f.write(f"Mot de passe : {newPassword}\n")
        print("✅ Adaptation terminée")
    except Exception as e:
        print("❌ Erreur d'adaptation :", e)
        exit()

# Fonction pour récupérer le mot de passe
def recupererLeMotDePasse():
    try:
        # Ouvrir le fichier
        with open(chemin, "r") as f:

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
        # Créer et appeler la fonction du fichier (Mot de passe uniquement)
        try:
            print("💾 Sauvegarde en cours...")
            FichierMotDePasse(mot_de_passe_final)
            print("✅ Sauvegarde terminée") 
        except Exception as e:
            print("❌ Erreur lors de la sauvegarde :", e) 
            exit()
            return  

        # Demander s'il souhaite enregistrer le nom de l'application associée
        questionSauvegardeAppli = input("📱 Voulez-vous également enregistrer le nom de l'application liée ? (oui/non) ").strip().lower()

        if questionSauvegardeAppli == "oui":

            # Demander le nom de l'application
            sauvegardeAppli = input("➡️  Entrez le nom de l'application : ").strip()

            # Créer et appeler la fonction du fichier (Application)
            try:
                print("💾 Sauvegarde en cours...")
                FichierAppli(sauvegardeAppli)
                print("✅ Sauvegarde terminée") 
            except Exception as e:
                print("❌ Erreur lors de la sauvegarde :", e) 
                exit()
                return    

            # Demander si l'utilisateur veut enregistrer son identifiant lié à l'application
            questionSauvegardeIdentif = input("👤 Voulez-vous enregistrer l'identifiant lié à l'application (pseudo, email, etc.) ? (oui/non) ").strip().lower()

            if questionSauvegardeIdentif == "oui":
                # Demander l'identifiant
                SauvegardeIdentif = input("➡️  Entrez votre identifiant : ").strip()

                # Créer et appeler la fonction du fichier (Mot de passe, Application, Identifiant)
                try:
                    print("💾 Sauvegarde en cours...")
                    FichierIdentif(SauvegardeIdentif)
                    print("✅ Sauvegarde terminée")
                except Exception as e:
                    print("❌ Erreur lors de la sauvegarde :", e)
                    exit()
                    return
    else:
        print("❌ Mot de passe non sauvegardé")
        exit()