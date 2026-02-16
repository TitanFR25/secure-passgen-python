# Questions simples (à adapter)
QUESTIONS = {
    "start": {
        "text": "Possédez-vous déjà le fichier qui sauvegarde vos données ?",
        "yes": "ask_alr_encryption",
        "no": "ask_generate"
    },
    "ask_alr_encryption": { 
        "text": "Avez-vous chiffré votre mot de passe dans ce fichier ?",
        "yes": "ask_decryption",
        "no": "ask_encryption"
    },
    "ask_decryption": {
        "text": "Souhaitez-vous déchiffrer votre mot de passe ?",
        "yes": "?",
        "no": "goodbye"
    },
    "ask_encryption": {
        "text": "Voulez vous le chiffrer ?",
        "yes": "?",
        "no": "goodbye"
    },
    "ask_generate": {
        "text": "Voulez vous générer un mot de passe ?",
        "yes": "ask_length",
        "no": "goodbye"
    },
    "ask_length": {
        "text": "Quelle longueur voulez vous ? (entre 10 et 40). Répondez avec un nombre ou 'non' pour annuler.",
        "yes" : None,
        "no": "goodbye"
    },
    "show_password": {
        "text": "Mot de passe généré : {password}\nVeux-tu en générer un autre ? (oui/non)",
        "yes": "ask_length",
        "no": "ask_save"
    },
    "ask_save":{
        "text": "Voulez vous sauvegarder votre mot de passe ?",
        "yes": "?",
        "no": "goodbye"
    },
    "goodbye": {
        "text": "D'accord. À bientôt !",
        "yes": None,
        "no": None
    }
}