# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:56:20 2023

@author: enric
"""

(a,b)=(0,1)
suma = 0
n = 4*10**6
while b < n:
    if b%2 == 0:
        suma += b
    (a,b) = (b,a+b)
print(suma)