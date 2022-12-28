# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:34:59 2022

@author: Ivan Tonatiuh
"""



cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
listaPalabras = cadenaPalabras.split()

print(listaPalabras[0:4])
-> ['it', 'was', 'the', 'best']

print(listaPalabras[0:6])
-> ['it', 'was', 'the', 'best', 'of', 'times']

print(listaPalabras[6:10])
-> ['it', 'was', 'the', 'worst']

print(listaPalabras[0:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(listaPalabras[:12])
-> ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']

print(listaPalabras[12:])
-> ['it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']