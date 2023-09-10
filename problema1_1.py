# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:52:48 2023

@author: enric
"""
def calcula11(n):
    q3=(n-1)//3
    q5=(n-1)//5
    q15=(n-1)//15
    a1=3*q3*(q3+1)//2
    a2=5*q5*(q5+1)//2
    a3=15*q15*(q15+1)//2
    tot = a1 + a2 - a3
    return(tot)
