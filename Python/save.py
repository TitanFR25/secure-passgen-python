from generator import generatePassword

def savePassword(mot_de_passe_final):
    #Stocker le mot de passe génerer
    sauvegardePass = mot_de_passe_final

    #Demandez a l'utilisateur si il veut saugarder son mot de passe
    questionSauvegardePass = input("Voulez vous enregistrer votre mot de passe ? (oui/non)")
    #stocker la reponse dans la variable
    reponsePass = questionSauvegardePass

    #Si il accepte demandez d'autre potentiel enregistrement
    if reponsePass.lower() == "oui":

        #Demandez si il veut enregistrer le nom de l'application dans lequel le mot de passe sera rattaché
        questionSauvegardeAppli = input("Voulez-vous enregistrer également le nom de l'application à qui il sera rattaché ? (oui/non)")
        #stocker la reponse dans la variable
        reponseAppli = questionSauvegardeAppli

        #Si il repond oui
        if reponseAppli.lower() == "oui":

            #Demandez à l'utilisateur le nom de l'application
            sauvegardeAppli = input("Entrer le nom de l'application :")

            #Demandez si l'utilisateur veut aussi enregistrer ses identifiant relié a l'application
            questionSauvegardeIdentif = input("Voulez vous enregistrer le nom de votre identifiant relié à l'appli (pseudo / email ect) ?"
            "(oui/non) ")

            #stocker la reponse dans la variable
            reponseIdentif = questionSauvegardeIdentif

            #si il repond oui a la question
            if reponseIdentif.lower() == "oui":
                #demandez ses identifiant
                SauvegardeIdentif = input("Entrer votre identifiant de votre application :")

                #Créer le fichier pour le Mot de passe,Appli,Identifiant, si il y'a une erreur la sortir
                try:
                    print("Sauvegarde en cours...")
                    with open("Mes Données.txt","a") as f:
                        f.write(f"Mot de passe : {sauvegardePass}\n")
                        f.write(f"Application : {sauvegardeAppli}\n")
                        f.write(f"Identifiant : {SauvegardeIdentif}\n")
                        print("Sauvegarde terminé")
                except Exception as e:
                    print("Erreur lors de la sauvegarde", e)
            else:
                #Créer le fichier pour le Mot de passe,Appli, si il y'a une erreur la sortir
                try:
                    print("Sauvegarde en cours...")
                    with open("Mes Données.txt","a") as f:
                        f.write(f"Mot de passe : {sauvegardePass}\n")
                        f.write(f"Application : {sauvegardeAppli}\n")
                        print("Sauvegarde terminé") 
                except Exception as e:
                    print("Erreur lors de la sauvegarde", e)     
        else:
            #Créer le fichier pour le Mot de passe, si il y'a une erreur la sortir
            try:
                print("Sauvegarde en cours...")
                with open("Mes Données.txt","a") as f:
                    f.write(f"Mot de passe : {sauvegardePass}\n")
                    print("Sauvegarde terminé") 
            except Exception as e:
                print("Erreur lors de la sauvegarde", e)   
    else:
        print("Mot de passe non sauvegardé")
        exit()
#Pouvoir executer les script
if __name__ == "__main__":
    mot_de_passe = generatePassword()
    savePassword(mot_de_passe)