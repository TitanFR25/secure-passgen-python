import random

#on definit quel type de caractere on va utiliser
lettres = "azertyuiopqsdfghjklmwxcvbnéàè"
lettreMaj = lettres.upper()
chiffre = "123456789"
symbole = ",.@#$*"

#on stock tout sa dans une variable caractere
caractere = lettres + lettreMaj + chiffre + symbole

#on defini la variable longueur qui definira la longueur du mot de passe que l'utilisateur aura choisis

#On vien verifier si l'utilisateur entre un nombre entier sinon on sort une erreur
try:
    longueur = int(input("Quel longueur voulez-vous pour votre mot de passe ? (minimum 10 / maximum 40) :"))
except ValueError:
    print("Erreur entrer un nombre entier")
    exit()

#on vérifie que la longueur choisis respecte les régle
if longueur < 10 or longueur > 40:
    print("Erreur le mot de passe doit contenir entre 10 et 40 caractere")
    exit()
else:
    #si la longueur et bonne on vien génerer le mot de passe

    #on vien definir que le mot de passe doit avoir au minimin 1 caractere de chaque type sous forme de tableau
    mot_de_passe = [
        random.choice(lettres),
        random.choice(lettreMaj),
        random.choice(chiffre),
        random.choice(symbole)
    ]

    #on defini les caractere manquant
    reste = longueur - 4

    #on vien completer le reste par des caractere aleatoire
    for _ in range(reste):
        mot_de_passe.append(random.choice(caractere))

    #on melange les caractere
    random.shuffle(mot_de_passe)

    #on vien stocker le mot de passe dans une variable de type texte(string)
    mot_de_passe_final = "".join(mot_de_passe)

    #on vien afficher le mot de passe demandé
    print("🔐 Voici le mot de passe:", mot_de_passe_final)