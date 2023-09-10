# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:58:12 2023

@author: enric
"""
Champan = " "

for i in range (1,10**6):
    I = str (i)
    Champan = Champan + I
    
for j in range(0,6):
    print(Champan[10**j])
    