#retrouver les mots réservés de python (Keywords)
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
a=25  #    :identifiant doivent etre différents de Python Keywords exp : as=25
#123somme=25  les identifiants ne commencent pas par un nobre
somme113=25
#somme$=25  #les identifiants ne doit pas contenir un caractère spécial
_somme=25  # un identifiant peut commencer par underscore (variable privé)
def maFonction():
    pass