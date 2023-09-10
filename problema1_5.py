# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:21:22 2023

@author: enric
"""
prod=1
 
def encuentradigito(n):
    i=0
    while n>0:
        m = n
        n += -9*10**(i)*(i+1)
        i += 1
    m = m-1
    x = m//i
    y = m%i
    j=10**(i-1)+x
    jcadenado = str(j)
    digito = jcadenado[y]
    return digito

for k in range(6):
    d = encuentradigito(10**k)
    ddigitado = int(d)
    prod = prod*ddigitado
    
print(prod)   