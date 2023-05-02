#ecrire un programme qui trouve le plus grand nombre parmi deux nombres avec un prompt(saisie)
try:
    nbre1 = int(input("Donner le premier nombre : "))     #type casting
    nbre2 = int(input("Donner le deuxième nombre : "))
except ValueError:
    print("Erreur : la valeur n'est pas un nombre entier")
else:
    if nbre1 > nbre2:
        print(nbre1, " est plus grand !")
    elif nbre1 < nbre2:
        print(nbre2, " est plus grand !")
    else:
        print(nbre1, " est égal à ", nbre2)