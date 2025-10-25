# front.py
import tkinter as tk
from tkinter import messagebox, filedialog
import sys, os

from back.generator import DialogueEngine

# gestion du chemin pour icon (utile si tu créés un .exe avec PyInstaller)
def resource_path(relative):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.dirname(__file__), relative)

engine = DialogueEngine()

root = tk.Tk()
root.title("Générateur interactif")
root.geometry("540x260")
BG = "#111827"
root.configure(bg=BG)

frame = tk.Frame(root, bg=BG, padx=12, pady=12)
frame.pack(fill="both", expand=True)

question_var = tk.StringVar(value=engine.get_current_text())
status_var = tk.StringVar(value="")

label = tk.Label(frame, textvariable=question_var, bg=BG, fg="#0F1724", wraplength=500, justify="left", font=("Segoe UI", 12))
label.pack(anchor="w", pady=(0,10))

entry = tk.Entry(frame, width=36, font=("Consolas", 12))
entry.pack(anchor="w")

status_label = tk.Label(frame, textvariable=status_var, bg=BG, fg="#B00020", font=("Segoe UI", 10))
status_label.pack(anchor="w", pady=(6,0))

def update_question(text):
    question_var.set(text)
    entry.delete(0, tk.END)
    status_var.set("")

def handle_response(raw=None):
    if raw is None:
        raw = entry.get()
    result = engine.process_answer(raw)
    if result["status"] == "unknown":
        status_var.set(result["message"])
    elif result["status"] == "error":
        status_var.set("Erreur interne.")
    elif result["status"] == "end":
        update_question(result["message"])
        # si password dans ctx on affiche bouton pour sauvegarder
        if "password" in engine.ctx:
            show_password_and_save(engine.ctx["password"])
    elif result["status"] == "next":
        update_question(result["message"])
        # si on vient d'arriver sur show_password, afficher popup
        if "password" in engine.ctx and engine.current == "show_password":
            show_password_and_save(engine.ctx["password"])

def show_password_and_save(password):
    # Popup d'information
    messagebox.showinfo("Mot de passe généré", f"🔐 {password}")
    # Proposer de sauvegarder
    if messagebox.askyesno("Sauvegarder", "Veux-tu sauvegarder ce mot de passe dans un fichier texte ?"):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt")],
            title="Sauvegarder le mot de passe",
            initialfile="mot_de_passe.txt"
        )
        if save_path:
            try:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(password)
                messagebox.showinfo("Enregistré", f"Mot de passe sauvegardé dans :\n{save_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'enregistrer le fichier :\n{e}")

# boutons rapides
btn_frame = tk.Frame(frame, bg=BG)
btn_frame.pack(anchor="w", pady=12)

def btn_yes(): handle_response("oui")
def btn_no(): handle_response("non")

yes_btn = tk.Button(btn_frame, text="Oui", width=10, command=btn_yes, bg="#0B63B7", fg="white")
no_btn  = tk.Button(btn_frame, text="Non", width=10, command=btn_no, bg="#E02424", fg="white")
send_btn = tk.Button(btn_frame, text="Envoyer texte", command=lambda: handle_response(None))

yes_btn.grid(row=0, column=0, padx=(0,8))
no_btn.grid(row=0, column=1, padx=(0,8))
send_btn.grid(row=0, column=2)

# Menu : reset / quitter
menu = tk.Menu(root)
root.config(menu=menu)
app_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="App", menu=app_menu)
app_menu.add_command(label="Réinitialiser", command=lambda: (engine.reset(), update_question(engine.get_current_text())))
app_menu.add_separator()
app_menu.add_command(label="Quitter", command=root.destroy)

root.mainloop()
