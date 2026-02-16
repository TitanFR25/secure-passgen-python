# front.py
import tkinter as tk
from tkinter import ttk
import sys, os

# Ajouter le dossier racine Project/ au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Front.question import QUESTIONS
from back.generator import generate_password

# -------- Fenêtre principale --------
root = tk.Tk()
root.title("Secure-passgen")

base_dir = os.path.dirname(__file__)
icon_path = os.path.join(base_dir, "UI", "padlock.ico")
root.iconbitmap(icon_path)
root.geometry("640x350")
BG = "#111827"
root.configure(bg=BG)

current_state = "start"

# -------- Style --------
style = ttk.Style()
style.configure("Big.TEntry")

# -------- Splash screen --------
splash_frame = tk.Frame(root, bg=BG)
splash_frame.pack(fill="both", expand=True)

title_label = tk.Label(
    splash_frame,
    text="SecurePass",
    font=("Segoe UI", 36, "bold"),
    bg=BG,
    fg="white"
)
title_label.pack(expand=True)

loading_label = tk.Label(
    splash_frame,
    text="Chargement",
    font=("Segoe UI", 14),
    bg=BG,
    fg="white"
)
loading_label.pack(pady=(0, 50))

# Animation des points "..."
def animate_loading(dots=0):
    loading_label.config(text="Chargement" + "." * dots)
    dots = (dots + 1) % 4  # 0,1,2,3, puis revient à 0
    root.after(500, animate_loading, dots)  # mise à jour toutes les 0,5s

animate_loading()

# -------- Fonction pour lancer l'interface principale --------
def show_main_interface():
    splash_frame.destroy()  # Supprime le splash screen

    # -------- Frame principal --------
    root_frame = tk.Frame(root, bg=BG)
    root_frame.pack(fill="both", expand=True)

    # -------- Titre en haut --------
    title_label = tk.Label(
        root_frame,
        text="SecurePass",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg="white"
    )
    title_label.pack(pady=(20, 10))

    # -------- Ligne séparatrice --------
    separator = tk.Frame(root_frame, bg="#374151", height=2, width=400)
    separator.pack(pady=(0, 20))

    # -------- Contenu central --------
    center_frame = tk.Frame(root_frame, bg=BG)
    center_frame.pack(expand=True)

    question_label = tk.Label(
        center_frame,
        text=QUESTIONS[current_state]["text"],
        font=("Segoe UI", 13),
        bg=BG,
        fg="white",
        wraplength=600
    )
    question_label.pack(pady=10)

    #Frame pour les boutton 
    buttons_frame = tk.Frame(center_frame, bg=BG)
    buttons_frame.pack()

    #Fonction pour afficher la prochaine question
    def show_question(state):
        question_label.config(text=QUESTIONS[state]["text"])
        return state
        text = QUESTIONS
    
    #Fonction appelées par les bouton
    def next_question(answer):
        global current_state
        next_state= QUESTIONS[current_state].get(answer)
        if next_state is None:
            root.quit()
        else:
            current_state = next_state
            show_question(current_state)
        

        
    
    #Créer les 2 bouton oui/non
    yes_button = tk.Button(
        buttons_frame, 
        text="Oui",
        font=("Segoe UI",11),
        command=lambda: next_question("yes"),
        width=10,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049"
    )
    yes_button.grid(row=0, column=0, padx=20)

    no_button = tk.Button(
        buttons_frame, 
        text="Non",
        font=("Segoe UI",11),
        command=lambda: next_question("no"),
        width=10,
        bg="#F44336",
        fg="white",
        activebackground="#e53935"
    )
    no_button.grid(row=0, column=1, padx=20)

     # Afficher la première question après 200ms pour un effet "chargement"
    root.after(200, lambda: show_question(current_state))

# -------- Lancer le main interface après 1,5s --------
root.after(1500, show_main_interface)

# -------- Lancer l'interface --------
root.mainloop()
