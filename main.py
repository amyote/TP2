import random


# Fonction qui demande a l'utilisateur pour une borne minimale. Retourne l'entree de l'utilisateur, en int.
def choisirBorneMin():
    return int(input("Entrez la borne minimale: "))

# Fonction qui demande a l'utilisateur pour une borne maximale. Retourne l'entree de l'utilisateur, en int.
def choisirBorneMax():
    return int(input("Entrez la borne maximale: "))

entree = ""

while entree != "n":

    # Placer les bornes et choisir un nombre. Annoncer a l'utilisateur.
    borneMin = choisirBorneMin()
    borneMax = choisirBorneMax()
    reponse = random.randint(borneMin + 1, borneMax - 1)

    print(f"J'ai choisi un nombre entre {borneMin} et {borneMax}. Essaie de le deviner.")

    essai = borneMin
    nombreEssais = 0

    # Boucle du jeu.
    while essai != reponse:
        
        entree = input("Entrez votre essai: ")
        
        essai = int(entree)
        nombreEssais += 1

        # Dire si c'est trop petit ou trop grand.
        if essai < reponse:
            print("C'est trop petit.")

        elif essai > reponse:
            print("C'est trop grand.")
    
    # Une fois qu'ils ont gagne, afficher le nombre d'essais et demander s'ils veulent rejouer.
    print(f"C'est la bonne reponse! Vous avez reussi en {nombreEssais} essais.")
    entree = input("Voulez-vous reessayer? [Y/n]: ")
