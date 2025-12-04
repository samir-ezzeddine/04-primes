"""Module pour tester si un entier est un nombre premier ou non."""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Retourne True si p est un nombre premier, sinon False."""
    if p < 2:
        return False

    if p ==2:
        return True

    if p % 2 == 0:
        return False

    for i in range (2, int(sqrt(p)) + 1 ):
        if p % i == 0:
            return False

    return True
#### Fonction principale


def main():

    """Affiche tous les nombres premiers strictement inférieurs à 100."""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
