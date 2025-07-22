# Import des modules nécessaires pour le programme
from generator import generatePassword
from crypt import cryptPass
from save import savePassword

# Point d'entrée du script
if __name__ == "__main__":
    # Génération du mot de passe
    mot_de_passe = generatePassword()

    # Demande à l'utilisateur s'il souhaite chiffrer le mot de passe et le chiffre si besoin
    mot_de_passe_resultat, est_chiffre = cryptPass(mot_de_passe)

    # Sauvegarde du mot de passe (chiffré ou non) en fonction de la réponse de l'utilisateur
    savePassword(mot_de_passe, mot_de_passe_resultat, est_chiffre)