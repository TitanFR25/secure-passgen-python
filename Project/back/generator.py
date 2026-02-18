# back.py
import random


# Fonction de génération (adaptée de ton code, sans input/print/exit)
def generate_password(length: int = 12) -> str:
    """
    Génère un mot de passe respectant :
    - longueur entre 10 et 40 (sinon ValueError)
    - au moins 1 minuscule, 1 majuscule, 1 chiffre, 1 symbole
    - mélange aléatoire
    """
    try:
        longueur = int(length)
    except Exception:
        raise ValueError("La longueur doit être un entier.")

    if longueur < 10 or longueur > 40:
        raise ValueError("La longueur doit être entre 10 et 40.")

    # jeux de caractères (ta version)
    lettres = "azertyuiopqsdfghjklmwxcvbn"
    lettreMaj = lettres.upper()
    chiffres = "0123456789"
    symboles = ",.@#$*"

    caracteres = lettres + lettreMaj + chiffres + symboles

    # garantir au moins un de chaque catégorie
    mot_de_passe = [
        random.choice(lettres),
        random.choice(lettreMaj),
        random.choice(chiffres),
        random.choice(symboles),
    ]

    reste = longueur - len(mot_de_passe)
    for _ in range(reste):
        mot_de_passe.append(random.choice(caracteres))

    random.shuffle(mot_de_passe)
    return "".join(mot_de_passe)
