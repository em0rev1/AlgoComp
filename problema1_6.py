# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:02:27 2023

@author: enric
"""

def cambiar5por3(n):
    N = str(n)
    K = " "
    for w in N:
        if w == "5":
            w = "3"
        K = K + w
    K = int(K)
    return K