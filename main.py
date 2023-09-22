import random


def choisirBorneMin():
    return int(input("Entrez la borne minimale: "))

def choisirBorneMax():
    return int(input("Entrez la borne maximale: "))

entree = ""

while entree != "n":

    borneMin = choisirBorneMin()
    borneMax = choisirBorneMax()
    reponse = random.randint(borneMin + 1, borneMax - 1)

    print(f"J'ai choisi un nombre entre {borneMin} et {borneMax}. Essaie de le deviner.")

    essai = borneMin
    nombreEssais = 0

    while essai != reponse:
        
        entree = input("Entrez votre essai: ")
        
        essai = int(entree)
        nombreEssais += 1

        if essai < reponse:
            print("C'est trop petit.")

        elif essai > reponse:
            print("C'est trop grand.")
    
    print(f"C'est la bonne reponse! Vous avez reussi en {nombreEssais} essais.")
    entree = input("Voulez-vous reessayer? [Y/n]: ")
