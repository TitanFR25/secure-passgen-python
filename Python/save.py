# Fonction pour sauvegarder les données
def savePassword(mot_de_passe_original, mot_de_passe_crypt, est_chiffre):

    # Stocker les mots de passe reçus
    sauvegardePassChiffre = mot_de_passe_crypt
    sauvegardePass = mot_de_passe_original

    print("Détection de cryptage...")

    # Sélectionner le bon mot de passe à afficher et enregistrer
    mot_de_passe_final = sauvegardePassChiffre if est_chiffre else sauvegardePass

    # Affichage dynamique du mot de passe selon qu'il soit chiffré ou non
    if est_chiffre:
        print("✅ Cryptage détecté")
        print("🔐 Votre mot de passe chiffré :", mot_de_passe_final)
    else:
        print("❌ Cryptage non détecté")
        
    # Demander à l'utilisateur s'il souhaite enregistrer son mot de passe
    questionSauvegardePass = input("\n💾 Voulez-vous enregistrer votre mot de passe ? (oui/non) ")
    reponsePass = questionSauvegardePass.strip().lower()

    # Si l'utilisateur accepte, demander d'autres informations potentielles
    if reponsePass == "oui":

        # Demander s'il souhaite enregistrer le nom de l'application associée
        questionSauvegardeAppli = input("📱 Voulez-vous également enregistrer le nom de l'application liée ? (oui/non) ").strip().lower()
        reponseAppli = questionSauvegardeAppli

        if reponseAppli == "oui":

            # Demander le nom de l'application
            sauvegardeAppli = input("➡️ Entrez le nom de l'application : ").strip()

            # Demander si l'utilisateur veut enregistrer son identifiant lié à l'application
            questionSauvegardeIdentif = input("👤 Voulez-vous enregistrer l'identifiant lié à l'application (pseudo, email, etc.) ? (oui/non) ").strip().lower()
            reponseIdentif = questionSauvegardeIdentif

            if reponseIdentif == "oui":
                # Demander l'identifiant
                SauvegardeIdentif = input("➡️ Entrez votre identifiant : ").strip()

                # Créer et écrire dans le fichier (Mot de passe, Application, Identifiant)
                try:
                    print("💾 Sauvegarde en cours...")
                    with open("Mes Données.txt", "a") as f:
                        f.write(f"Mot de passe : {mot_de_passe_final}\n")
                        f.write(f"Application : {sauvegardeAppli}\n")
                        f.write(f"Identifiant : {SauvegardeIdentif}\n")
                    print("✅ Sauvegarde terminée")
                except Exception as e:
                    print("❌ Erreur lors de la sauvegarde :", e)
            else:
                # Créer et écrire dans le fichier (Mot de passe, Application)
                try:
                    print("💾 Sauvegarde en cours...")
                    with open("Mes Données.txt", "a") as f:
                        f.write(f"Mot de passe : {mot_de_passe_final}\n")
                        f.write(f"Application : {sauvegardeAppli}\n")
                    print("✅ Sauvegarde terminée") 
                except Exception as e:
                    print("❌ Erreur lors de la sauvegarde :", e)     
        else:
            # Créer et écrire dans le fichier (Mot de passe uniquement)
            try:
                print("💾 Sauvegarde en cours...")
                with open("Mes Données.txt", "a") as f:
                    f.write(f"Mot de passe : {mot_de_passe_final}\n")
                print("✅ Sauvegarde terminée") 
            except Exception as e:
                print("❌ Erreur lors de la sauvegarde :", e)   
    else:
        print("❌ Mot de passe non sauvegardé")
        exit()