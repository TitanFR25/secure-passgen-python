# Front/question.py

from back.generator import generate_password

# Questions et états
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
        "yes":  None,  # à compléter
        "no": "goodbye"
    },
    "ask_encryption": {
        "text": "Voulez vous le chiffrer ?",
        "yes": "ask_save",
        "no": "goodbye"
    },
    "ask_generate": {
        "text": "Voulez vous générer un mot de passe ?",
        "yes": "ask_length",
        "no": "goodbye"
    },
    "ask_length": {
        "text": "Quelle longueur voulez vous ? (entre 10 et 40). Répondez avec un nombre ou 'non' pour annuler.",
        "yes": "show_password",
        "no": "start"
    },
    "show_password": {
        "text": "Mot de passe généré : {password}\nVoulez-vous en générer un autre ?",
        "yes": "ask_length",
        "no": "ask_save"
    },
    "ask_save": {
        "text": "Voulez vous sauvegarder votre mot de passe ?",
        "yes": None,  # à compléter
        "no": "goodbye"
    },
    "goodbye": {
        "text": "D'accord. À bientôt !",
        "yes": None,
        "no": None
    }
}

# -------- Fonctions --------
def next_question(current_state, answer):
    """Détermine le prochain état en fonction de la réponse ('yes'/'no')"""
    if current_state not in QUESTIONS:
        print(f"[DEBUG][next_question] État invalide : '{current_state}'")
        return None

    next_state = QUESTIONS[current_state].get(answer)
    if next_state is None:
        print(f"[DEBUG][next_question] Aucun état suivant pour '{answer}' dans '{current_state}'")
    return next_state

def show_question(
    state,
    current_length,
    question_label,
    entry,
    buttons_frame,
    generate_password_fn,
    validate_length_fn
):
    """
    Affiche la question correspondant à l'état donné.
    Gère aussi le cas spécial 'show_password' et 'goodbye'.
    """
    try:
        if state not in QUESTIONS:
            raise ValueError(f"[show_question] État inconnu : '{state}'")

        text = QUESTIONS[state]["text"]

        # ----- Cas particulier : génération du mot de passe -----
        if state == "show_password":
            password = generate_password_fn(current_length)
            text = text.format(password=password)

        question_label.config(text=text)

        # ----- Gestion ask_length -----
        if state == "ask_length":
            entry.pack(ipady=4)
            entry.delete(0, "end")
            entry.insert(0, str(current_length))
            buttons_frame.pack_forget()
            entry.focus_set()
        # ----- Gestion goodbye -----
        elif state == "goodbye":
            entry.pack_forget()
            buttons_frame.pack_forget()
            # Ferme l'application après 2 secondes
            question_label.after(2000, question_label.master.quit)
        else:
            entry.pack_forget()
            buttons_frame.pack(pady=10)

    except Exception as e:
        print(f"[ERREUR][show_question] {e}")