s1="automatisation de test"
s2='test manuel'
s3= """
test automatisé
avec sélénium
"""
s4='''
test automatisé 
avec RobotFramework
'''
print(type(s1))   # meme type str
print(type(s2))
print(type(s3))
print(type(s4))
# la différence  les triples cotes permets d'afficher telle que écrit et conserver l'affichage
print(s1)
print(s2)
print(s3)
print(s4)
# pour différencier l'appostrophe du str
s5="L'hiverprochain il fera chaud"
# pour utiliser le double code on utilise single code
s6='cet hiver est "éxcessivement" froid'
s7='L\'hiver prochain il va faire chaud'
#slicing (découpage de la chaine de caractère)
s1="automatisation de test"
print(len(s1))
#indexation dans une liste
print(s1[0])
print(s1[8])
print(s1[21])
#parcours inverse
print(s1[-1])
# concatiner chaine de caractères
s7=s1+" "+s2
print(s7)
s9=s1*9
print(s9)