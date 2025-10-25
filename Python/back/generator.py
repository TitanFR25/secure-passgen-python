# back.py
import random
import unicodedata

# Normalisation utile si tu veux traiter des réponses texte ailleurs
def normalize_text(s: str) -> str:
    if s is None:
        return ""
    s = s.strip().lower()
    s = ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn')
    return s

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


# --- Moteur de dialogue simple (oui/non) avec actions ---
YES_TOKENS = {"oui", "o", "y", "yes", "1", "true", "vrai"}
NO_TOKENS  = {"non", "n", "no", "0", "false", "faux"}

def interpret_yes_no(s: str) -> str:
    if s is None:
        return "unknown"
    s_norm = normalize_text(s)
    if s_norm in YES_TOKENS:
        return "yes"
    if s_norm in NO_TOKENS:
        return "no"
    if s_norm.startswith("o"):
        return "yes"
    if s_norm.startswith("n"):
        return "no"
    return "unknown"

# Questions simples (à adapter)
QUESTIONS = {
    "start": {
        "text": "Souhaites-tu générer un mot de passe maintenant ? (oui / non)",
        "yes": "ask_length",
        "no": "goodbye"
    },
    "ask_length": {
        "text": "Quelle longueur veux-tu ? (entre 10 et 40). Réponds avec un nombre ou 'non' pour annuler.",
        "yes": "unused",  # pas utilisé ici ; on traitera la réponse texte
        "no": "goodbye"
    },
    "show_password": {
        "text": "Mot de passe généré : {password}\nVeux-tu en générer un autre ? (oui/non)",
        "yes": "ask_length",
        "no": "goodbye"
    },
    "goodbye": {
        "text": "D'accord. À bientôt !",
        "yes": None,
        "no": None
    }
}

class DialogueEngine:
    def __init__(self, questions=QUESTIONS):
        self.questions = questions
        self.ctx = {}
        self.current = "start"

    def get_current_text(self):
        node = self.questions[self.current]
        text = node["text"]
        try:
            return text.format(**self.ctx)
        except Exception:
            return text

    def process_answer(self, raw_answer: str):
        """
        Comportements :
        - Si on est dans 'ask_length' et la réponse est un entier -> génère le mdp.
        - Sinon interprète comme oui/non pour naviguer.
        Retourne dict: {status: 'next'|'unknown'|'end'|'error', message: str}
        """
        node = self.questions[self.current]

        # cas spécial : on attend une longueur (noeud ask_length)
        if self.current == "ask_length":
            if raw_answer is None:
                return {"status": "unknown", "message": "Donne un nombre entre 10 et 40 ou 'non'."}
            s = raw_answer.strip()
            if s == "":
                return {"status": "unknown", "message": "Réponse vide — donne un nombre entre 10 et 40 ou 'non'."}
            # si l'utilisateur répond 'non'
            if interpret_yes_no(s) == "no":
                self.current = "goodbye"
                return {"status": "end", "message": self.get_current_text()}
            # tenter d'interpréter comme entier
            try:
                longeur = int(s)
            except Exception:
                return {"status": "unknown", "message": "Veuillez entrer un nombre entier entre 10 et 40, ou 'non'."}
            # try générer
            try:
                pwd = generate_password(longeur)
            except ValueError as e:
                return {"status": "unknown", "message": str(e)}
            # stocker et avancer
            self.ctx["length"] = longeur
            self.ctx["password"] = pwd
            self.current = "show_password"
            return {"status": "next", "message": self.get_current_text()}

        # sinon on attend un oui/non
        parsed = interpret_yes_no(raw_answer)
        if parsed == "unknown":
            return {"status": "unknown", "message": "Réponds par 'oui' ou 'non' (ou utilise les boutons)."}
        target = node.get(parsed)
        if target is None:
            return {"status": "end", "message": self.get_current_text()}
        if isinstance(target, str):
            self.current = target
            return {"status": "next", "message": self.get_current_text()}
        return {"status": "error", "message": "Flux non reconnu."}

    def reset(self):
        self.ctx = {}
        self.current = "start"