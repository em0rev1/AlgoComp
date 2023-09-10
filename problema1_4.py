# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:07:18 2023

@author: enric
"""
k =  1000000
Lmax = 0

# comprobados = {1}

def collatz(n):
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    return n

for j in range(1,k):
    n = j
    longitud = 1
    while n != 1:
        n = collatz(n)
        longitud += 1
    if longitud > Lmax:
        (largo, Lmax) = (j, longitud)
print(largo, Lmax)

#    longitud += L

#for n in range(2,k):
#    suc = {n}
#    flag = True
#    longitud = 0
#    if n in comprobados:
#        flag = False
#    while flag:
#        n = collatz(n)
#        longitud += 1
#        suc = suc | {n} 
#        if n in comprobados:
#            flag = False
#            L = long(n) # devuelve la longitud de la cadena a partir de n
#    longitud += L
#    comprobados = comprobados | suc
#    print (comprobados)
#    # guardar longitud de comprobados