# Front/graphique.py
import tkinter as tk  # Import de Tkinter pour créer l'interface graphique
from tkinter import ttk, messagebox  # Import des widgets ttk et boîtes de dialogue
import sys, os  # Modules pour manipuler les chemins et le système

# Ajoute le dossier parent au path pour pouvoir importer les modules du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import des modules internes du projet
from Front.question import QUESTIONS, show_question, next_question
from Front.length import validate_length
from back.generator import generate_password
from Front.animation import animate_text

# -------- Variables globales --------
current_state = "start"  # État initial de l'application
current_length = 10      # Longueur par défaut du mot de passe
BG = "#111827"           # Couleur de fond principale

# -------- Fenêtre principale --------
root = tk.Tk()                        # Création de la fenêtre principale
root.title("SecurePass")              # Titre de la fenêtre
root.geometry("640x350")              # Taille initiale (largeur x hauteur)
root.configure(bg=BG)                 # Couleur de fond de la fenêtre

# ---------- Taille minimale ----------
root.minsize(640, 350)  # Empêche de réduire la fenêtre en dessous de cette taille

# -------- Iconbitmap --------
base_dir = os.path.dirname(__file__)          # Récupère le dossier courant
icon_path = os.path.join(base_dir, "UI", "padlock.ico")  # Chemin de l'icône
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)  # Définit l'icône de la fenêtre si elle existe

# -------- Splash screen --------
splash_frame = tk.Frame(root, bg=BG)  # Frame pour le splash screen
splash_frame.pack(fill="both", expand=True)  # Remplit toute la fenêtre

# Label principal du splash
title_label_splash = tk.Label(
    splash_frame, 
    text="SecurePass",
    font=("Segoe UI", 36, "bold"),
    bg=BG, fg="white"
)
title_label_splash.pack(expand=True)  # Centré verticalement et horizontalement

# Label pour l'animation de chargement
loading_label = tk.Label(
    splash_frame, 
    text="Chargement",
    font=("Segoe UI", 14),
    bg=BG, fg="white"
)
loading_label.pack(pady=(0, 50))  # Marge sous le label

# Lancer l'animation du texte de chargement après 100ms
root.after(100, lambda: animate_text(
    loading_label,
    base_text="Chargement",
    duration=1500,
    dots_interval=300,
    end_text="Chargement terminé !"
))

# -------- Lancer l'interface principale --------
def show_main_interface():
    """Affiche l'interface principale après le splash screen"""
    global current_state, current_length

    splash_frame.destroy()  # Supprime le splash screen

    # Frame principal pour l'interface après le splash
    root_frame = tk.Frame(root, bg=BG)
    root_frame.pack(fill="both", expand=True)  # Remplit toute la fenêtre

    # ---------- Widgets principaux ----------
    title_label = tk.Label(
        root_frame, 
        text="SecurePass", 
        font=("Segoe UI", 36, "bold"),
        bg=BG, 
        fg="white"
    )
    title_label.pack(pady=20)  # Marge verticale

    separator = tk.Frame(root_frame, bg="#374151", height=2, width=400)  # Ligne séparatrice
    separator.pack(pady=(0,20))  # Marge sous la ligne

    center_frame = tk.Frame(root_frame, bg=BG)
    center_frame.pack(expand=True, fill="x")  # Frame central qui prend toute la largeur

    # ---------- Question label adaptable ----------
    question_label = tk.Label(
        center_frame, 
        text="", 
        font=("Segoe UI",16),
        bg=BG, fg="white", 
        wraplength=root.winfo_width() - 40,  # Texte se wrap dynamiquement
        justify="center"
    )
    question_label.pack(pady=10, fill="x")  # Remplit horizontalement

    # Frame pour les boutons Oui/Non
    buttons_frame = tk.Frame(center_frame, bg=BG)
    buttons_frame.pack(pady=10)

    # Entry pour saisir la longueur du mot de passe
    entry = ttk.Entry(center_frame, width=45, font=("Segoe UI",14))
    entry.pack()
    entry.pack_forget()  # Caché par défaut

    # Bouton Oui
    yes_button = tk.Button(
        buttons_frame, 
        text="Oui", 
        font=("Segoe UI",14),
        width=10, 
        bg="#4CAF50", 
        fg="white", 
        activebackground="#45a049",
        command=lambda: handle_answer("yes")
    )
    yes_button.grid(row=0, column=0, padx=20)  # Position dans la grille

    # Bouton Non
    no_button = tk.Button(
        buttons_frame, 
        text="Non", 
        font=("Segoe UI",14),
        width=10, 
        bg="#F44336", 
        fg="white", 
        activebackground="#e53935",
        command=lambda: handle_answer("no")
    )
    no_button.grid(row=0, column=1, padx=20)

    # ---------- Fonction de scaling ----------
    import tkinter.font as tkFont  # Import pour manipuler les fonts

    def scale_widgets(event=None):
        """Redimensionne dynamiquement tous les widgets selon la taille de la fenêtre"""
        screen_width = root.winfo_width()  # Largeur actuelle
        screen_height = root.winfo_height()  # Hauteur actuelle

        # ---------- Titre ----------
        base_title_size = min(max(screen_height // 12, 36), 80)  # Taille proportionnelle
        f_title = tkFont.Font(font=title_label['font'])
        f_title.configure(size=base_title_size)
        title_label.config(font=f_title)

        # ---------- Question ----------
        question_size = min(max(screen_height // 35, 14), 28)
        f_question = tkFont.Font(font=question_label['font'])
        f_question.configure(size=question_size)
        question_label.config(font=f_question)
        question_label.config(wraplength=screen_width - 40)  # Ajuste le wraplength

        # ---------- Boutons et Entry ----------
        widget_size = min(max(screen_height // 50, 12), 18)
        for w in [yes_button, no_button, entry]:
            f = tkFont.Font(font=w['font'])
            f.configure(size=widget_size)
            w.config(font=f)

        # ---------- Paddings ----------
        title_label.pack_configure(pady=min(screen_height // 40, 50))
        question_label.pack_configure(pady=min(screen_height // 60, 25))
        yes_button.grid_configure(padx=min(screen_width // 50, 30), pady=min(screen_height // 120, 10))
        no_button.grid_configure(padx=min(screen_width // 50, 30), pady=min(screen_height // 120, 10))

        # ---------- Largeur Entry ----------
        entry.config(width=min(max(25, screen_width // 35), 50))

    # ---------- Lier scaling à redimension ----------
    root.bind("<Configure>", scale_widgets)

    # ---------- Lancer la question initiale ----------
    show_question(
        current_state, 
        current_length, 
        question_label, 
        entry,
        buttons_frame, 
        generate_password, 
        validate_length
    )

    # ---------- Fonction utilitaire pour mettre à jour la question à tout moment ----------
    def update_question(text):
        """Met à jour le texte de question et ajuste le wraplength"""
        question_label.config(text=text)
        question_label.config(wraplength=root.winfo_width() - 40)
        question_label.update_idletasks()  # Force le recalcul de la taille

    # -------- Fonctions de gestion --------
    def handle_answer(answer):
        """Gère les réponses Oui/Non aux questions"""
        global current_state, current_length

        # Si l'état actuel demande de saisir une longueur, ignorer les boutons Oui/Non
        if current_state == "ask_length":
            return

        # Détermine le prochain état en fonction de la réponse donnée
        next_state_val = next_question(current_state, answer)
        if next_state_val:
            current_state = next_state_val  # Met à jour l'état courant

            # Affiche la question correspondante au nouvel état
            show_question(
                current_state, 
                current_length, 
                question_label, 
                entry, 
                buttons_frame, 
                generate_password, 
                validate_length
            )

    def handle_length():
        """Gère la validation de la longueur saisie par l'utilisateur"""
        global current_state, current_length

        # Récupère la valeur entrée par l'utilisateur
        raw = entry.get()

        # Valide la longueur avec la fonction du module length.py
        next_state_val, length = validate_length(raw, current_length)

        if next_state_val == "yes":  # La saisie est valide
            current_length = length  # Met à jour la longueur choisie
            current_state = "show_password"  # Passe à l'état affichage mot de passe

            # Cache l'entrée pendant la génération
            entry.pack_forget()

            # Lance l'animation "Génération en cours..."
            animate_text(
                question_label,
                base_text="Génération en cours",
                duration=1500,
                dots_interval=300,
            )

            # Fonction appelée après la fin visuelle
            def after_animation():
                global current_state
                current_state = "show_password"

                # Réactive boutons
                yes_button.config(state="normal")
                no_button.config(state="normal")

                show_question(
                    current_state,
                    current_length,
                    question_label,
                    entry,
                    buttons_frame,
                    generate_password,
                    validate_length
                )

            # On attend légèrement plus que l'animation
            root.after(1600, after_animation)

        elif next_state_val == "no":  # La saisie est invalide mais pas une erreur critique
            current_state = "start"  # Retour à l'état initial
            messagebox.showinfo("Information", "Retour au menu principal.")
            show_question(
                current_state,
                current_length,
                question_label,
                entry,
                buttons_frame,
                generate_password,
                validate_length
            )

        elif next_state_val == "error":  # Erreur critique dans la saisie
            messagebox.showerror("Erreur", "La longueur doit être un nombre entre 10 et 40")

    # Lie la touche Entrée de l'Entry à la fonction handle_length
    entry.bind("<Return>", lambda e: handle_length())

    # -------- Afficher la première question --------
    # On appelle show_question une première fois pour démarrer l'application
    show_question(
        current_state, 
        current_length, 
        question_label, 
        entry, 
        buttons_frame, 
        generate_password, 
        validate_length
    )

# -------- Lancer main interface après 1.5s --------
root.after(
    1500, 
    show_main_interface
)

# -------- Lancer application --------
root.mainloop()  # Démarre la boucle principale Tkinter