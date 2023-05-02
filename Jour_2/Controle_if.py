
a=int(input("donner l'heure:     "))
if (a<19):
    print("Bonjour!")
else:
    print("c'est nuit! bonsoir!")
#saisie utilisateur
nom=input("Entrer votre nom:     ").upper().strip()
if nom=="SOUMAYA":
    print("Salut Soumaya")
else:
    print("C'est pas ton poste!")

"""a=20
b=20
if b>a:
    print("b est plus grand")
elif a==b:
    print("a est égal a b")"""
equipe= input("Quel est ton équipe préfèrée:   ").lower().strip()
if equipe=="brésil":
    print("est ce que le capitaine est présent?")
elif equipe=="argentine":
    print("Combient de buts vous avez marqué aujourd'hui")
elif equipe=="tunisie":
    print("vous devez travailler plus!")
else:
    print("Oups! je connais pas!")

