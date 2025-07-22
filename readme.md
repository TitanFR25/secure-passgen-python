# 🔐 Générateur de mot de passe sécurisé — Projet Débutant Python

Bonjour !  
Je débute en Python aujourd’hui, et voici mon **mini-projet** : un **générateur de mot de passe**.

On sait tous qu’en sécurité informatique, un mot de passe solide est **essentiel**.  
Avoir un outil qui le génère automatiquement, en quelques millisecondes, et à la longueur qu’on souhaite, c’est très pratique !

---

## 🚀 Comment l’utiliser ?

> ⚠️ **Pré-requis** :  
> - Avoir installé **l’interpréteur Python** sur votre machine (disponible via le Microsoft Store ou [python.org](https://www.python.org/))  
> - Avoir installé **l’extension Python** dans Visual Studio Code  
> - Avoir installé **Git** pour cloner le projet (ou bien télécharger les fichiers manuellement)

### 📦 Cloner le projet

Si vous ne savez pas comment utiliser Git, voici la commande pour cloner le projet :

```bash
git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git
cd nom-du-repo
```
Si vous n’avez pas Git installé :

Vous pouvez télécharger Git [ici](https://git-scm.com/downloads).


Ou copiez les fichiers manuellement via le bouton vert "Code > Télécharger ZIP" sur GitHub
Sinon, vous pouvez simplement télécharger le fichier .zip depuis GitHub, puis l'extraire.

📦 Installation des dépendances
Avant d'exécuter le programme, vous devez installer les bibliothèques nécessaires :

```bash
pip install -r requirements.txt
```
Si pip ne fonctionne pas, essayez :
```bash
python -m pip install -r requirements.txt
```

#### ▶️ Exécution
Ouvrez le dossier dans Visual Studio Code

Clic droit sur main.py > "Run Python File in Terminal"
ou utilisez le terminal :

```bash
python python/main.py
```
💡 Si python ne fonctionne pas, essayez :
```bash
python3 python/main.py
```

Le programme vous demandera :

Quel longueur voulez-vous pour votre mot de passe ? (minimum 10 / maximum 40) :
Tapez la longueur souhaitée (ex. : 15)

Le mot de passe sera généré et affiché immédiatement :

```bash
🔐 Voici votre mot de passe : Nd.V#RBBpjjaTfU 
```
#### 🎯 Fonctionnalités :
✅ Longueur personnalisable entre 10 et 40 caractères

✅ Contient au minimum :

1 lettre minuscule

1 lettre majuscule

1 chiffre

1 symbole

Mélange totalement aléatoire

✅ Possibilité de chiffrer le mot de passe

✅ Sauvegarde du mot de passe et d'autres données dans un fichier .txt

##### 🛠️ Améliorations possibles (pour la suite)

1. Ajouter une option pour choisir les types de caractères inclus (ex : exclure les symboles)

2. Proposer une interface graphique simple

3. Enregistrer les mots de passe de façon chiffrée

4. Ajouter une fonctionnalité de vérification de robustesse des mots de passe

##### 🔒 Attention à la sécurité

1. Si vous choisissez de sauvegarder votre mot de passe dans un fichier .txt, faites attention à l’endroit où vous le stockez.

2. Ne partagez pas ces fichiers sur des plateformes publiques ou avec des personnes non autorisées.

3. Pour un usage sérieux, préférez un gestionnaire de mots de passe spécialisé (comme Bitwarden, KeePass, 1Password).

4. Ce programme est un projet pédagogique, il ne doit pas être utilisé pour stocker des données sensibles en production.

Merci d’avoir pris le temps de découvrir ce projet !
N’hésitez pas à le tester et à me faire vos retours.
Bonne génération de mots de passe ! 🔐