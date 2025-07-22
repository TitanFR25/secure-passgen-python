import random

def generatePassword():
    # On définit les types de caractères à utiliser
    lettres = "azertyuiopqsdfghjklmwxcvbn"
    lettreMaj = lettres.upper()
    chiffres = "123456789"
    symboles = ",.@#$*"

    # On regroupe tous les caractères possibles dans une seule variable
    caracteres = lettres + lettreMaj + chiffres + symboles

    # On demande à l'utilisateur la longueur du mot de passe
    try:
        longueur = int(input("Quelle longueur voulez-vous pour votre mot de passe ? (minimum 10 / maximum 40) : "))
    except ValueError:
        print("❌ Erreur : veuillez entrer un nombre entier.")
        exit()

    # On vérifie que la longueur choisie respecte les règles
    if longueur < 10 or longueur > 40:
        print("❌ Erreur : le mot de passe doit contenir entre 10 et 40 caractères.")
        exit()
    else:
        # Si la longueur est correcte, on génère le mot de passe

        # On ajoute au minimum un caractère de chaque type
        mot_de_passe = [
            random.choice(lettres),
            random.choice(lettreMaj),
            random.choice(chiffres),
            random.choice(symboles)
        ]

        # On calcule le nombre de caractères restants à générer
        reste = longueur - 4

        # On complète le reste du mot de passe avec des caractères aléatoires
        for _ in range(reste):
            mot_de_passe.append(random.choice(caracteres))

        # On mélange les caractères
        random.shuffle(mot_de_passe)

        # On transforme la liste en chaîne de caractères
        mot_de_passe_final = "".join(mot_de_passe)

        # On affiche le mot de passe généré
        print("🔐 Voici le mot de passe (copiez-le si vous voulez le chiffrer) :", mot_de_passe_final)
        return mot_de_passe_final