# Front/length.py
import unicodedata


# Normalisation utile pour traiter des réponses texte ailleurs
def normalize_text(s: str) -> str:
    if s is None:
        return ""
    s = s.strip().lower()
    s = ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn')
    return s

def validate_length(raw_input, current_length):
    """
    Valide l'entrée utilisateur pour la longueur.

    - Si 'non' → retourne 'no'
    - Si nombre < 10 ou > 40 → retourne 'error'
    - Si erreur de conversion → retourne 'error'
    - Si OK → retourne 'yes'

    Retourne : (next_state_candidate, new_length)
    """
    try:
        answer = normalize_text(raw_input)

        # ----- Cas annulation -----
        if answer == "non":
            return "no", current_length

        # ----- Cas numérique -----
        try:
            length = int(answer)
        except ValueError:
            return "error", current_length  # input non numérique

        if length < 10:
            return "error", current_length  # trop petit
        elif length > 40:
            return "error", current_length  # trop grand
        else:
            return "yes", length  # OK

    except Exception as e:
        print(f"[ERREUR][validate_length] {e}")
        return "error", current_length