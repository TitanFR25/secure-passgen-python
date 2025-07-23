# Import des modules nécessaires pour le programme
from generator import generatePassword
from chiffrement import cryptPass
from save import savePassword
from save import recupererLeMotDePasse
from decrypt import fichierPassDecrypt

# Demander à l'utilisateur s'il possède déjà le fichier Mes Données.txt
questionPossederFich = input("Possédez-vous déjà le fichier qui sauvegarde vos données ? (oui/non) ").strip().lower()

# Si la réponse est oui, demander s'il a chiffré son mot de passe
if questionPossederFich == "oui":
    questionCryptPass = input("Avez-vous chiffré votre mot de passe dans ce fichier ? (oui/non) ").strip().lower()

    # Si la réponse est oui, demander s'il veut déchiffrer son mot de passe
    if questionCryptPass == "oui":
        questionDecryptPass = input("Souhaitez-vous déchiffrer votre mot de passe ? (oui/non) ").strip().lower()

        if questionDecryptPass == "oui":
            if __name__ == "__main__":
                # Récupérer le contenu du fichier .txt
                FichierPassCrypt = recupererLeMotDePasse()

                if FichierPassCrypt is None:
                    print("❌ Aucun mot de passe trouvé dans le fichier.")
                    exit()
                else:
                    MotDePasseDecrypt = fichierPassDecrypt(FichierPassCrypt)
                    print("🔓 Voici votre mot de passe :", MotDePasseDecrypt)
        else:
            exit()
    else:
        # À venir...
        exit()
else:
    # Point d'entrée du script
    if __name__ == "__main__":
        # Génération du mot de passe
        mot_de_passe = generatePassword()

        # Demander à l'utilisateur s'il souhaite chiffrer le mot de passe et le chiffrer si besoin
        mot_de_passe_resultat, est_chiffre = cryptPass(mot_de_passe)

        # Sauvegarde du mot de passe (chiffré ou non) en fonction de la réponse de l'utilisateur
        savePassword(mot_de_passe, mot_de_passe_resultat, est_chiffre)