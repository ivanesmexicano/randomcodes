# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:55:44 2022

@author: Ivan Tonatiuh
"""


tex_to=text_yt     

str_list = tex_to.split()
 
# gives set of unique words
unique_words = set(str_list)
w=[]
c=[]
i=0
   
 
for words in unique_words :
    #print('Frequency of ', words , 'is :', str_list.count(words))
    w.append(words)
    c.append(str_list.count(words))
    i+=1
    #print(i)
        
    #print(w)
    #print(c)

import numpy as np
import pandas as pd
df = pd.DataFrame(np.column_stack([w, c]), columns=['words', 'freq'])

df.to_excel("YTconteofrecuencias.xlsx")

#%% hacer frases para salir del paso

lista_artificial=["trabajo","profesional","honesto","honrado","formación","conocimiento","donde aprender","curso","aprender","cambio de aceite","aceite de motor","mantenimiento","llantas","motor","tipos de aceites","mejor aceite","aprendizaje","experiencias","información","vehículos","poder","mecánica","profesionales","aprender mecánica"]

#with open("input_text.txt") as file:
#text_IGN = text_filtered.read()


#n = text.count("aceite de motor")
#print(n)
#%%


frequ=[]
for frase in lista_artificial:
    
    frequ.append(tex_to.count(frase))
    
dfART = pd.DataFrame(np.column_stack([lista_artificial, frequ]), columns=['phrase', 'freq'])
dfART.to_excel("IGconteofrecuenciasenfrase.xlsx")

#%%

import nltk

listOfFreq= nltk.FreqDist(filtered_sentence)
FreqDF= pd.DataFrame(list(listOfFreq.items()), columns = ["Word","Frequency"]) 



