# Front/graphique.py
import tkinter as tk
from tkinter import ttk, messagebox
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Front.question import QUESTIONS, show_question, next_question
from Front.length import validate_length
from back.generator import generate_password
from Front.animation import animate_text

# -------- Variables globales --------
current_state = "start"
current_length = 10
BG = "#111827"

# -------- Fenêtre principale --------
root = tk.Tk()
root.title("SecurePass")
root.geometry("640x350")
root.configure(bg=BG)
root.minsize(640, 350)

base_dir = os.path.dirname(__file__)
icon_path = os.path.join(base_dir, "UI", "padlock.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# -------- Splash screen --------
splash_frame = tk.Frame(root, bg=BG)
splash_frame.pack(fill="both", expand=True)

title_label_splash = tk.Label(
    splash_frame,
    text="SecurePass",
    font=("Segoe UI", 36, "bold"),
    bg=BG, fg="white"
)
title_label_splash.pack(expand=True)

loading_label = tk.Label(
    splash_frame,
    text="Chargement",
    font=("Segoe UI", 14),
    bg=BG, fg="white"
)
loading_label.pack(pady=(0, 50))

root.after(100, lambda: animate_text(
    loading_label,
    base_text="Chargement",
    duration=1500,
    dots_interval=300,
    end_text="Chargement terminé !"
))

# -------- Interface principale --------
def show_main_interface():
    global current_state, current_length

    splash_frame.destroy()

    root_frame = tk.Frame(root, bg=BG)
    root_frame.pack(fill="both", expand=True)

    title_label = tk.Label(
        root_frame,
        text="SecurePass",
        font=("Segoe UI", 36, "bold"),
        bg=BG,
        fg="white"
    )
    title_label.pack(pady=20)

    separator = tk.Frame(root_frame, bg="#374151", height=2, width=400)
    separator.pack(pady=(0, 20))

    center_frame = tk.Frame(root_frame, bg=BG)
    center_frame.pack(expand=True, fill="x")

    question_label = tk.Label(
        center_frame,
        text="",
        font=("Segoe UI", 16),
        bg=BG,
        fg="white",
        wraplength=root.winfo_width() - 40,
        justify="center"
    )
    question_label.pack(pady=10, fill="x")

    buttons_frame = tk.Frame(center_frame, bg=BG)
    buttons_frame.pack(pady=10)

    entry = ttk.Entry(center_frame, width=45, font=("Segoe UI", 14))
    entry.pack()
    entry.pack_forget()

    yes_button = tk.Button(
        buttons_frame,
        text="Oui",
        font=("Segoe UI", 14),
        width=15,
        bg="#4CAF50",
        fg="white",
        command=lambda: handle_answer("yes")
    )
    yes_button.grid(row=0, column=0, padx=20)

    no_button = tk.Button(
        buttons_frame,
        text="Non",
        font=("Segoe UI", 14),
        width=15,
        bg="#F44336",
        fg="white",
        command=lambda: handle_answer("no")
    )
    no_button.grid(row=0, column=1, padx=20)

        # ---------- Fonction de scaling ----------
    import tkinter.font as tkFont

    def scale_widgets(event=None):
        """Redimensionne dynamiquement tous les widgets selon la taille de la fenêtre"""

        screen_width = root.winfo_width()
        screen_height = root.winfo_height()

        # ---------- Titre ----------
        base_title_size = min(max(screen_height // 12, 36), 80)
        f_title = tkFont.Font(font=title_label['font'])
        f_title.configure(size=base_title_size)
        title_label.config(font=f_title)

        # ---------- Question ----------
        question_size = min(max(screen_height // 35, 14), 28)
        f_question = tkFont.Font(font=question_label['font'])
        f_question.configure(size=question_size)
        question_label.config(font=f_question)
        question_label.config(wraplength=screen_width - 40)

        # ---------- Boutons et Entry ----------
        widget_size = min(max(screen_height // 50, 12), 18)

        for w in [yes_button, no_button, entry]:
            f = tkFont.Font(font=w['font'])
            f.configure(size=widget_size)
            w.config(font=f)

        # ---------- Paddings dynamiques ----------
        title_label.pack_configure(pady=min(screen_height // 40, 50))
        question_label.pack_configure(pady=min(screen_height // 60, 25))

        try:
            yes_button.grid_configure(
                padx=min(screen_width // 50, 30),
                pady=min(screen_height // 120, 10)
            )
            no_button.grid_configure(
                padx=min(screen_width // 50, 30),
                pady=min(screen_height // 120, 10)
            )
        except:
            pass

        # ---------- Largeur Entry ----------
        entry.config(width=min(max(25, screen_width // 35), 50))

    # ---------- Lier scaling ----------
    root.after(50, lambda: root.bind("<Configure>", scale_widgets))

    # -------- MENU PRINCIPAL --------
    def show_main_menu():
        global current_state
        current_state = "main_menu"

        question_label.config(
            text="Bienvenue sur SecurePass\n\nVeuillez sélectionner une option."
        )

        entry.pack_forget()

        buttons_frame.pack(pady=10)

        # On remet bien les deux boutons dans la grille
        yes_button.grid(row=0, column=0, padx=20)
        no_button.grid(row=0, column=1, padx=20)

        yes_button.config(
            text="Première utilisation",
            command=start_first_time_flow
        )

        no_button.config(
            text="Utilisateur existant",
            command=start_standard_flow
        )

    # -------- FLOW UTILISATEUR STANDARD --------
    def start_standard_flow():
        global current_state
        current_state = "ask_length"

        yes_button.config(
            text="Oui",
            command=lambda: handle_answer("yes")
        )

        no_button.config(
            text="Non",
            command=lambda: handle_answer("no")
        )

        show_question(
            current_state,
            current_length,
            question_label,
            entry,
            buttons_frame,
            generate_password,
            validate_length
        )

    # -------- FLOW PREMIÈRE UTILISATION --------
    def start_first_time_flow():
        global current_state
        current_state = "onboarding"

        question_label.config(
            text="Bienvenue \n\nSecurePass va vous guider pour créer votre premier mot de passe sécurisé.\n\nCommençons par choisir la longueur."
        )

        entry.pack_forget()

        yes_button.config(
            text="Commencer",
            command=start_standard_flow
        )

        no_button.grid_remove()

    # -------- GESTION DES RÉPONSES --------
    def handle_answer(answer):
        global current_state, current_length

        if current_state == "ask_length":
            return

        next_state_val = next_question(current_state, answer)

        if next_state_val:
            current_state = next_state_val
            show_question(
                current_state,
                current_length,
                question_label,
                entry,
                buttons_frame,
                generate_password,
                validate_length
            )

    # -------- VALIDATION LONGUEUR --------
    def handle_length():
        global current_state, current_length

        raw = entry.get()
        next_state_val, length = validate_length(raw, current_length)

        if next_state_val == "yes":
            current_length = length
            entry.pack_forget()

            animate_text(
                question_label,
                base_text="Génération en cours",
                duration=1500,
                dots_interval=300,
            )

            def after_animation():
                global current_state
                current_state = "show_password"

                show_question(
                    current_state,
                    current_length,
                    question_label,
                    entry,
                    buttons_frame,
                    generate_password,
                    validate_length
                )

            root.after(1600, after_animation)

        elif next_state_val == "no":
            messagebox.showinfo("Information", "Retour au menu principal.")
            show_main_menu()

        elif next_state_val == "error":
            messagebox.showerror("Erreur", "La longueur doit être un nombre entre 10 et 40")

    entry.bind("<Return>", lambda e: handle_length())

    # 👉 On lance maintenant le menu principal au lieu de show_question()
    show_main_menu()

# -------- Lancer main interface --------
root.after(1500, show_main_interface)
root.mainloop()