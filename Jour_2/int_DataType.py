a=10
print(type(a))  #système décimal
#système numérique: décimal
#on peut representer le système numérique en plusieurs formes: décimal, binaire, hexadécimal, octal

#représentation binaire
somme=0b01111
print(somme)    #0b pour dire que la variable est présentée en binaire 0 et 1
total=(0B11110001)
print(total)
#representation octale
b=0o365472
print(b)       #0o pour dire que la variable est présentée en octale entre 0 et 7
c=0o2564221300
print(c)

#représentation hexadécimale de 0 a 9 et de A/a  --F/f
d=0xface
print(d)    #0x ou 0X pour dire que la variable est présentée en hexadécimale entre 0 a 9 et de A/a  --F/f

#conversion de base
#commentaire1: conversion binaire/octal/hexadécimale
k=25
print(oct(k))
print(bin(k))
print(hex(k))